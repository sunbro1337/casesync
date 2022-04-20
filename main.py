import logging
import os.path

from file_manager import parse_template_config
from testrail.testrail_requests import *
from project import Project
from workspace import Workspace
from logger import create_logger


SUITE_NAME = "[Mobile: Render]"
client_info = {
    'project_name': "WOWSC",
    'project_path': "test_cases",
    'mask_suite_name': None,
    'cache_path': 'cache'
}
logger = create_logger('main')


if __name__ == '__main__':
    client = auth_client(
        url=parse_template_config("url"),
        user=parse_template_config("user"),
        password=parse_template_config("password")
    )

    logger.info("Start")
    project = Project(
        client = client,
        client_info=client_info,
        cached=True
    )
    workspace = Workspace(project)
    # workspace.case_base_local_clear()
    # workspace.case_base_local_create(soft=True)
    workspace.add_section(
        description='',
        suite_id=project.find_suite_by_name(SUITE_NAME)['id'],
        name='3D-UI'
    )
    logger.info("Finish")
