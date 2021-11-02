from testrail.methods_testrail import GetMethod
from testrail.filters import GetCaseFilter
import tesrail_test

if __name__ == '__main__':
    client = tesrail_test.auth_client(
        url='',
        user='',
        password=''
    )
    tesrail_test.get_request(
        client,
        method=GetMethod().get_case_more(1, 2,
                                         GetCaseFilter().created_after("01"),
                                         GetCaseFilter().created_before("02"))
    )
