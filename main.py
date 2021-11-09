from file_manager import parse_template_config

from testrail.requests import *
from testrail.parameters import GetCaseMoreParameter
from testrail.cases_methods import GetMethod, PostMethod


WOWSC_PROJECT_ID = 21


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
