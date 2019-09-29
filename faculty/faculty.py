from flask import jsonify,request,json
from flask import Blueprint
from os.path import dirname,abspath
from common import fileutils

# print(__name__)
faculty_var = Blueprint('faculty', __name__, url_prefix='/faculty')

# print("loading faculty api....")

file_name = "faculty_data.json"
parent_dir_path = dirname(dirname(abspath(__file__)))
res2 = fileutils.read_new_line_json(parent_dir_path + "/resources/" + file_name)
# print(res2)

@faculty_var.route('/getfaculty', methods=['GET'])
def get_faculty_info():
    # print("ENTRY: get_faculty_info")
    return jsonify(res2)


@faculty_var.route('/getfacultybyname/<string:name>', methods=['GET'])
def get_faculty_by_id(name):
    # print("ENTRY: get_faculty_by_id name: {}".format(name))
    data = None
    for i in res2:
        if i["name"] == name:
            data = i
    return jsonify(res2)


@faculty_var.route('/deletebyname/<string:name>', methods=['DELETE'])
def delete_faculty_by_name(name):
    #print("ENTRY: delete_faculty_by_name name:{} ".format(name))
    for i in res2:
        if i["name"] == name:
            res2.remove(i)
    return jsonify(res2)


@faculty_var.route('/addnewfaculty', methods=['POST'])
def add_new_faculty():
    #print("ENTRY: add_new_faculty")
    name = request.form.get("name")
    age = request.form.get("age")
    salary = request.form.get("salary")
    loc = request.form.get("loc")
    f = {"name": name, "age": age, "salary": salary, "loc": loc}
    data1 = request.get_json(f)
    res2.append(data1)
    file_name = "faculty_data.json"
    parent_dir_path = dirname(dirname(abspath(__file__)))
    fileutils.write_list_as_new_line_json(res2, parent_dir_path + "/resources/" + file_name)
    # with open("/home/ninky/PycharmProjects/first_Rest_Api/faculty/faculty_data.json", "w") as fw1:
    #     for j in res2:
    #         fw1.write(json.dumps(j))
    #         fw1.write("\n")
    return jsonify(res2)


