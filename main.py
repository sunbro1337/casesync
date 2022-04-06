import logging
import os.path

from file_manager import parse_template_config, read_yaml, read_json
from testrail.requests import *
from tms_project import TMSProject
from tms_suite import TMSSuite
from logger import create_logger


SUITE_NAME = "с_Mobile_sandbox"
client_info = {
    'project_name': "WOWSC",
    'project_path': "test_cases"
}
logger = create_logger('main')


if __name__ == '__main__':
    client = auth_client(
        url=parse_template_config("url"),
        user=parse_template_config("user"),
        password=parse_template_config("password")
    )

    project = TMSProject(
        client = client,
        client_info=client_info
    )
    for suite in project.suites:
        tms_suite = TMSSuite(project, suite)
        tms_suite.case_local_clear()
        # tms_suite.update_suite(suite)
    #tms_suite.update_case(os.path.join('test_cases', 'с_Mobile_sandbox', '13092365_Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt'))
    #tms_suite.add_case(os.path.join('test_cases', 'с_Mobile_sandbox', 'Lorem'))
    #tms_suite.add_section()
