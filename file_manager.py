import sys
from xml.etree import ElementTree


def create_xml(name_file, data):
    file = open(f"{name_file}.xml", "w", encoding="utf-8")
    for key in data.keys():
        print(f"{key}: {data[key]}", file=file)
    file.close()


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


def parse_case_file(file):
    case_dict = {
        "description": "",
        "precondition": "",
        "steps": [],
    }
    for event, element in ElementTree.iterparse(file):
        for i in case_dict:
            pass
