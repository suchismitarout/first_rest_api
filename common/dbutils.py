import mysql.connector
from os.path import dirname,abspath
import json

file_name = "db_config.json"
parent_dir_path = dirname(dirname(abspath(__file__)))
file = parent_dir_path + "\\resources\\" + file_name
with open(file, "r") as fr:
    data = fr.read()
    f = json.loads(data)


def connect_to_student_db(f):
    conn1 = mysql.connector.connect(host=f["MYSQL_HOST"], user=f["MYSQL_USER"], password=f["MYSQL_PASSWORD"], database=f["MYSQL_DB"])
    return conn1


def connect_to_faculty_db():
    conn2 = mysql.connector.connect(host=f["MYSQL_HOST"], user=f["MYSQL_USER"], password=f["MYSQL_PASSWORD"], database=f["MYSQL_DB"])
    return conn2


def insert_data_to_student_database(conn, data):
    conn = connect_to_student_db()
    cur = conn.cursor()
    for i in data:
        columns = ', '.join("""""" + str(x) + """""" for x in i.keys())
        values = ', '.join("'" + str(x) + "'" for x in i.values())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('student', columns, values)
        cur.execute(sql)
        conn.commit()


def delete_data_from_student_database():
    conn = connect_to_student_db()
    cur = conn.cursor()
    query = "DELETE FROM student where id = '16753'"
    cur.execute(query)
    conn.commit()
