from testrail.testrail import *
from pprint import pprint
from file_manager import create_json
from testrail.cases_methods import GetMethod, PostMethod


def auth_client(url, user, password):
    client = APIClient(url)
    client.user = user
    client.password = password
    return client


def get_request(client, method: GetMethod) -> int:
    result = client.send_get(method)
    print(type(result))
    pprint(result)
    # create_json(datetime.datetime.now(), result)
    return 0


def post_request(client, method: PostMethod, data) -> int:
    result = client.send_post(method, data)
    print(type(result))
    pprint(result)
    return 0
