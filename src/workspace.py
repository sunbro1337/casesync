import logging
import os

from logger import create_logger
from project import Project
from testrail.testrail_requests import *
from file_manager import create_yaml, read_yaml, check_path, check_name, remove_path, get_dict_value_from_list
from testrail.cases_methods import GetMethod, PostMethod


logger = create_logger('Workspace', logger_lvl=logging.INFO)


class Workspace:
    def __init__(self, project: Project):
        logger.debug("Start init Workspace")
        self.project = project
        assert self.project
        if not self.project.client:
            self.project_name = ''
        else:
            self.project_name = self.project.project['name']
        logger.info(f"Workspace init")

    # SUITES
    def add_suite(self, name, description):
        suite_data = {
            'name': name,
            'description': description,
        }
        post_request(
            client=self.project.client,
            method=PostMethod().add_suite(self.project.project['id']),
            data=suite_data
        )

    # SECTIONS
    def add_section(self, description, suite_id, name, parent_id=None):
        section_data = {
            'description': description,
            'suite_id': suite_id,
            'parent_id': parent_id,
            'name': name
        }
        post_request(
            client=self.project.client,
            method=PostMethod().add_section(self.project.project['id']),
            data= section_data
        )

    # CASES
    def create_cases_for_suite(self, suite: dict, section=None, soft=True):
        for case in self.project.cases:
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
        base_name = os.path.join(self.project.project_path, self.project_name)
        section = None
        suite_name = None
        for suite in self.project.sections:
            if not suite:
                continue
            for section in suite:
                if not section:
                    continue
                suite_name = get_dict_value_from_list(self.project.suites, 'id', section['suite_id'], 'name')
                parent_id = get_dict_value_from_list(suite, 'id', section['parent_id'], 'id')
                parent_dirs = []
                while parent_id:
                    parent_section_name = get_dict_value_from_list(suite, 'id', parent_id, 'name')
                    parent_dirs.insert(0, parent_section_name)
                    parent_id = get_dict_value_from_list(suite, 'id', parent_id, 'parent_id')
                parent_path = ''
                if len(parent_dirs) != 0:
                    for i in parent_dirs:
                        parent_path = os.path.join(parent_path, i)
                section_path = os.path.join(base_name, suite_name, parent_path, section['name'])
                section_path = check_path(section_path)
                for case_list in self.project.cases:
                    if not case_list:
                        continue
                    for case in case_list:
                        if case['suite_id'] != section['suite_id']:
                            continue
                        if case['section_id'] != section['id']:
                            continue
                        create_yaml(
                            name=case['title'],
                            path=section_path,
                            data=case,
                            soft=soft
                        )
            if suite and section:
                logger.info(f"Cases for suite {suite_name, section['suite_id']} has been created")
            else:
                logger.info(f"Error in suite creating")

    def case_base_local_clear(self, suite=None):
        if not suite:
            path = os.path.join(self.project.project_path, self.project_name)
        else:
            path = os.path.join(self.project.project_path, self.project_name, check_name(suite))
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
