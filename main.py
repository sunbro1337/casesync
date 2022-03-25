from file_manager import parse_template_config

from testrail.requests import *
from testrail.parameters import GetCaseMoreParameter
from testrail.cases_methods import GetMethod, PostMethod
from file_manager import create_json, create_yaml, read_json, read_yaml


WOWSC_PROJECT_ID = 21


if __name__ == '__main__':
    client = auth_client(
        url=parse_template_config("url"),
        user=parse_template_config("user"),
        password=parse_template_config("password")
    )

    data = get_request(
        client=client,
        method=GetMethod().get_case(12486969)
    )

    # get_request(
    #     client=client,
    #     method=GetMethod().get_case_more(
    #         WOWSC_PROJECT_ID,
    #         13316,
    #         GetCaseMoreParameter.create(GetCaseMoreParameter.LIMIT, 2)
    #     )
    # )
    template_case = "template/template_case"
    path_to_case = f"test_cases/{data['id']}"

    #create_json(path_to_case, data)
    #print("Json data:")
    #pprint(read_json(path_to_case))

    #create_yaml(path_to_case, data)
    #print("Yaml data:")
    #pprint(read_yaml(path_to_case))

    pprint(read_json(template_case))
    create_json(f"{template_case}1", read_json(template_case))
    pprint(read_yaml(template_case))
    create_yaml(f"{template_case}1", read_yaml(template_case))

