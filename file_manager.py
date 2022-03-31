import os.path
import re
import sys
from xml.etree import ElementTree
import json
import yaml

from configs.settings import *


def parse_template_config(tag):
    result = None
    template_config = os.path.join('configs', "template_config.xml")
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
    path = re.sub(MASKS_FOR_DIRS, '', path) # WARNING replaces / char
    if not os.path.exists(path):
        os.mkdir(path)
    return path

def create_json(name: str, path: str, data: dict) -> str:
    path = os.path.join(check_path(path), check_name(name))
    json_file = open(f"{path}.json", 'w', encoding="utf8")
    json.dump(data, json_file , indent=4, ensure_ascii=False)
    json_file.close()
    return path

def read_json(path: str):
    json_file = open(f"{path}.json", 'r', encoding="utf8")
    json_data = json.load(json_file)
    json_file.close()
    return json_data

def create_yaml(name: str, path: str, data: dict) -> str:
    path = os.path.join(check_path(path), check_name(name))
    yaml_file = open(f"{path}.yml", 'w', encoding="utf8")
    yaml.dump(data, yaml_file, allow_unicode=True)
    yaml_file.close()
    return path

def read_yaml(path: str):
    yaml_file = open(f"{path}.yml", 'r', encoding="utf8")
    yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    yaml_file.close()
    return yaml_data
