from .parameters import GetCaseMoreParameter


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
        self.GET_CASE = "get_case"
        self.GET_CASES = "get_cases"
        self.GET_HISTORY_FOR_CASE = "get_history_for_case"

    def get_case(self, case_id: int):
        return f"{self.GET_CASE}/{case_id}"

    def get_case_more(self, project_id: int, suite_id: int, *parameters: GetCaseMoreParameter):
        if parameters:
            return f"{self.GET_CASES}/{project_id}&suite_id={suite_id}{self.create_query_str(parameters)}"
        else:
            return f"{self.GET_CASES}/{project_id}&suite_id={suite_id}"

    def get_history_for_case(self, case_id, *parameters):
        if parameters:
            return f"{self.GET_HISTORY_FOR_CASE}/{case_id}{self.create_query_str(parameters)}"
        else:
            return f"{self.GET_HISTORY_FOR_CASE}/{case_id}"


class PostMethod(Method):
    def __init__(self):
        self.ADD_CASE = "add_case"
        self.COPY_CASES_TO_SELECTION = "copy_cases_to_section"
        self.UPDATE_CASE = "update_case"
        self.UPDATE_CASES = "update_cases"
        self.MOVE_CASE_TO_SECTION = "move_cases_to_section"
        self.DELETE_CASE = "delete_case"
        self.DELETE_CASES = "delete_cases"

    def add_case(self, section_id: int, title: str):
        return f"{self.ADD_CASE}/{section_id}&title={title}"

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

    def delete_case_more(self, project_id, suite_id, soft=None):
        if soft:
            return f"{self.DELETE_CASES}/{project_id}&{suite_id}&soft=1"
        else:
            return f"{self.DELETE_CASES}/{project_id}&{suite_id}"


# Examples
#result = GetMethod().get_case_more(
#    1,
#    2,
#    GetCaseMoreParameter.create(GetCaseMoreParameter.CREATED_AFTER, "02"),
#    GetCaseMoreParameter.create(GetCaseMoreParameter.CREATED_BEFORE, "02")
#)
#
#print(result)
