import unittest

import test_crm
import test_hr
import test_store

from model import data_manager


def main():
    introduction_text = "Hello!\nWelcome to automated test suite for erp project!\n\
    Please enter name of module to run test on or type all to run all modules!\n"

    incorrect_data_format_warning = "I can't run tests :(\n \
    Your import function from data_manager.py module does not import data in proper format\n\
    !Import should return list of lists\n\
    !Every nested list should contains 5 data elements\n\
    !List cannot be empty\n\
    Please check your implementation and try again"

    print(introduction_text)
    user_input = input("Enter name of module to test or type all to run all tests: ")
    handle_user_input(user_input, incorrect_data_format_warning)


def handle_user_input(user_input,incorrect_data_text):
    if user_input.lower() == "all":
        if verify_data_integrity():
            run_all_modules()
        else:
            print(incorrect_data_text)
    else:
        if verify_data_integrity():
            run_module(user_input)
        else:
            print(incorrect_data_text)


def verify_data_integrity():
    fetched_data = data_manager.get_table_from_file("data_integrity.csv")

    if not fetched_data: return

    fetched_data_is_a_list_of_list = type(fetched_data[0]) is list
    fetched_data_rows_contains_expected_elements_count = True
    expected_row_elements_count = 5

    for data_row in fetched_data:
        if len(data_row) != expected_row_elements_count:
            fetched_data_rows_contains_expected_elements_count = False

    if fetched_data_is_a_list_of_list and fetched_data_rows_contains_expected_elements_count:
        return True

    return False


def run_module(module_name):
    if module_name == "crm":
        suite = unittest.TestLoader().loadTestsFromModule(test_crm)
        unittest.TextTestRunner(verbosity = 2).run(suite)
    elif module_name == "hr":
        suite = unittest.TestLoader().loadTestsFromModule(test_hr)
        unittest.TextTestRunner(verbosity = 2).run(suite)
    elif module_name == "store":
        suite = unittest.TestLoader().loadTestsFromModule(test_store)
        unittest.TextTestRunner(verbosity = 2).run(suite)
    else:
        print("There is no module")



def run_all_modules():
    test_suites = [test_crm, test_hr, test_store]

    for test_suite in test_suites:
        suite = unittest.TestLoader().loadTestsFromModule(test_suite)
        unittest.TextTestRunner(verbosity = 2).run(suite)


if __name__ == '__main__':
    main()
