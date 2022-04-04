from .parameters import GetCasesParameter, PostAddCaseParameter


class Method:
    @staticmethod
    def create_query_str(parameters):
        """
        Create a query string for child class method
        :param parameters: number of parameters for query string from ./parameters.py
        :return: query string : str
        """
        query_str = ''
        for i in parameters:
            query_str = query_str + str(i)
        return query_str


class GetMethod(Method):
    def __init__(self):
        # api/reference/cases/
        self.GET_CASE = "get_case"
        self.GET_CASES = "get_cases"
        self.GET_HISTORY_FOR_CASE = "get_history_for_case"
        # api/reference/projects/
        self.GET_PROJECT = "get_project"
        self.GET_PROJECTS = "get_projects"
        # api/reference/suites/
        self.GET_SUITE = "get_suite"
        self.GET_SUITES = "get_suites"
        # api/reference/sections/
        self.GET_SECTION = "get_section"
        self.GET_SECTIONS = "get_sections"

    # api/reference/cases/
    def get_case(self, case_id: int):
        return f"{self.GET_CASE}/{case_id}"

    def get_cases(self, project_id: int, suite_id: int, *parameters: GetCasesParameter):
        return \
            f"{self.GET_CASES}/{project_id}&suite_id={suite_id}{self.create_query_str(parameters) if parameters else ''}"

    def get_history_for_case(self, case_id, *parameters):
        return f"{self.GET_HISTORY_FOR_CASE}/{case_id}{self.create_query_str(parameters) if parameters else ''}"

    # api/reference/projects/
    def get_project(self, project_id):
        return f"{self.GET_PROJECT}/{project_id}"

    def get_projects(self):
        return f"{self.GET_PROJECTS}"

    # api/reference/suites/
    def get_suite(self, suite_id):
        return f"{self.GET_SUITE}/{suite_id}"

    def get_suites(self, project_id):
        return f"{self.GET_SUITES}/{project_id}"

    # api/reference/sections/
    def get_section(self, section_id):
        return f"{self.GET_SECTION}/{section_id}"

    def get_sections(self, project_id, suite_id):
        # The ID of the test suite (optional if the project is operating in single suite mode). Now it's required.
        return f"{self.GET_SECTIONS}/{project_id}&suite_id={suite_id}"



class PostMethod(Method):
    def __init__(self):
        # api/reference/cases/
        self.ADD_CASE = "add_case"
        self.COPY_CASES_TO_SELECTION = "copy_cases_to_section"
        self.UPDATE_CASE = "update_case"
        self.UPDATE_CASES = "update_cases"
        self.MOVE_CASE_TO_SECTION = "move_cases_to_section"
        self.DELETE_CASE = "delete_case"
        self.DELETE_CASES = "delete_cases"
        # api/reference/suites/
        self.ADD_SUITE = "add_suite"
        self.UPDATE_SUITE = "update_suite"
        self.DELETE_SUITE = "delete_suite"
        # api/reference/sections/
        self.ADD_SECTION = "add_section"
        self.UPDATE_SECTION = "update_section"
        self.DELETE_SECTION = "delete_section"

    # api/reference/cases/
    def add_case(self, section_id: int, title: str, *parameters: PostAddCaseParameter):
        return f"{self.ADD_CASE}/{section_id}&title={title}{self.create_query_str(parameters) if parameters else ''}"

    def copy_cases_to_section(self, section_id: int):
        return f"{self.COPY_CASES_TO_SELECTION}/{section_id}"

    def update_case(self, case_id: int):
        return f"{self.UPDATE_CASE}/{case_id}"

    def update_more_case(self, suite_id: int):
        return f"{self.UPDATE_CASES}/{suite_id}"

    def move_cases_to_section(self, section_id=None, suite_id=None):
        if section_id:
            return f"{self.MOVE_CASE_TO_SECTION}/{section_id}"
        elif suite_id:
            return f"{self.MOVE_CASE_TO_SECTION}/{suite_id}"

    def delete_case(self, case_id):
        return f"{self.DELETE_CASE}/{case_id}"

    def delete_cases(self, project_id, suite_id, soft=False):
        return f"{self.DELETE_CASES}/{project_id}&suite_id={suite_id}{'&soft=1' if soft else ''}"

    # api/reference/suites/
    def add_suite(self, project_id):
        return f"{self.ADD_SUITE}/{project_id}"

    def update_suite(self, suite_id):
        return f"{self.ADD_SUITE}/{suite_id}"

    # api/reference/sections/
    def add_section(self, project_id):
        return f"{self.ADD_SECTION}/{project_id}"

    def update_section(self, section_id):
        return f"{self.UPDATE_SECTION}/{section_id}"

    def delete_section(self, section_id, soft=False):
        return f"{self.DELETE_SECTION}/{section_id}{'&soft=1' if soft else ''}"

# Examples
# result = GetMethod().get_cases(
#     1,
#     2,
#     GetCasesParameter.create(GetCasesParameter.CREATED_AFTER, "02"),
#     GetCasesParameter.create(GetCasesParameter.CREATED_BEFORE, "02")
# )
#
# print(result)
