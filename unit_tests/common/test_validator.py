import unittest
from first_restapi.common import validator


class Testvalidation(unittest.TestCase):
    def test_validation_of_id(self):
        self.assertRaises(Exception, validator.validate_id, "ab")

    def test_validation_of_age(self):
        self.assertRaises(Exception, validator.validate_age, 28)





