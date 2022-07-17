import logging
import os.path
import re
import shutil
import sys
from xml.etree import ElementTree
import json
import yaml

from configs.settings import *
from .logger import create_logger


logger = create_logger('file_manager', logger_lvl=logging.WARNING)


def parse_template_config(tag):
    result = None
    template_config = os.path.join('../configs', "template_config.xml")
    for event, elem in ElementTree.iterparse(template_config):
        if elem.tag == tag:
            result = elem.text
            elem.clear()
    if result:
        return str(result)
    else:
        print(f"{template_config} not found")
        sys.exit()

def check_name(name):
    if len(name) > LEN_FOR_NAMES:
        name = name[:LEN_FOR_NAMES]
    name = name.strip()
    return re.sub(MASKS_FOR_NAMES, '', name)

def check_path(path: str) -> str:
    logger.debug(f"Checking path '{path}'")
    split_char = '/'
    if sys.platform == 'win32':
        split_char = '\\'
    path = re.sub(MASKS_FOR_DIRS, '', path) # WARNING replaces / char
    for dir in path.split(split_char):
        path = path.replace(dir, dir.strip())
    if not os.path.exists(path):
        logger.debug(f"Path {path} not found")
        os.makedirs(path)
        logger.debug(f"Path {path} has ben created")
    logger.debug(f"Path '{path}' has been checked")
    return path

def calculate_crc(dict):
    return lambda x,y : x^y, [hash(repr(item)) for item in dict.items()]

def check_crc(dict_1, dict_2):
    if calculate_crc(dict_1) == calculate_crc(dict_2):
        return True
    else:
        return False

def remove_path(path):
    logger.info(f"Path for rmdir {path}")
    try:
        shutil.rmtree(path)
        logger.info(f"Dir {path} has been removed")
        return True
    except FileNotFoundError:
        logger.info(f"Not found path for rmdir {path}")
        return False

def create_json(name: str, path: str, data: dict, soft=True) -> str or bool:
    logger.debug(f"Start creating {path, name}")
    path = os.path.join(path, f"{check_name(name)}.json")
    if os.path.exists(path) and soft:
        logger.debug(f"Skip create {path} already exist")
        return False
    json_file = open(f"{path}", 'w', encoding="utf8")
    json.dump(data, json_file , indent=4, ensure_ascii=False)
    json_file.close()
    logger.debug(f"File {path} created")
    return path

def read_json(path: str):
    json_file = open(f"{path}", 'r', encoding="utf8")
    json_data = json.load(json_file)
    json_file.close()
    return json_data

def create_yaml(name: str, path: str, data: dict, soft=True) -> str or bool:
    logger.debug(f"Start creating {path, name}")
    path = os.path.join(path,  f"{check_name(name)}.yml")
    if os.path.exists(path) and soft:
        logger.debug(f"Skip create {path} already exist")
        return False
    yaml_file = open(f"{path}", 'w', encoding="utf8")
    yaml.dump(data, yaml_file, allow_unicode=True)
    yaml_file.close()
    logger.debug(f"File {path} created")
    return path

def read_yaml(path: str):
    yaml_file = open(f"{path}", 'r', encoding="utf8")
    yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    yaml_file.close()
    return yaml_data

def get_dict_value_from_list(list: list, key: str, value, returned_key: str) -> dict or None:
    for dict in list:
        if dict[key] == value:
            return dict[returned_key]
    else:
        return None

def collect_yaml_data(path: str, data_types: list) -> dict:
    yaml_data = read_yaml(os.path.join(path))
    result_data = {}
    for key in yaml_data.keys():
        for i in data_types:
            if key == i:
                result_data[key] = yaml_data[key]
    return result_data
