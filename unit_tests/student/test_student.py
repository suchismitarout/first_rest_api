import unittest
import requests

class Teststudent(unittest.TestCase):
    def test_student_api_get_response(self):
        response = requests.get("http://127.0.0.1:5000/student/getall")
        self.assertTrue(response.ok)

    def test_get_student_by_id(self):
        response = requests.get("http://127.0.0.1:5000/student/getstudentbyid/16753")
        actual = response.json()
        expected = {"age": 27, "id": 16753, "loc": "delhi", "name": "khirod", "salary": 42000}
        self.assertEqual(expected, actual)

    def test_delete_student_by_id(self):
        response = requests.delete("http://127.0.0.1:5000/student/deletebyid/16753")
        response1 = requests.get("http://127.0.0.1:5000/student/getstudentbyid/16753")
        actual = response1.json()
        self.assertFalse(actual)

    def test_add_student(self):
        response = requests.post("http://127.0.0.1:5000/add_new_student",
                                 json={"name": "khirod", "age": 27, "id": 16753, "salary": 42000, "loc": "delhi"})
        response1 = requests.get("http://127.0.0.1:5000/getstudentbyid/16753")
        self.assertTrue(response1.ok)

