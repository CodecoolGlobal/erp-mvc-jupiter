# Do not modify this file (if you want to modify anyway, contact a mentor before, who will explain why do not modify)
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath("test.py")))
sys.path.append(BASE_PATH)


import unittest
from model import data_manager


def compare_lists(tester, expected_list, result_list):
    if len(expected_list) == 0 and len(result_list) == 0:
        return

    if len(expected_list) != 0 and len(result_list) == 0:
        tester.assertListEqual(result_list, expected_list)

    for item in result_list:
        tester.assertTrue(item in expected_list)


def get_subscribed_list():
    return ["hv8@qsuotla508.com;Lieselotte Rainey",
            "t1ytt@vpm5xkvn.com;Maude Toll",
            "-cip@jlyzpvm.com;Fawn Lambrecht",
            "38ds7@0733we.com;Phylis Farberanmt",
            "net@bjewwj9.com;Genoveva Dingess",
            "rnh5z@zss4-n3.com;Royce Stager",
            "x0jp9xg4@2zh-j6v9ai6.com;Pierre Cotta",
            "p7zgwk@jszadvjsr.com;Concetta Nussbaum",
            "ixnqwxkgvlppx9@4qt-a5jtsj.com;Missy Stoney",
            "ufvp64.ghw5@r2l3f1.com;Sadye Hession",
            "u6vt7o4@n7a-0t.com;Kanesha Moshier",
            "qq9.-2o1cj2bii@g2fdac.com;Caleb Paschal"]


def get_item_sold_between_dates():
    return [["eH34Ju#&", "Astebreed", 25, 3, 10, 2016],
            ["bH34Ju#&", "Age of Wonders II: The Wizard's Throne", 20, 4, 1, 2016],
            ["vH34Ju#&", "AudioSurf", 23, 6, 2, 2016],
            ["kH35Ju#&", "Age of Empires", 11, 3, 7, 2016]]


def get_count_by_manufacturer_list():
    return {"Ensemble Studios": 4,
            "Edelweiss": 1,
            "Triumph Studios": 5,
            "Dylan Fitterer": 1,
            "Frictional Games": 1,
            "Related Designs, Ubisoft Blue Byte": 1,
            "Remedy Entertainment": 1,
            "Alexander Bruce": 1,
            "Bohemia Interactive": 2,
            "Valve Corporation": 1,
            "Eugen Systems": 1,
            "Innocent Grey": 2,
            "Black Element Software": 1,
            "Cyanide": 1,
            "Jagex": 1,
            "Hooksoft": 1,
            "Reflexive Entertainment": 1,
            "Advance Reality Interactive": 1,
            "Gears for Breakfast": 1,
            "Games Farm": 2}


def check_forbidden_functions(tester, file_name):
    with open(file_name, "r") as file:
        lines = file.read()
        tester.assertEqual(lines.find("find("), -1)
        tester.assertEqual(lines.find("sort("), -1)
        tester.assertEqual(lines.find("sorted("), -1)
        tester.assertEqual(lines.find("sum("), -1)
        tester.assertEqual(lines.find("count("), -1)
        tester.assertEqual(lines.find("index("), -1)
        tester.assertEqual(lines.find("print("), -1)
        tester.assertEqual(lines.find("input("), -1)


def check_forbidden_list_functions(tester, file_name):
    with open(file_name, "r") as file:
        lines = file.read()
        tester.assertEqual(lines.find("find("), -1)
        tester.assertEqual(lines.find("sort("), -1)
        tester.assertEqual(lines.find("sorted("), -1)
        tester.assertEqual(lines.find("sum("), -1)
        tester.assertEqual(lines.find("count("), -1)
        tester.assertEqual(lines.find("index("), -1)


class CommonTester(unittest.TestCase):

    def test_forbidden_functions(self):
        check_forbidden_functions(self, "model/common.py")


class terminal_viewTester(unittest.TestCase):

    def test_forbidden_functions(self):
        check_forbidden_list_functions(self, "view/terminal_view.py")
