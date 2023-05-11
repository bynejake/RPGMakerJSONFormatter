#!/usr/bin/python


import os
import json


def json_format(path: str):
    if os.path.isdir(path):
        for sub_pathname in os.listdir(path):
            json_format(os.path.join(path, sub_pathname))
    else:
        json_format_file(path)


def json_format_file(path: str):
    try:
        print(path)
        with open(path, "r", encoding="utf-8") as rf:
            json_data = json.load(rf)
        with open(path, "w", encoding="utf-8") as wf:
            json.dump(json_data, wf, ensure_ascii=False, indent=4)
    except:
        pass


json_format("data")
