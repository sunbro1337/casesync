import os
from file_manager import read_yaml

x = os.walk(
    top='test_cases/[Acceptance for Branch]'
)

# for i in x:
#     print(i)


# Example:
# C:\Users\cyril\AppData\Local\Programs\Python\Python38\python.exe D:/CodeProjects/WelcomeToMars/test.py
# ('test_cases/[Acceptance for Branch]', ['Acceptance'], [])
# ('test_cases/[Acceptance for Branch]\\Acceptance', [], ['Все билды Android собраны.yml', 'Все билды IOS собраны.yml', 'Все билды PC собраны.yml', 'Все билды PS4 собраны.yml', 'Все билды PS5 собраны .yml', 'Все билды Xbox Scarlett собраны.yml', 'Все билды Xbox собраны.yml', 'Загрузка в бой.yml', 'Проверка платформенной авторизации.yml'])
#
# Process finished with exit code 0
#


def collect_yaml_data(path: str, data_types: list):
    yaml_data = read_yaml(os.path.join(path))
    result_data = {}
    for key in yaml_data.keys():
        for i in data_types:
            if key == i:
                result_data[key] = yaml_data[key]
    return result_data

#print(collect_yaml_data(
#    path='test_cases/[Acceptance for Branch]/Acceptance/Проверка платформенной авторизации.yml',
#    data_types=['suite_id', 'section_id', 'id']
#))
