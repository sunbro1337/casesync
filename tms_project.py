import os
import shutil

from testrail.parameters import GetCaseMoreParameter
from testrail.cases_methods import GetMethod, PostMethod
from testrail.requests import *
from file_manager import create_json, create_yaml, read_json, read_yaml


class TMSProject:
    def __init__(self, client: APIClient, client_info: dict):
        self.client = client
        self.project = self.find_project(
            client=client,
            project_name=client_info['project_name']
        )
        assert self.project

        self.suites = get_request(self.client, GetMethod().get_suites(self.project['id']))
        assert self.suites

        self.cur_dir = client_info['case_path']
        # self.cur_suite = None
        # self.cur_cases = None

    def find_project(self, client: APIClient, project_name: str) -> dict or None:
        for project in get_request(client, GetMethod().get_projects()):
            if project['name'] == project_name:
                print(f"Find project with name {project_name}: {project}")
                return project
        else:
            print(f"Not found project with name {project_name}")
            return None

    def find_suite(self, suite_name: str) -> dict or None:
        for suite in self.suites:
            if suite['name'] == suite_name:
                print(f"Find suite with name {suite_name}: {suite}")
                return suite
        else:
            print(f"Not found suite with name {suite_name}")
            return None

    def find_cases_for_suite(self, client, project_id, suite: dict) -> dict or None:
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

    def case_base_update(self):
        # example for update case base method
        assert self.suites
        for suite in self.suites:
            self.update_suite(suite)

    def update_suite(self, suite: dict) -> bool:
        cases = self.find_cases_for_suite(
            client=self.client,
            project_id=self.project['id'],
            suite=suite,
        )
        if not cases:
            return False
        for case in cases:
            create_json(
                name=f"{case['id']}_{case['title']}",
                path=os.path.join(self.cur_dir, suite['name']),
                data=case
            )
            create_yaml(
                name=f"{case['id']}_{case['title']}",
                path=os.path.join(self.cur_dir, suite['name']),
                data=case
            )
        print(f"Cases has been created for suite {suite['id']} with name {suite['name']}")
        return True

    def case_local_clear(self, path=None):
        if not path:
            path = self.cur_dir
        for dir in os.listdir(path):
            print(f"rm -r dir {path}/{dir}")
            shutil.rmtree(os.path.join(path, dir))
