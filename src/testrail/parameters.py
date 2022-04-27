class Parameter:
    @staticmethod
    def create(parameter, var):
        """
        Create a parameter for child classes
        :param parameter: parameter of child class
        :param var: variable for parameter
        :return: format query string parameter : str
        """
        return f"&{parameter}={var}"


# Parameters for GET method
class GetCasesParameter(Parameter):
    CREATED_AFTER = "created_after"
    CREATED_BEFORE = "created_before"
    CREATED_BY = "created_by"
    FILTER = "filter"
    LIMIT = "limit"
    MILESTONE_ID = "milestone_id"
    OFFSET = "offset"
    PRIORITY_ID = "priority_id"
    REFS = "refs"
    SECTION_ID = "section_id"
    TEMPLATE_ID = "template_id"
    TYPE_ID = "type_id"
    UPDATED_AFTER = "updated_after"
    UPDATED_BEFORE = "updated_before"
    UPDATED_BY = "updated_by"


class GetHistoryForCaseParameter(Parameter):
    LIMIT = "limit"
    OFFSET = "offset"


# Parameters for POST method
class PostAddCaseParameter(Parameter):
    TEMPLATE_ID = "template_id"
    TYPE_ID = "type_id"
    PRIORITY_ID = "priority_id"
    ESTIMATE = "estimate"
    MILESTONE_ID = "milestone_id"
    REFS = "refs"
