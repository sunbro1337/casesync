from testrail.requests import *


class TMSProject:
    def __init__(self, client: APIClient, client_info: dict):
        self.client = client
        assert client

        self.project = self.find_project(
            client=client,
            project_name=client_info['project_name']
        )
        assert self.project

        self.suites = get_request(self.client, GetMethod().get_suites(self.project['id']))
        assert self.suites

        self.cur_dir = client_info['project_path']
        assert self.cur_dir

    # PROJECTS
    def find_project(self, client: APIClient, project_name: str) -> dict or None:
        for project in get_request(client, GetMethod().get_projects()):
            if project['name'] == project_name:
                print(f"Find project with name {project_name}: {project}")
                return project
        else:
            print(f"Not found project with name {project_name}")
            return None

    # SUITES
    def find_suite_by_name(self, suite_name: str) -> dict or None:
        for suite in self.suites:
            if suite['name'] == suite_name:
                print(f"Find suite with name {suite_name}: {suite}")
                return suite
        else:
            print(f"Not found suite with name {suite_name}")
            return None
