from testrail.testrail import *
from pprint import pprint
from testrail.cases_methods import GetMethod, PostMethod


def auth_client(url, user, password) -> APIClient:
    """
    Authorization client function
    :param url: url of ur TestRail repo expl: https://testrail.company.net/project
    :param user: username
    :param password: password of username
    :return: client APIClient instance
    """
    client = APIClient(url)
    client.user = user
    client.password = password
    return client


def get_request(client, method: GetMethod):
    """
    Get method to TestRail, that create file.xml with responses data
    :param client: client APIClient instance
    :param method: GetMethod instance from ./cases_methods
    :return: status : int
    """
    result = client.send_get(method)
    # print('GET method result:')
    # print(type(result))
    # pprint(result)
    return result


def post_request(client, method: PostMethod, data):
    """
    Post method to TestRail
    :param client: client APIClient instance
    :param method: PostMethod instance from ./cases_methods
    :param data: The data to submit as part of the request as a dict; strings
                must be UTF-8 encoded. If adding an attachment, must be the
                path to the file.
    :return: status : int
    """
    result = client.send_post(method, data)
    # print('POST method result:')
    # print(type(result))
    # pprint(result)
    return result
