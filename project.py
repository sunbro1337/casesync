import logging
import os.path

from testrail.testrail_requests import *
from logger import create_logger
from testrail.parameters import GetCasesParameter
from file_manager import read_json


logger = create_logger("Project", logger_lvl=logging.INFO)


class Project:
    def __init__(self, client: APIClient or bool, client_info: dict, cached=False):
        logger.debug("Start init Project")
        self.project_path = client_info['project_path']

        if client:
            self.client = client
            assert client
            self.project = self.find_project(client, client_info['project_name'].strip())
            assert self.project
        else:
            logger.warning('Project will be inited in offline mode')

        if not cached:
            self.suites = self.find_suites(self.client, self.project, client_info['mask_suite_name'])
            assert self.suites

            self.sections = [self.find_sections(suite) for suite in self.suites]
            self.cases = [self.find_cases(self.client, self.project, suite) \
                          for suite in self.suites]
        else:
            self.suites = read_json(os.path.join(client_info['cache_path'], 'suites.json'))
            self.sections = read_json(os.path.join(client_info['cache_path'], 'sections.json'))
            self.cases = read_json(os.path.join(client_info['cache_path'], 'cases.json'))
        logger.info("Project init")

    # PROJECTS
    @staticmethod
    def find_project(client: APIClient, project_name: str) -> dict or None:
        for project in get_request(client, GetMethod().get_projects()):
            if project['name'] == project_name:
                logger.info(f"Found project: {project_name}: {project}")
                return project
        else:
            logger.info(f"Not found project: {project_name}")
            return None

    # SUITES
    @staticmethod
    def find_suites(client, project, mask_name=None):
        suites = get_request(client, GetMethod().get_suites(project['id']))
        logger.debug(f"Mask name: {mask_name}")
        if mask_name:
            masked_suites = []
            for suite in suites:
                if mask_name in suite['name']:
                    masked_suites.append(suite)
            suites = masked_suites
            logger.debug(f"Masked suites {suites}")
        return suites

    def find_suite_by_name(self, suite_name: str) -> dict or None:
        for suite in self.suites:
            if suite['name'] == suite_name:
                logger.info(f"Found suite with name {suite_name}: {suite}")
                return suite
        else:
            logger.info(f"Not found suite with name {suite_name}")
            return None

    # SECTIONS
    def find_sections(self, suite):
        if not self.find_suite_by_name(suite['name']):
            logger.error(f"Not found suite: {suite}")
            return False
        sections = get_request(
            client=self.client,
            method=GetMethod().get_sections(
                project_id=self.project['id'],
                suite_id=suite['id']
            )
        )
        logger.info(f"Section for suite {suite['id'], suite['name']} has been found")
        return sections

    # CASES
    @staticmethod
    def find_cases(client, project: dict, suite: dict, section=None) -> dict or None:
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
