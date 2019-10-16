import unittest
from first_restapi.common import dbutils
import mysql.connector

class Testdbutils(unittest.TestCase):
    def test_connect_to_student_db(self):
        result = dbutils.connect_to_student_db("db_config.json")
        self.assertTrue(result)

    def test_connect_to_faculty_db(self):
        result = dbutils.connect_to_faculty_db("db_config.json")
        self.assertTrue(result)

    def test_insert_data_to_student_database(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="vnprout@1234", database="student")
        data = {"name": "raima", "age": 27, "id": 35113, "salary": 40000, "loc": "blr"}
        dbutils.insert_data_to_student_database(conn, data)
        actual = dbutils.select_data_from_student_database(conn, 35113)
        self.assertTrue(actual)

    def test_delete_data_from_student_database(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="vnprout@1234", database="student")
        dbutils.delete_data_from_student_database(conn,35113)
        actual = dbutils.select_data_from_student_database(conn, 35113)
        self.assertFalse(actual)


    def test_insert_data_to_faculty_database(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="vnprout@1234", database="faculty")
        data = {"name": "rita", "age": 32, "salary": 60000, "loc": "blr"}
        dbutils.insert_data_to_faculty_database(conn, data)
        actual = dbutils.select_data_from_faculty_database(conn, 'rita')
        self.assertTrue(actual)

    def test_delete_data_from_faculty_database(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="vnprout@1234", database="faculty")
        dbutils.delete_data_from_faculty_database(conn, 'rita')
        actual = dbutils.select_data_from_faculty_database(conn, 'rita')
        self.assertFalse(actual)








