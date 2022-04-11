import logging
import os
import shutil
from logger import create_logger

from tms_project import TMSProject
from testrail.requests import *
from file_manager import create_json, create_yaml, read_json, read_yaml, check_path, check_name, remove_path, check_crc
from testrail.parameters import GetCasesParameter
from testrail.cases_methods import GetMethod, PostMethod


logger = create_logger('TMSSuite', logger_lvl=logging.DEBUG)


class TMSSuites:
    def __init__(self, tms_project: TMSProject, cur_suite=None):
        logger.debug("Start init TMSSuites")
        self.tms_project = tms_project
        assert self.tms_project
        self.cur_suite = cur_suite
        self.sections = [self.find_sections(suite) for suite in self.tms_project.suites]
        self.cases = [self.find_cases(tms_project.client, tms_project.project, suite) \
                      for suite in self.tms_project.suites]
        logger.info(f"TMSSuite init with suite: {self.cur_suite}")

    # SUITES
    def download_suite(self, suite=None, soft=True) -> bool:
        # Hard download suite, TODO soft download
        if not suite:
            suite = self.cur_suite
        sections = self.find_sections(suite)
        if sections:
            for section in sections:
                self.create_cases_for_suite(suite, section, soft=soft)
        else:
            self.create_cases_for_suite(suite, soft=soft)
        logger.info(f"Suite: {suite['id'], suite['name']} has been updated")
        return True

    # SECTIONS
    def find_sections(self, suite):
        if not self.tms_project.find_suite_by_name(suite['name']):
            logger.error(f"Not found suite: {suite}")
            return False
        sections = get_request(
            client=self.tms_project.client,
            method=GetMethod().get_sections(
                project_id=self.tms_project.project['id'],
                suite_id=suite['id']
            )
        )
        logger.info(f"Section for suite {suite['id'], suite['name']} has been found")
        return sections

    def add_section(self, description, suite_id, parent_id, name):
        section_data = {
            'description': description,
            'suite_id': suite_id,
            'parent_id': parent_id,
            'name': name
        }
        post_request(self.tms_project.client, PostMethod().add_section(self.tms_project.project['id']), section_data)

    # CASES
    def find_cases(self, client, project: dict, suite: dict, section=None) -> dict or None:
        cases = get_request(client, GetMethod().get_cases(
            project['id'],
            suite['id'],
            GetCasesParameter().create(GetCasesParameter.SECTION_ID, section['id'] if section else '')
        ))
        if cases:
            logger.info(f"Found cases for suite: {suite['id'], suite['name']}")
            return cases
        else:
            logger.info(f"Not found cases for suite {suite['id'], suite['name']}")
            return None

    def create_cases_for_suite(self, suite: dict, section=None, soft=True):
        for case in self.cases:
            # WARNING: Json file format not usability for test design
            # create_json(
            #     name=f"{case['id']}_{case['title']}",
            #     path=os.path.join(self.tms_project.cur_dir, suite['name'].strip(), section['name'].strip() if section else ''),
            #     data=case,
            #     soft=soft
            # )
            logger.debug("Start creating path")
            path = os.path.join(self.tms_project.cur_dir, suite['name'].strip(), section['name'].strip() if section else '')
            logger.debug("Path is created")
            create_yaml(
                name=f"{case['id']}_{case['title']}",
                path=path,
                data=case,
                soft=soft
            )
        logger.info(f"Cases for suite {suite['id'], suite['name']} has been created, section {section}")

    def case_base_local_download(self, soft=True):
        # Hard download, TODO soft download
        for suite in self.tms_project.suites:
            self.download_suite(suite, soft=soft)

    def case_base_local_clear(self, suite=None):
        if not suite:
            path = os.path.join(self.tms_project.cur_dir)
        else:
            path = os.path.join(self.tms_project.cur_dir, check_name(self.cur_suite['name']))
        remove_path(path)

    def update_case(self, case_path):
        data = read_yaml(case_path)
        post_request(self.tms_project.client, PostMethod().update_case(data['id']), data)

    def add_case(self, case_path):
        data = read_yaml(case_path)
        post_request(
            client=self.tms_project.client,
            method=PostMethod().add_case(data['section_id'], data['title']),
            data=data
        )
        logger.info(f"Case {data['title']} has been added for section {data['section_id']}")
