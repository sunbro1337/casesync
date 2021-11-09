import sys
from xml.etree import ElementTree

from testrail.requests import *
from testrail.parameters import GetCaseMoreParameter
from testrail.cases_methods import GetMethod, PostMethod


WOWSC_PROJECT_ID = 21


def parse_template_config(tag):
    result = None
    for event, elem in ElementTree.iterparse("template_config.xml"):
        if elem.tag == tag:
            result = elem.text
            elem.clear()
    if result:
        return str(result)
    else:
        print("Not found")
        sys.exit()


if __name__ == '__main__':
    client = auth_client(
        url=parse_template_config("url"),
        user=parse_template_config("user"),
        password=parse_template_config("password")
    )

    get_request(
        client=client,
        method=GetMethod().get_case(6611042)
    )

    get_request(
        client=client,
        method=GetMethod().get_case_more(
            WOWSC_PROJECT_ID,
            13316,
            GetCaseMoreParameter.create(GetCaseMoreParameter.LIMIT, 2)
        )
    )
