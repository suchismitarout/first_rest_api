import mysql.connector
from os.path import dirname,abspath
from first_restapi.common import fileutils
from first_restapi import resources

def read_config_file(file_name):
    parent_dir_path = dirname(dirname(abspath(__file__)))
    file_path = "{}\\resources\\{}".format(parent_dir_path, file_name)
    f = fileutils.read_json_file(file_path)
    return f


def connect_to_student_db(file_name):
    f = read_config_file(file_name)
    conn1 = mysql.connector.connect(host=f["MYSQL_HOST"], user=f["MYSQL_USER"], password=f["MYSQL_PASSWORD"], database=f["MYSQL_DB"])
    return conn1


def connect_to_faculty_db(file_name):
    f = read_config_file(file_name)
    conn2 = mysql.connector.connect(host=f["MYSQL_HOST"], user=f["MYSQL_USER"], password=f["MYSQL_PASSWORD"], database=f["MYSQL_DB"])
    return conn2


def insert_data_to_student_database(conn, list_of_dict):
    cur = conn.cursor()
    columns = ', '.join(list_of_dict.keys())
    values = ', '.join("'" + str(x) + "'" for x in list_of_dict.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('student', columns, values)
    cur.execute(sql)
    conn.commit()


def select_data_from_student_database(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE id = {}".format(id))
    result = cur.fetchall()
    for x in result:
        return x


def delete_data_from_student_database(conn, id):
    cur = conn.cursor()
    query = "DELETE FROM student where id = {}".format(id)
    cur.execute(query)
    conn.commit()


def insert_data_to_faculty_database(conn, list_of_dict):
    cur = conn.cursor()
    columns = ', '.join(list_of_dict.keys())
    values = ', '.join("'" + str(x) + "'" for x in list_of_dict.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('faculty', columns, values)
    cur.execute(sql)
    conn.commit()

def select_data_from_faculty_database(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM faculty WHERE name = '{}'".format(name))
    result = cur.fetchall()
    for x in result:
        return x


def delete_data_from_faculty_database(conn, name):
    cur = conn.cursor()
    query = "DELETE FROM faculty where name = '{}'".format(name)
    cur.execute(query)
    conn.commit()