import os
import unittest
from getpassport2 import isvaliddata
import logging

class TestAccountNumberMethods(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_byrvalid(self):
        fields = {
            'byr': "2002",
        }
        self.assertTrue(isvaliddata(fields))

    def test_byrnotvalid(self):
        fields = {
            'byr': "2003",
        }
        self.assertFalse(isvaliddata(fields))
        fields2 = {
            'byr': "202",
        }
        self.assertFalse(isvaliddata(fields2))

    def test_iyrvalid(self):
        fields = {
            'iyr': "2010",
        }
        self.assertTrue(isvaliddata(fields))

    def test_iyrnotvalid(self):
        fields = {
            'iyr': "2003",
        }
        self.assertFalse(isvaliddata(fields))
        fields2 = {
            'iyr': "202",
        }
        self.assertFalse(isvaliddata(fields2))

    def test_eyrvalid(self):
        fields = {
            'eyr': "2025",
        }
        self.assertTrue(isvaliddata(fields))

    def test_eyrnotvalid(self):
        fields = {
            'eyr': "2003",
        }
        self.assertFalse(isvaliddata(fields))
        fields2 = {
            'eyr': "202",
        }
        self.assertFalse(isvaliddata(fields2))

    def test_hgtvalid(self):
        fields = {
            'hgt': "190cm",
        }
        self.assertTrue(isvaliddata(fields))
        fields2 = {
            'hgt': "60in",
        }
        self.assertTrue(isvaliddata(fields2))

    def test_hgtnotvalid(self):
        fields = {
            'hgt': "190",
        }
        self.assertFalse(isvaliddata(fields))
        fields2 = {
            'hgt': "100cm",
        }
        self.assertFalse(isvaliddata(fields2))
        fields3 = {
            'hgt': "190in",
        }
        self.assertFalse(isvaliddata(fields3))

    def test_eclvalid(self):
        fields = {
            'ecl': "brn",
        }
        self.assertTrue(isvaliddata(fields))

    def test_eclnotvalid(self):
        fields = {
            'ecl': "wat",
        }
        self.assertFalse(isvaliddata(fields))

    def test_pidvalid(self):
        fields = {
            'pid': "000000001",
        }
        self.assertTrue(isvaliddata(fields))

    def test_pidnotvalid(self):
        fields = {
            'pid': "0123456789",
        }
        self.assertFalse(isvaliddata(fields))

    def test_notallvalid(self):
        fields = {
            'eyr': '1972',
            'cid': '100',
            'hcl': '#18171d',
            'ecl':'amb',
            'hgt': '170',
            'pid': '186cm',
            'iyr': '2018',
            'byr': '1926'
        }
        self.assertFalse(isvaliddata(fields))

    def test_notallvalid2(self):
        fields = {
            'eyr': '1967',
            'cid': '100',
            'hcl': '#602927',
            'ecl':'grn',
            'hgt': '170cm',
            'pid': '012533040',
            'iyr': '2019',
            'byr': '1946'
        }
        self.assertFalse(isvaliddata(fields))

    def test_validall(self):
        fields = {
            'pid': '087499704',
            'hgt': '74in',
            'ecl': 'grn',
            'iyr': '2012',
            'eyr': '2030',
            'byr': '1980',
            'hcl': '#623a2f'
        }
        self.assertTrue(isvaliddata(fields))

    def test_validall2(self):
        fields = {
            'eyr': '2029',
            'ecl': 'blu',
            'cid': '129',
            'byr': '1989',
            'iyr': '2014',
            'pid': '896056539',
            'hcl': '#a97842',
            'hgt': '165cm'
        }
        self.assertTrue(isvaliddata(fields))


if __name__ == '__main__':
    unittest.main()