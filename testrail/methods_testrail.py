from filters import GetCaseFilter


class GetMethod:
    def __init__(self):
        self.GET_CASE = "get_case"
        self.GET_CASES = "get_cases"
        self.GET_HISTORY_FOR_CASE = "get_history_for_case"

    def get_case(self, case_id=1, *_filters: GetCaseFilter):
        _filters_str = ''
        if _filters:
            for i in _filters:
                _filters_str = _filters_str + str(i)
        return f"{self.GET_CASE}/{case_id}{_filters_str}"

    def get_case_more(self, project_id, suite_id):
        return f"{self.GET_CASES}/{project_id}&suite_id={suite_id}"

    def get_history_for_case(self, case_id):
        return f"{self.GET_HISTORY_FOR_CASE}/{case_id}"


get_method = GetMethod()
get_case_filter = GetCaseFilter()
print(get_method.get_case(1, get_case_filter.created_after("01"), get_case_filter.created_before("02")))
