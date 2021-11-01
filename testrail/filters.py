class GetCaseFilter:
    def __init__(self):
        self.CREATED_AFTER = f"&created_after="
        self.CREATED_BEFORE = f"&created_before="

    def created_after(self, var):
        return f"{self.CREATED_AFTER}{var}"

    def created_before(self, var):
        return f"{self.CREATED_BEFORE}{var}"
