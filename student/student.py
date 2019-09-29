from flask import Flask, request,jsonify, g
import json
from flask import Blueprint
from os.path import dirname,abspath
from common import fileutils
from common import fileutils

student_var = Blueprint('student', __name__, url_prefix='/student')

# print("loading student_api.....")
file_name = "student_data.json"
parent_dir_path = dirname(dirname(abspath(__file__)))
res=fileutils.read_new_line_json(parent_dir_path + "/resources/" + file_name)
# print(res)

@student_var.route('/getall', methods=['GET'])
def get_student_info():
    # print("ENTRY:get_student_info")
    return jsonify(res)


@student_var.route('/getstudentbyid/<int:id>', methods=['GET'])
def get_student_info_by_id(id):
    # print("ENTRY: get_student_info_by_id id={}".format(id))
    data = None
    for i in res:
        if i["id"] == id:
            data = i
    return jsonify(data)


@student_var.route('/deletebyid/<int:id>', methods=['DELETE'])
def delete_by_student_by_id(id):
    # print("ENTRY: delete_by_student_by_id id={}".format(id))
    for i in res:
           if i["id"] == id:
            res.remove(i)
    return jsonify(res)


@student_var.route('/add_new_student', methods=['POST'])
def add_new_student():
    # print("ENTRY: add_new_student")
    name = request.form.get("name")
    age = request.form.get("age")
    id = request.form.get("id")
    salary = request.form.get("salary")
    loc = request.form.get("loc")
    d = {"name": name, "age": age, "id": id, "salary": salary, "loc": loc}
    data = request.get_json(d)
    res.append(data)
    ##res.append(data)
    file_name = "student_data.json"
    parent_dir_path = dirname(dirname(abspath(__file__)))
    fileutils.write_list_as_new_line_json(res, parent_dir_path + "/resources/" + file_name)
    # dirpath=os.getcwd()
    # with open ("{}/student_data.json".format(dirpath), "w") as fw:
    #     for i in res:
    #         fw.write(json.dumps(i))
    #         fw.write("\n")

    return jsonify(res)












