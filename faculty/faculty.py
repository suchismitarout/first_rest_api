from flask import jsonify,request,json
from flask import Blueprint
from os.path import dirname,abspath
from first_restapi.common import fileutils,dbutils,validator

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
def get_faculty_by_name(name):
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
    data1 = request.get_json()
    res2.append(data1)
    validator.validate_id(data1["id"])
    validator.validate_age(data1["age"])
    conn = dbutils.connect_to_faculty_db("db_config.json")
    dbutils.insert_data_to_faculty_database(conn, data1)
    file_name = "faculty_data.json"
    parent_dir_path = dirname(dirname(abspath(__file__)))
    fileutils.write_list_as_new_line_json(res2, parent_dir_path + "/resources/" + file_name)
    return jsonify(res2)


