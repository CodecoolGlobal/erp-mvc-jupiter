# Store module
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath("test_store.py")))
sys.path.append(BASE_PATH)


import unittest

from model import data_manager
from model.store import store
from test import check_forbidden_functions, get_count_by_manufacturer_list, compare_lists


class StoreTester(unittest.TestCase):
    data_file = "games_test.csv"

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "../model/store/store.py")

    def test_get_counts_by_manufacturers(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = get_count_by_manufacturer_list()
        result = store.get_counts_by_manufacturers(table)
        self.assertEqual(result, expected)

    def test_get_average_by_manufacturer(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = store.get_average_by_manufacturer(table, "Ensemble Studios")
        self.assertEqual(result, 28.25)

    def test_create_record(self):
        table = data_manager.get_table_from_file(self.data_file)
        test_record = ["bH37Jx#&","Minecraft 2","Microsoft","11", "2028-11-07"]
        store.create(table, test_record)
        self.assertTrue(test_record in table)

    def test_fetch_record_by_id(self):
        table = data_manager.get_table_from_file(self.data_file)
        record_id_to_found = "bH34Jx#&"
        expected_record = ["bH34Jx#&", "ARMA 2", "Bohemia Interactive", "43", "2008-09-10"]
        actual_record = store.read(table, record_id_to_found)
        self.assertListEqual(actual_record, expected_record)

    def test_update_record(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected_updated_record = ["kH34Ju#&", 'x' ,'x', 'x', 'x']
        updated_data_row = ['x' , 'x', 'x', 'x']
        store.update(table, "kH34Ju#&", updated_data_row)
        self.assertListEqual(table[0], expected_updated_record)

    def test_remove_record(self):
        table = data_manager.get_table_from_file(self.data_file)
        record_id_to_delete = "tH34Jl#&"
        store.delete(table, record_id_to_delete)

        element_found = False

        for data_row in table:
            for data_element in data_row:
                if data_element == record_id_to_delete:
                    element_found = True

        self.assertFalse(element_found)

    def test_get_oldest_game(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = ["Act of War: Direct Action", "1996-07-28"]
        actual = store.get_oldest_game(table)
        self.assertListEqual(expected, actual)

    def test_get_cheapest_game(self):
        table = data_manager.get_table_from_file(self.data_file)
        expected = ["Age of Empires", 11]
        actual = store.get_cheapest_game(table)
        self.assertListEqual(expected, actual)

    def test_get_age_by(self):
        table = data_manager.get_table_from_file(self.data_file)
        title = "A Fairy Tale"
        expected = ["A Fairy Tale", 9]
        actual = store.get_age_by(title, table)
        self.assertListEqual(expected, actual)

    def test_get_game_by(self):
        table = data_manager.get_table_from_file(self.data_file)
        keyword = "Swarm"
        expected = ["vH34Jz#&", "Alien Swarm", "Valve Corporation", "49", "2009-12-22"]
        actual_game = store.get_game_by(keyword, table)
        self.assertListEqual(actual_game, expected)


if __name__ == '__main__':
    unittest.main()
