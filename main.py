import logging
import os.path

from file_manager import parse_template_config
from testrail.requests import *
from project import Project
from workspace import Workspace
from logger import create_logger


SUITE_NAME = "с_Mobile_sandbox"
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

    project = Project(
        client = client,
        client_info=client_info,
        cached=True
    )
    logger.info("Start")
    workspace = Workspace(project)
    workspace.case_base_local_create(soft=False)
    logger.info("Finish")

"""
1 without case_base_local_clear
2022-04-08 17:46:08,942 - main - INFO - Start
2022-04-08 17:47:12,348 - main - INFO - Finish

2 with case_base_local_clear
2022-04-08 17:49:04,579 - main - INFO - Start
2022-04-08 17:50:09,239 - main - INFO - Finish
"""
