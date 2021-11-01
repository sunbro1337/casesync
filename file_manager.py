import os


def create_json(name_file, data):
    file = open(f"{name_file}.json", "w", encoding="utf-8")
    for key in data.keys():
        print(f"{key}: {data[key]}", file=file)
    file.close()
