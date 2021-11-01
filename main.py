from testrail.methods_testrail import GetMethod
import tesrail_test

if __name__ == '__main__':
    client = tesrail_test.auth_client(
        url='',
        user='',
        password=''
    )
    tesrail_test.get_request(
        client,
        method=GetMethod.GET_CASE,
        case_id='10640173'
    )
