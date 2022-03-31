from file_manager import parse_template_config
from testrail.requests import *
from tms_project import TMSProject


SUITE_NAME = "с_Mobile_sandbox"
client_info = {
    'project_name': "WOWSC",
    'case_path': "test_cases"
}


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
    project.case_local_clear()
    project.update_suite(project.find_suite(SUITE_NAME))
