import logging

from testrail.requests import *
from logger import create_logger


logger = create_logger("TMSProject", logger_lvl=logging.WARNING)


class TMSProject:
    def __init__(self, client: APIClient, client_info: dict):
        self.client = client
        assert client

        self.project = self.find_project(
            client=client,
            project_name=client_info['project_name'].strip()
        )
        assert self.project

        self.suites = self.find_suites(self.client, self.project, client_info['mask_suite_name'])
        assert self.suites

        self.cur_dir = client_info['project_path'].strip()
        assert self.cur_dir

    # PROJECTS
    def find_project(self, client: APIClient, project_name: str) -> dict or None:
        for project in get_request(client, GetMethod().get_projects()):
            if project['name'] == project_name:
                logger.info(f"Found project: {project_name}: {project}")
                return project
        else:
            logger.info(f"Not found project: {project_name}")
            return None

    # SUITES
    def find_suites(self, client, project, mask_name=None):
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
