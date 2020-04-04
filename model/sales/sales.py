""" Sales module """

# modules import go here: 
import random

from model import data_manager

# global variables go here: 

def get_table():
    file = "model/sales/sales.csv"
    table = data_manager.get_table_from_file(file)
    return table

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    generated = ''

    printables_letters_lower = 'abcdefghijklmnopqrstuvwxyz'
    printables_letters_upper = printables_letters_lower.upper()
    printables_numbers = '0123456789'
    printables_specials = '!"#$%&\'()*+,-./:?@[\]^_`{|}~'

    printables = [printables_letters_lower, printables_letters_upper, printables_numbers, printables_specials]

    hash_list = ""
    for record in table:
        hash_list.append(record[ID])

    while generated not in hash_list:
        for printables_set in printables:
            choices = random.choices(printables_set, k = 2)
            generated = generated + choices[0] + choices[1]
            generated = ''.join(random.sample(generated, len(generated)))
    return generated


def add_transaction(table, id, store_id, hr_id, crm_id, quantity):
    """ take id, then pair it with corresponding hr_id, customer_id, product_id, and add numbers of bought items,
    put it into new record
    
    Args: 
    list (of lists) - table from sales
    int - id 
    int - id from store
    int - id from hr"
    int - id from crm 
    int - quantity of bought items
    """
    record = []
    record.extend(id, store_id, hr_id, crm_id, quantity)
    table.append(record)

    return table


def filter_by_employee(table, employee_id):
    operations = []
    employee_id_index = 1
    for record in table:
        id = record[employee_id_index]
        if id == employee_id:
            operations.append(record)
    return operations


def filter_by_customer():
    pass


def filter_by_manufacturer():
    pass


def most_earned():
    pass


def rank_by_manufacturer():
    pass


def gererate_rapoprt():
    pass