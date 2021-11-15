#!/usr/bin/python3
"""
Tests for class FileStorage
"""
from optparse import Values
import unittest
import pep8
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Class that tests class FileStorage
    """

    def test_instances(self):
        """
        Test if obj is instance of FileStorage
        """
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_attributes(self):
        """
        Test for attributes in obj
        """
        obj = FileStorage()
        self.assertTrue(FileStorage, "__file_path")
        self.assertTrue(FileStorage, "__objects")
        self.assertTrue(hasattr(obj, "all"))
        self.assertTrue(hasattr(obj, "new"))
        self.assertTrue(hasattr(obj, "save"))
        self.assertTrue(hasattr(obj, "reload"))

    def test_obj_attr(self):
        """
        Test type of attributes
        """
        obj = FileStorage()
        self.assertIs(type(obj._FileStorage__objects), dict)
        self.assertIs(type(obj._FileStorage__file_path), str)

    def test_all(self):
        """
        Test method all
        """
        obj = FileStorage()
        dict_obj = obj.all()
        self.assertIsNotNone(dict_obj)
        self.assertIs(type(dict_obj), dict)
        self.assertIs(dict_obj, obj._FileStorage__objects)

    def test_new(self):
        """
        Test method new
        """
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        obj = FileStorage()
        obj.new(my_user)
        dict_obj = obj.all()
        class_id = my_user.__class__.__name__ + "." + str(my_user.id)
        self.assertIsNotNone(dict_obj[class_id])

    def test_save(self):
        """
        Test method save
        """
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        obj = FileStorage()
        obj.new(my_user)
        dict_obj = obj.all()
        class_id = my_user.__class__.__name__ + "." + str(my_user.id)
        self.assertIsNotNone(dict_obj[class_id])
        obj.save()
        obj_2 = FileStorage()
        obj_2.reload()
        users_dic = obj_2.all()
        self.assertIsNotNone(users_dic.get(class_id))
        self.assertEqual(users_dic[class_id].first_name, my_user.first_name)
        self.assertEqual(users_dic[class_id].last_name, my_user.last_name)
        self.assertEqual(users_dic[class_id].email, my_user.email)
        self.assertEqual(users_dic[class_id].password, my_user.password)

    def test_pep8_style(self):
        """Test pep8 coding style"""
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors")

if __name__ == '__main__':
    unittest.main()
