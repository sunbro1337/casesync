import logging
import os
from logger import create_logger

from project import Project
from testrail.requests import *
from file_manager import create_yaml, read_yaml, check_path, check_name, remove_path, get_dict_value_from_list
from testrail.cases_methods import GetMethod, PostMethod


logger = create_logger('Workspace', logger_lvl=logging.INFO)


class Workspace:
    def __init__(self, project: Project):
        logger.debug("Start init Workspace")
        self.project = project
        assert self.project
        logger.info(f"Workspace init")

    # SUITES
    pass

    # SECTIONS
    def add_section(self, description, suite_id, name, parent_id=None):
        section_data = {
            'description': description,
            'suite_id': suite_id,
            'parent_id': parent_id,
            'name': name
        }
        post_request(self.project.client, PostMethod().add_section(self.project.project['id']), section_data)

    # CASES
    def create_cases_for_suite(self, suite: dict, section=None, soft=True):
        for case in self.project.cases:
            # WARNING: Json file format not usability for test design
            # create_json(
            #     name=f"{case['id']}_{case['title']}",
            #     path=os.path.join(self.tms_project.cur_dir, suite['name'].strip(), section['name'].strip() if section else ''),
            #     data=case,
            #     soft=soft
            # )
            logger.debug("Start creating path")
            path = os.path.join(self.project.project_path, suite['name'].strip(), section['name'].strip() if section else '')
            logger.debug("Path is created")
            create_yaml(
                name=case['title'],
                path=path,
                data=case,
                soft=soft
            )
        logger.info(f"Cases for suite {suite['id'], suite['name']} has been created, section {section}")

    def case_base_local_create(self, soft=True):
        for suite in self.project.cases:
            if not suite:
                continue
            for case in suite:
                # WARNING: Json file format not usability for test design
                # create_json(
                #     name=f"{case['id']}_{case['title']}",
                #     path=os.path.join(self.tms_project.cur_dir, suite['name'].strip(), section['name'].strip() if section else ''),
                #     data=case,
                #     soft=soft
                # )
                logger.debug("Start creating path")
                case_name = case['title']
                section_name = get_dict_value_from_list(
                    self.project.sections[self.project.cases.index(suite)], 'id', case['section_id'], 'name'
                )
                suite_name = get_dict_value_from_list(self.project.suites, 'id', case['suite_id'], 'name')
                base_name = self.project.project_path
                path = check_path(os.path.join(base_name, suite_name, section_name))
                logger.debug("Path is created")
                create_yaml(
                    name=case_name,
                    path=path,
                    data=case,
                    soft=soft
                )
            logger.info(f"Cases for suite {suite[0]['suite_id']} has been created")

    def case_base_local_clear(self, suite=None):
        if not suite:
            path = os.path.join(self.project.project_path)
        else:
            path = os.path.join(self.project.project_path, check_name(suite))
        remove_path(path)

    def update_case(self, case_path):
        data = read_yaml(case_path)
        post_request(self.project.client, PostMethod().update_case(data['id']), data)

    def add_case(self, case_path):
        data = read_yaml(case_path)
        post_request(
            client=self.project.client,
            method=PostMethod().add_case(data['section_id'], data['title']),
            data=data
        )
        logger.info(f"Case {data['title']} has been added for section {data['section_id']}")
