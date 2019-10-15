import unittest
from first_restapi.common import fileutils
from os.path import dirname,abspath



class Testreadfile(unittest.TestCase):
    def test_read_new_line_json(self):
        """
        this test describes the functionlity of read method.
        :return:
        """
        file_name = "data.json"
        dir_path = dirname(dirname(abspath(__file__)))
        print(dir_path)
        # file_path = dir_path + "/resources/" + file_name
        file_path ="{}\\resources\\{}".format(dir_path,file_name)
        print(file_path)
        actual_output = fileutils.read_new_line_json(file_path)
        print(actual_output)
        expected_output = [{'name': 'romil', 'age': 45, 'salary': 67000, 'loc': 'delhi'}, {'name': 'rajesh', 'age': 40, 'salary': 56000, 'loc': 'blr'}]
        assert expected_output == actual_output

    def test_write_list_as_new_line_json(self):
        file_name = "data1.json"
        dir_path1 = dirname(dirname(abspath(__file__)))
        file_path1 = "{}\\resources\\{}".format(dir_path1,file_name)
        input_list = [{"name":"deepak"},{"name":"abc"}]
        fileutils.write_list_as_new_line_json(input_list,file_path1)

        ## verification process
        # 1. read the above created file.
        content = fileutils.read_new_line_json(file_path1)
        assert input_list==content

    def test_write_list_as_new_line_json_with_empty_dict(self):
        file_name = "data1.json"
        dir_path1 = dirname(dirname(abspath(__file__)))
        file_path1 = "{}\\resources\\{}".format(dir_path1, file_name)
        input_list = [{}]
        self.assertRaises(Exception,fileutils.write_list_as_new_line_json,input_list, file_path1)

    def test_read_json_file_with_nonexisting_file(self):
        file_name = "pk.txt"
        parent_path = dirname(abspath(__file__))
        path = parent_path + "\\" + file_name
        self.assertRaises(Exception,fileutils.read_json_file, path)

    def test_read_json_file_without_json_extension(self):
        file_name = "hn.py"
        parent_path = dirname(abspath(__file__))
        path = "{}\\{}".format(parent_path,file_name)
        self.assertRaises(Exception,fileutils.read_json_file, path)

    def test_read_json_file_with_json_extension(self):
        file_name = "jk.json"
        parent_path = dirname(abspath(__file__))
        path = "{}\\{}".format(parent_path,file_name)
        expected = fileutils.read_json_file(path)
        actual = {"name": "abc"}
        self.assertEqual(expected,actual)



