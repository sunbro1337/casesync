import datetime
from testrail.testrail import *
from pprint import pprint
from file_manager import create_json
from testrail.methods_testrail import GetMethod


def auth_client(url, user, password):
    client = APIClient(url)
    client.user = user
    client.password = password
    return client


def get_request(client, method: GetMethod) -> int:
    result = client.send_get(f'{method}')
    print(type(result))
    pprint(result)
    create_json(datetime.datetime.now(), result)
    return 0
