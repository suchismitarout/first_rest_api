import json

def read_new_line_json(path):
    with open(path, "r") as fr:
        content2 = fr.read()
        p = content2.split("\n")
        return [json.loads(i) for i in p if len(i) > 0]

def write_list_as_new_line_json(list_obj, path):
    with open(path, "w") as fw:
        for i in list_obj:
            fw.write(json.dumps(i))
            fw.write("\n")
            
def read_json_file(path):
    with open(path, "r") as fj:
        f = fj.read()
        data = json.loads(f)
        





