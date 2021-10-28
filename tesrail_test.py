from testrail.testrail import *
from pprint import pprint


def get_case_request(client_url, client_user, client_password, case_id):
    client = APIClient(client_url)
    client.user = client_user
    client.password = client_password
    case = client.send_get(f'get_case/{case_id}')
    pprint(case)
