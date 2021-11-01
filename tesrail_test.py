from testrail.testrail import *
from pprint import pprint
from file_manager import create_json
from testrail.methods_testrail import GetMethod


def auth_client(url, user, password):
    client = APIClient(url)
    client.user = user
    client.password = password
    return client


def get_request(client, method: GetMethod, case_id='') -> int:
    case = client.send_get(f'{method}/{case_id}')
    print(type(case))
    pprint(case)
    create_json("case_1", case)
    return 0
