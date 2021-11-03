class GetCaseFilter:
    def __init__(self):
        self.CREATED_AFTER = "&created_after="
        self.CREATED_BEFORE = "&created_before="
        self.LIMIT = "&limit="
        self.OFFSET = "&offset="

    @staticmethod
    def create(_filter, var):
        return f"{_filter}{var}"
