import argparse
import logging
import os
import sys

cur_path=os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/..")

from src.logger import create_logger
from src.file_manager import read_json, read_yaml
from configs.settings import diff_file_name
from src.project import Project
from src.workspace import Workspace
from src.testrail.testrail_requests import *


# To install python libs on powershell: py -3.10 -m pip install package_name

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--url")
arg_parser.add_argument("--usr")
arg_parser.add_argument("--apikey")
args = arg_parser.parse_args()

logger = create_logger(
    name='build',
    logger_lvl=logging.DEBUG,
    handler_lvl=logging.DEBUG,
)

CLIENT_CONFIG_PATH = os.path.join('configs', 'client_config.yaml')
diff_data_path = os.path.join(diff_file_name)
CLIENT_CONFIG_DICT = read_yaml(CLIENT_CONFIG_PATH)
logger.debug(f"CLIENT_CONFIG_PATH: {CLIENT_CONFIG_PATH}")
logger.debug(f"diff_data_path: {diff_data_path}")
logger.debug(f"CLIENT_CONFIG_DICT: {CLIENT_CONFIG_DICT}")

logger.debug(f"CWD: {os.getcwd()}")

diff_data = read_json(diff_data_path)
logger.debug(f"Diff data: {diff_data}")
if not diff_data:
    print("Diff in None")
    sys.exit()

logger.info("Start auth gitlab client on testrail")
# client = auth_client(
#     url=CLIENT_CONFIG_DICT['testrail']['url'],
#     user=CLIENT_CONFIG_DICT['testrail']['username'] + "@wargaming.net",
#     password=CLIENT_CONFIG_DICT['testrail']['apikey'],
# )
client = auth_client(
    url=args.url,
    user=args.usr,
    password=args.apikey,
)
assert client
logger.info("Auth is completed")

logger.info("Getting info about project")
project = Project(
    client=client,
    client_info=CLIENT_CONFIG_DICT['client_info'],
    cached=False
)
logger.info("Getting project info is completed")

logger.info("Creating workspace...")
workspace = Workspace(project)
logger.info('Workspace is created')

logger.info("Start pushing changes on testrail")
for i in diff_data:
    case_path = diff_data[i]
    if os.path.isfile(case_path) and '.yml' in case_path:
        logger.info(f"Pushing changes from {case_path}...")
        response = workspace.update_case(case_path)
        logger.info(f"Testrail response: {response if response else 'success'}")
        logger.info("Success")
    else:
        logger.warning(f"File {case_path} has been skipped: incorrect format")
logger.info("Pushing changes is completed")
