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
    json_data = json.dumps(data, indent=4)
    json_file = open(f"{path}.json", 'w')
    json_file.writelines(json_data)
    json_file.close()
    return 0

def create_yaml(path, data):
    yaml_file = open(f"{path}.yml", 'w')
    yaml_data = yaml.dump(data, yaml_file)
    yaml_file.close()
    return 0
