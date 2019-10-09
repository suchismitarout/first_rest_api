import mysql.connector
from os.path import dirname,abspath
import json
from common import fileutils


def connect_to_student_db(file_name):
    parent_dir_path = dirname(dirname(abspath(__file__)))
    file_path = parent_dir_path + "\\resources\\" + file_name
    f = fileutils.read_json_file(file_path)
    conn1 = mysql.connector.connect(host=f["MYSQL_HOST"], user=f["MYSQL_USER"], password=f["MYSQL_PASSWORD"], database=f["MYSQL_DB"])
    return conn1


def connect_to_faculty_db():
    conn2 = mysql.connector.connect(host=f["MYSQL_HOST"], user=f["MYSQL_USER"], password=f["MYSQL_PASSWORD"], database=f["MYSQL_DB"])
    return conn2


def insert_data_to_student_database(conn, list_of_dict):
    cur = conn.cursor()
    for i in data:
        columns = ', '.join("""""" + str(x) + """""" for x in i.keys())
        values = ', '.join("'" + str(x) + "'" for x in i.values())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('student', columns, values)
        cur.execute(sql)
        conn.commit()


def delete_data_from_student_database(conn):
    cur = conn.cursor()
    query = "DELETE FROM student where id = '16753'"
    cur.execute(query)
    conn.commit()
