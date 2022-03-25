import os.path
import sys
from xml.etree import ElementTree
import json
import yaml


def parse_template_config(tag):
    result = None
    template_config = "template_config.xml"
    for event, elem in ElementTree.iterparse(template_config):
        if elem.tag == tag:
            result = elem.text
            elem.clear()
    if result:
        return str(result)
    else:
        print(f"{template_config} not found")
        sys.exit()

def create_json(path, data):
    path = f"{path}.json"
    json_file = open(path, 'w', encoding="utf8")
    json.dump(data, json_file , indent=4, ensure_ascii=False)
    json_file.close()
    return path

def read_json(path):
    json_file = open(f"{path}.json", 'r', encoding="utf8")
    json_data = json.load(json_file)
    json_file.close()
    return json_data

def create_yaml(path, data):
    path = f"{path}.yml"
    yaml_file = open(path, 'w', encoding="utf8")
    yaml.dump(data, yaml_file, allow_unicode=True)
    yaml_file.close()
    return path

def read_yaml(path):
    yaml_file = open(f"{path}.yml", 'r', encoding="utf8")
    yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    yaml_file.close()
    return yaml_data
