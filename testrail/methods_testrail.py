from filters import GetCaseFilter


class GetMethod:
    def __init__(self):
        self.GET_CASE = "get_case"
        self.GET_CASES = "get_cases"
        self.GET_HISTORY_FOR_CASE = "get_history_for_case"

    def get_case(self, case_id=1, *_filters: GetCaseFilter):
        return f"{self.GET_CASE}/{case_id}{_filters}"

    def get_case_more(self, project_id, suite_id):
        return f"{self.GET_CASES}/{project_id}&suite_id={suite_id}"

    def get_history_for_case(self, case_id):
        return f"{self.GET_HISTORY_FOR_CASE}/{case_id}"


test = GetMethod()
result = test.get_case(var=1, GetCaseFilter.created_after(var="03.10.11"), GetCaseFilter.created_before(var="13.10.12"))

