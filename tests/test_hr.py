# Human Resources (HR) module
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath("test_hr.py")))
sys.path.append(BASE_PATH)


import unittest

from model import data_manager
from model.hr import hr
from test import check_forbidden_functions, get_subscribed_list, compare_lists

class HRTester(unittest.TestCase):
    data_file = "persons_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "../model/hr/hr.py")

    def test_check_using_datetime(self):
        with open("../model/hr/hr.py", "r") as file:
            lines = file.read()
            self.assertEqual(lines.find("datetime"), -1)

    def test_get_oldest_person(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = ["Evelin Smile"]
        result = hr.get_oldest_person(table)
        compare_lists(self, expected, result)

    def test_get_persons_closest_to_average(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = ["Jimmy Hendrix"]
        result = hr.get_persons_closest_to_average_salary(table)
        compare_lists(self, expected, result)

    def test_create_record(self):
        table = data_manager.get_table_from_file(self.data_file)
        test_record = ["bH34Jx#&","Carin Arevalo","f7j79rcbhifh@klz5lexti6wo.com","0"]
        hr.create(table, test_record)
        self.assertTrue(test_record in table)

    def test_fetch_record_by_id(self):
        table = data_manager.get_table_from_file(self.data_file)
        record_id_to_found = "jH34Ju#&"
        expected_record = ["jH34Ju#&", "Barbara Streisand", "vbilalp@hdvideo-kontent.ru", "1955-11-21", "4125"]
        actual_record = hr.read(table, record_id_to_found)
        self.assertListEqual(actual_record, expected_record)

    def test_update_record(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected_updated_record = ["kH34Ju#&", 'x' ,'x', 'x', 'x']
        updated_data_row = ['x' , 'x', 'x', 'x']
        hr.update(table, "kH34Ju#&", updated_data_row)
        self.assertListEqual(table[0], expected_updated_record)

    def test_remove_record(self):
        table = data_manager.get_table_from_file(self.data_file)
        record_id_to_delete = "kH35Ju#&"
        hr.delete(table, record_id_to_delete)

        element_found = False

        for data_row in table:
            for data_element in data_row:
                if data_element == record_id_to_delete:
                    element_found = True


        self.assertFalse(element_found)

    def test_get_shortest_surname(self):
        table = data_manager.get_table_from_file(self.data_file)
        actual_surname = hr.get_shortest_surname(table)
        expected = "Dirt"
        self.assertTrue(actual_surname == expected)

    def test_get_age_by(self):
        table = data_manager.get_table_from_file(self.data_file)
        surname_to_fetch_age_from = "Dirt"
        expected_age = 19
        actual_age = hr.get_age_by(surname_to_fetch_age_from, table)
        self.assertTrue(actual_age == expected_age)

    def test_get_first_name_by(self):
        table = data_manager.get_table_from_file(self.data_file)
        surname = "Smile"
        actual_name = hr.get_first_name_by(surname, table)
        expected_name = "Evelin"
        self.assertEqual(actual_name, expected_name)

if __name__ == '__main__':
    unittest.main()
