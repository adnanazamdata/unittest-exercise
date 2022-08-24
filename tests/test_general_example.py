import unittest
from unittest import mock
import sys
sys.path.append('../')
from src.general_example import GeneralExample

obj = GeneralExample()

class test_general_example(unittest.TestCase):

    def test_flatten_dictionary(self):
        d = {'key1': [3, 2, 1], 'key2': [42, 55, 10], 'key3': [0, 22]}
        result = obj.flatten_dictionary(d)
        self.assertEqual(result, [0, 1, 2, 3, 10, 22, 42, 55])


    def test_load_employee_rec_from_database(self):
        result = obj.load_employee_rec_from_database()
        self.assertEqual(result, ['emp001', 'Sam', '100000'])

    @mock.patch('src.general_example.GeneralExample.load_employee_rec_from_database', return_value=['123', 'abc','1000'])
    def test_fetch_emp_details(self, mock_output):
        d = {
            'empId': '123',
            'empName': 'abc',
            'empSalary': '1000'
        }
        result = obj.fetch_emp_details()
        self.assertEqual(result, d)
        



if __name__ == '__main__':
    unittest.main()

        




