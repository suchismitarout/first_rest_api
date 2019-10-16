import unittest
import requests

class Testfaculty(unittest.TestCase):
    def test_get_faculty_info(self):
        response = requests.get("http://127.0.0.1:5000/faculty/getfaculty")
        self.assertTrue(response.ok)

    def test_get_faculty_by_name(self):
        response = requests.get("http://127.0.0.1:5000/faculty/getfacultybyname/tina")
        actual = response.json()
        expected = {"name": "tina", "age": 48, "salary": 65000, "loc": "assam"}
        self.assertEqual(expected, actual)

    def test_delete_faculty_by_name(self):
        response = requests.delete("http://127.0.0.1:5000/faculty/deletebyname/tina")
        response1 = requests.get("http://127.0.0.1:5000/faculty/getfacultybyname/1tina")
        actual = response1.json()
        self.assertFalse(actual)

    def test_add_new_faculty(self):
        response = requests.post("http://127.0.0.1:5000/faculty/addnewfaculty",
                                 json={"name": "kiran", "age": 58, "salary": 75000, "loc": "jaipur"})
        response1 = requests.get("http://127.0.0.1:5000/faculty/getfacultybyname/kiran")
        self.assertTrue(response1.ok)


