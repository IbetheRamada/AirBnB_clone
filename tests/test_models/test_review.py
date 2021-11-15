#!/usr/bin/python3
"""
Tests for class Review
"""
import unittest
import pep8
from models.review import Review
from models.base_model import BaseModel
import datetime


class TestReview(unittest.TestCase):
    """
    Class that tests class Review
    """

    def test_instances(self):
        """
        Test if obj is instance of Review
        """
        obj = Review()
        self.assertIsInstance(obj, Review)
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """
        Test for attributes in obj
        """
        obj = Review()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "__str__"))
        self.assertTrue(hasattr(obj, "save"))
        self.assertTrue(hasattr(obj, "to_dict"))
        self.assertTrue(hasattr(obj, "place_id"))
        self.assertTrue(hasattr(obj, "user_id"))
        self.assertTrue(hasattr(obj, "text"))

    def test_obj_attr(self):
        """
        Test type of attributes
        """
        obj = Review()
        obj_2 = Review()
        self.assertEqual(type(obj.created_at), type(obj.updated_at))
        self.assertIs(type(obj.created_at), datetime.datetime)
        self.assertIs(type(obj.updated_at), datetime.datetime)
        self.assertIs(type(obj.id), str)
        self.assertNotEqual(obj.id, obj_2.id)

    def test_to_dict(self):
        """
        Test method to_dict
        """
        obj = Review()
        self.assertIs(type(obj.created_at), datetime.datetime)
        self.assertIs(type(obj.updated_at), datetime.datetime)
        dict_obj = obj.to_dict()
        self.assertIs(type(dict_obj), dict)
        self.assertIs(type(dict_obj["created_at"]), str)
        self.assertIs(type(dict_obj["updated_at"]), str)
        self.assertTrue(dict_obj["__class__"])
        self.assertEqual(dict_obj["__class__"], "Review")

    def test_to_save(self):
        """
        Test method save
        """
        obj = Review()
        time_1 = obj.updated_at
        obj.save()
        time_2 = obj.updated_at
        self.assertNotEqual(time_1, time_2)
        self.assertIs(type(time_1), datetime.datetime)
        self.assertIs(type(time_1), datetime.datetime)

    def test_pep8_style(self):
        """Test pep8 coding style"""
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/review.py'])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors")

if __name__ == '__main__':
    unittest.main()
