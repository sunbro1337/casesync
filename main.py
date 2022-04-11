import logging
import os.path

from file_manager import parse_template_config, read_yaml, read_json
from testrail.requests import *
from tms_project import TMSProject
from tms_suite import TMSSuites
from logger import create_logger


SUITE_NAME = "с_Mobile_sandbox"
client_info = {
    'project_name': "WOWSC",
    'project_path': "test_cases",
    'mask_suite_name': None
}
logger = create_logger('main')


if __name__ == '__main__':
    client = auth_client(
        url=parse_template_config("url"),
        user=parse_template_config("user"),
        password=parse_template_config("password")
    )

    tms_project = TMSProject(
        client = client,
        client_info=client_info
    )
    logger.info("Start")
    tms_suite = TMSSuites(tms_project)
    logger.info("Finish")

"""
1 without case_base_local_clear
2022-04-08 17:46:08,942 - main - INFO - Start
2022-04-08 17:47:12,348 - main - INFO - Finish

2 with case_base_local_clear
2022-04-08 17:49:04,579 - main - INFO - Start
2022-04-08 17:50:09,239 - main - INFO - Finish
"""
