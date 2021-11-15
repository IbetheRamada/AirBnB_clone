#!/usr/bin/python3
"""
Tests for class User
"""
import unittest
import pep8
from models.user import User
from models.base_model import BaseModel
import datetime


class TestUser(unittest.TestCase):
    """
    Class that tests class User
    """

    def test_instances(self):
        """
        Test if obj is instance of User
        """
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """
        Test for attributes in obj
        """
        obj = User()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "__str__"))
        self.assertTrue(hasattr(obj, "save"))
        self.assertTrue(hasattr(obj, "to_dict"))
        self.assertTrue(hasattr(obj, "email"))
        self.assertTrue(hasattr(obj, "password"))
        self.assertTrue(hasattr(obj, "first_name"))
        self.assertTrue(hasattr(obj, "last_name"))

    def test_obj_attr(self):
        """
        Test type of attributes
        """
        obj = User()
        obj_2 = User()
        self.assertEqual(type(obj.created_at), type(obj.updated_at))
        self.assertIs(type(obj.created_at), datetime.datetime)
        self.assertIs(type(obj.updated_at), datetime.datetime)
        self.assertIs(type(obj.id), str)
        self.assertNotEqual(obj.id, obj_2.id)

    def test_to_dict(self):
        """
        Test method to_dict
        """
        obj = User()
        self.assertIs(type(obj.created_at), datetime.datetime)
        self.assertIs(type(obj.updated_at), datetime.datetime)
        dict_obj = obj.to_dict()
        self.assertIs(type(dict_obj), dict)
        self.assertIs(type(dict_obj["created_at"]), str)
        self.assertIs(type(dict_obj["updated_at"]), str)
        self.assertTrue(dict_obj["__class__"])
        self.assertEqual(dict_obj["__class__"], "User")

    def test_to_save(self):
        """
        Test method save
        """
        obj = User()
        time_1 = obj.updated_at
        obj.save()
        time_2 = obj.updated_at
        self.assertNotEqual(time_1, time_2)
        self.assertIs(type(time_1), datetime.datetime)
        self.assertIs(type(time_1), datetime.datetime)

    def test_pep8_style(self):
        """Test pep8 coding style"""
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/user.py'])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors")

if __name__ == '__main__':
    unittest.main()
