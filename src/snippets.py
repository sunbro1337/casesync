import logging
import os.path

from file_manager import parse_template_config
from testrail.testrail_requests import *
from project import Project
from workspace import Workspace
from logger import create_logger
from file_manager import read_yaml


CLIENT_CONFIG_PATH = os.path.join('..', 'configs', 'client_config.yaml')
CLIENT_CONFIG_DICT = read_yaml(CLIENT_CONFIG_PATH)
logger = create_logger('main')


if __name__ == '__main__':
    client = auth_client(
        url=CLIENT_CONFIG_DICT['testrail']['url'],
        user=CLIENT_CONFIG_DICT['testrail']['username'],
        password=CLIENT_CONFIG_DICT['testrail']['apikey'],
    )

    logger.info("Start")
    project = Project(
        client = client,
        client_info=CLIENT_CONFIG_DICT['client_info'],
        cached=False
    )
    workspace = Workspace(project)
    workspace.case_base_local_clear()
    workspace.case_base_local_create(soft=False)
    logger.info("Finish")
