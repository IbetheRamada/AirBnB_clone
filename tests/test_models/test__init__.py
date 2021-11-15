#!/usr/bin/python3
"""
Tests for storage
"""
import unittest
import pep8
from models.__init__ import storage
from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):
    """
    Class that tests storage
    """

    def test_instances(self):
        """
        Test if storage is instance of FileStorage
        """
        self.assertTrue(storage)
        self.assertIsInstance(storage, FileStorage)

    def test_attributes(self):
        """
        Test for attributes in storage
        """
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))

    def test_pep8_style(self):
        """Test pep8 coding style"""
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/__init__.py'])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors")

if __name__ == '__main__':
    unittest.main()
