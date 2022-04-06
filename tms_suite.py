import logging
import os
import shutil
from logger import create_logger

from tms_project import TMSProject
from testrail.requests import *
from file_manager import create_json, create_yaml, read_json, read_yaml
from testrail.parameters import GetCasesParameter
from testrail.cases_methods import GetMethod, PostMethod


logger = create_logger('TMSSuite')


class TMSSuite:
    def __init__(self, tms_project: TMSProject, cur_suite):
        self.tms_project = tms_project
        self.cur_suite = cur_suite
        self.sections = self.find_sections(self.cur_suite)
        assert self.tms_project, self.cur_suite

        logger.info(f"TMSSuite init with suite: {self.cur_suite['id']}{self.cur_suite['name']}")

    # SUITES
    def update_suite(self, suite: dict) -> bool:
        if self.sections:
            for section in self.sections:
                cases = self.find_cases(
                    client=self.tms_project.client,
                    project_id=self.tms_project.project['id'],
                    suite=suite,
                    section=section
                )
                for case in cases:
                    create_json(
                        name=f"{case['id']}_{case['title']}",
                        path=os.path.join(self.tms_project.cur_dir, suite['name'], section['name']),
                        data=case
                    )
                    create_yaml(
                        name=f"{case['id']}_{case['title']}",
                        path=os.path.join(self.tms_project.cur_dir, suite['name'], section['name']),
                        data=case
                    )
                print(f"Cases has been created for suite {suite['id']} with name {suite['name']}")
            return True
        else:
            # create cases without additional dirs
            cases = self.find_cases(
                client=self.tms_project.client,
                project_id=self.tms_project.project['id'],
                suite=suite,
            )
            if not cases:
                return False
            for case in cases:
                create_json(
                    name=f"{case['id']}_{case['title']}",
                    path=os.path.join(self.tms_project.cur_dir, suite['name']),
                    data=case
                )
                create_yaml(
                    name=f"{case['id']}_{case['title']}",
                    path=os.path.join(self.tms_project.cur_dir, suite['name']),
                    data=case
                )
            print(f"Cases has been created for suite {suite['id']} with name {suite['name']}")
            return True

    # SECTIONS
    def find_sections(self, suite):
        sections = get_request(
            client=self.tms_project.client,
            method=GetMethod().get_sections(
                project_id=self.tms_project.project['id'],
                suite_id=suite['id']
            )
        )
        return sections

    def find_section_by_name(self, name: str, suite: dict) -> None or dict:
        sections = self.find_sections(suite)
        if not sections:
            print(f"Not found sections for suite {suite['id']}")
            return None
        for section in sections:
            if section['name'] == name:
                print(f"Found section with name {name} for suite {suite['id']}")
                return section
        else:
            print(f"Not found any section for suite {suite['id']}")
            return None

    def add_section(self, description, suite_id, parent_id, name):
        section_data = {
            'description': description,
            'suite_id': suite_id,
            'parent_id': parent_id,
            'name': name
        }
        post_request(self.tms_project.client, PostMethod().add_section(self.tms_project.project['id']), section_data)

    # CASES
    def find_cases(self, client, project_id, suite: dict, section=None) -> dict or None:
        cases = get_request(client, GetMethod().get_cases(
            project_id,
            suite['id'],
            GetCasesParameter().create(GetCasesParameter.SECTION_ID, section['id'] if section else None)
        ))
        if cases:
            print(f"Found cases for suite {suite['id']} with name {suite['name']}")
            return cases
        else:
            print(f"Not found cases for suite {suite['id']} with name {suite['name']}")
            return None

    def case_base_update(self):
        # example for update case base method
        assert self.tms_project.suites
        for suite in self.tms_project.suites:
            self.update_suite(suite)

    def case_local_clear(self, path=None):
        try:
            if not path:
                path = os.path.join(self.tms_project.cur_dir, self.cur_suite['name'])
            for dir in os.listdir(path):
                logger.info(f"rm -r dir {path}/{dir}")
                shutil.rmtree(os.path.join(path, dir))
        finally:
            return False

    def update_case(self, case_path):
        data = read_yaml(case_path)
        post_request(self.tms_project.client, PostMethod().update_case(data['id']), data)

    def add_case(self, case_path):
        data = read_yaml(case_path)
        post_request(
            client=self.tms_project.client,
            method=PostMethod().add_case(data['section_id'], data['title']),
            data=data
        )
        print(f"Case {data['title']} has been added for section {data['section_id']}")

