import os
import unittest
from getpassport import isvalid
import logging

class TestAccountNumberMethods(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isvalid(self):
        fields = {
            'byr': "item",
            'iyr': "item2",
            'eyr': "item3",
            'hgt': "item4a",
            'hcl': "item4",
            'ecl': "item5",
            'pid': "item6",
        }
        self.assertTrue(isvalid(fields))

    def test_notisvalid(self):
        fields = {
            'byr': "item",
            'iyr': "item2",
            'eyr': "item3",
            'hgt': "item4a",
            'hcl': "item4",
            'ecl': "item5",
            'cid': "item6",
        }
        self.assertFalse(isvalid(fields))

    def test_notisvalid2(self):
        fields = {
            'iyr': "item2",
            'eyr': "item3",
            'hgt': "item4a",
            'hcl': "item4",
            'ecl': "item5",
            'pid': "item6",
        }
        self.assertFalse(isvalid(fields))


if __name__ == '__main__':
    unittest.main()