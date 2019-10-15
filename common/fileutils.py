import json
import os
import logging
logger = logging.getLogger(__name__)


def read_new_line_json(path):
    with open(path, "r") as fr:
        content2 = fr.read()
        p = content2.split("\n")
        return [json.loads(i) for i in p if len(i) > 0]


def write_list_as_new_line_json(list_obj, path):
    if list_obj == [{}]:
        raise Exception("empty dictionary can not be inserted")
    with open(path, "w") as fw:
        for i in list_obj:
            fw.write(json.dumps(i))
            fw.write("\n")


def read_json_file(path):
    if not os.path.exists(path):
        try:
            raise FileNotFoundError("File not found")
        except FileNotFoundError as exp:
            print("Error", exp)

    if not path.endswith(".json"):
        try:
            raise ValueError("file extension is not json")
        except ValueError as exp:
            print("Error", exp)

    with open(path, "r") as fj:
        f = fj.read()
        data = json.loads(f)
        return data
        





