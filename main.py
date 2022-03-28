import os.path
import sys

from file_manager import parse_template_config

from testrail.requests import *
from testrail.parameters import GetCaseMoreParameter
from testrail.cases_methods import GetMethod, PostMethod
from file_manager import create_json, create_yaml, read_json, read_yaml


PROJECT_NAME = "WOWSC"
SUITE_NAME = "[Mobile: Render]"
CASE_PATH = "test_cases"


def find_project(client: APIClient, project_name: str) -> dict or None:
    for project in get_request(client, GetMethod().get_projects()):
        if project['name'] == project_name:
            print(f"Find project with name {project_name}: {project}")
            return project
    else:
        print(f"Not found project with name {project_name}")
        return None


def find_suite(client: APIClient, project_id: int, suite_name: str) -> dict or None:
    for suite in get_request(client, GetMethod().get_suites(project_id)):
        if suite['name'] == suite_name:
            print(f"Find suite with name {suite_name}: {suite}")
            return suite
    else:
        print(f"Not found suite with name {suite_name}")
        return None

def find_cases_for_suite(client, project_id, suite: dict):
    cases = get_request(client, GetMethod().get_cases(
        project_id=project_id,
        suite_id=suite['id']
    ))
    if cases:
        print(f"Found cases for suite {suite['id']} with name {suite['name']}")
        return cases
    else:
        print(f"Not found cases for suite {suite['id']} with name {suite['name']}")
        return None


if __name__ == '__main__':
    client = auth_client(
        url=parse_template_config("url"),
        user=parse_template_config("user"),
        password=parse_template_config("password")
    )

    # find project
    project = find_project(
        client=client,
        project_name=PROJECT_NAME
    )
    assert project

# example for update case base method
    for suite in get_request(client, GetMethod().get_suites(project['id'])):

        #suite = find_suite(
        #    client=client,
        #    project_id=project['id'],
        #    suite_name=SUITE_NAME
        #)
        #assert suite

        cases = find_cases_for_suite(
            client=client,
            project_id=project['id'],
            suite=suite,
        )

        if not cases:
            continue

        for case in cases:
            create_json(
                name=f"{case['id']}_{case['title']}",
                path=os.path.join(CASE_PATH, suite['name']),
                data=case
            )
            create_yaml(
                name=f"{case['id']}_{case['title']}",
                path=os.path.join(CASE_PATH, suite['name']),
                data=case
            )
        print(f"Cases has been created for suite {suite['id']} with name {suite['name']}")
