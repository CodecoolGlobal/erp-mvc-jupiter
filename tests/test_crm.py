# Customer Relationship Management (CRM) module
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath("test_crm.py")))
sys.path.append(BASE_PATH)


from model import data_manager
import unittest

from model.crm import crm
from test import check_forbidden_functions, get_subscribed_list, compare_lists


class CRMTester(unittest.TestCase):
    data_file = "customers_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "../model/crm/crm.py")

    def test_get_longest_name_id(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = crm.get_longest_name_id(table)
        self.assertEqual(result, "kH38Jm#&")

    def test_get_subscribed_emails(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = get_subscribed_list()
        result = crm.get_subscribed_emails(table)
        compare_lists(self, expected, result)

    def test_create_record(self):
        table = data_manager.get_table_from_file(self.data_file)
        test_record = ["bH34Jx#&","Carin Arevalo","f7j79rcbhifh@klz5lexti6wo.com","0"]
        crm.create(table, test_record)
        self.assertTrue(test_record in table)

    def test_fetch_record_by_id(self):
        table = data_manager.get_table_from_file(self.data_file)
        record_id_to_found = "vH34Jz#&"
        expected_record = ["vH34Jz#&", "Royce Stager", "rnh5z@zss4-n3.com", "1959-12-19", "1"]
        actual_record = crm.read(table, record_id_to_found)
        self.assertListEqual(actual_record, expected_record)

    def test_update_record(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected_updated_record = ["kH38Jm#&", 'x' ,'x', 'x', 'x']
        updated_data_row = ['x' , 'x', 'x', 'x']
        crm.update(table, "kH38Jm#&", updated_data_row)
        self.assertListEqual(table[0], expected_updated_record)

    def test_remove_record(self):
        table = data_manager.get_table_from_file(self.data_file)
        record_id_to_delete = "tH34Jl#&"
        crm.delete(table, record_id_to_delete)

        element_found = False

        for data_row in table:
            for data_element in data_row:
                if data_element == record_id_to_delete:
                    element_found = True

        self.assertFalse(element_found)

    def test_youngest_customer(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected_customer_data = ["kH94Jc#&", "Daniele Coach", "l8hv5k5gt@c5hsou.com", "2000-03-24", "0"]
        actual_customer_data = crm.get_youngest_customer(table)
        self.assertListEqual(actual_customer_data, expected_customer_data)

    def test_get_age_by(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected_age = 19
        actual_outcome_age = crm.get_age_by("Coach", table)
        self.assertTrue(actual_outcome_age == expected_age)

    def test_get_email_by(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected_email = "t1ytt@vpm5xkvn.com"
        surname_to_find_email = "Toll"
        actual_outcome_email = crm.get_email_by(surname_to_find_email, table)
        self.assertEqual(actual_outcome_email, expected_email)

    def test_get_first_name_by(self):
        table = data_manager.get_table_from_file(self.data_file)
        surname = "Kossman"
        expected_first_name = "Signe"
        actual_outcome_name = crm.get_first_name_by(surname, table)
        self.assertEqual(actual_outcome_name, expected_first_name)

if __name__ == '__main__':
    main()

def main():
    unittest.main()
