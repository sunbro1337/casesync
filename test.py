list = [
        {
            "id": 1298788,
            "suite_id": 12210,
            "name": "On start",
            "description": None,
            "parent_id": None,
            "display_order": 6,
            "depth": 0
        },
        {
            "id": 1298789,
            "suite_id": 12210,
            "name": "Меню логина",
            "description": None,
            "parent_id": None,
            "display_order": 7,
            "depth": 0
        },
        {
            "id": 1298790,
            "suite_id": 12210,
            "name": "Logins",
            "description": "https://confluence.wargaming.net/display/WOWSC/Mobile+logins\n\nДля мобильных платформ поле platform и authmEntryPoint в настройках host в scripts_config.xml больше не имеет значения. Тип логина выбирается исключительно по нажатию соответствующих кнопок на экране (awesome, facebook, guest, apple sign in)",
            "parent_id": 1298789,
            "display_order": 8,
            "depth": 1
        },
        {
            "id": 1298791,
            "suite_id": 12210,
            "name": "Linkage",
            "description": None,
            "parent_id": 1298790,
            "display_order": 9,
            "depth": 2
        },
    ]

def find(list: list, key: str, value, returned_key: str) -> dict or None:
    for dict in list:
        if dict[key] == value:
            return dict[returned_key]
    else:
        return None

result = find(list, 'id', 1298790, 'suite_id')
print(result)
