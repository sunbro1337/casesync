import os

x = os.walk(
    top='test_cases/[Acceptance for Branch]'
)

for i in x:
    print(i)

"""
Example:
C:\Users\cyril\AppData\Local\Programs\Python\Python38\python.exe D:/CodeProjects/WelcomeToMars/test.py
('test_cases/[Acceptance for Branch]', ['Acceptance'], [])
('test_cases/[Acceptance for Branch]\\Acceptance', [], ['Все билды Android собраны.yml', 'Все билды IOS собраны.yml', 'Все билды PC собраны.yml', 'Все билды PS4 собраны.yml', 'Все билды PS5 собраны .yml', 'Все билды Xbox Scarlett собраны.yml', 'Все билды Xbox собраны.yml', 'Загрузка в бой.yml', 'Проверка платформенной авторизации.yml'])

Process finished with exit code 0
"""