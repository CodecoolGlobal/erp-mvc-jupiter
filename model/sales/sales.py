""" Sales module """

# modules import go here: 
import random

from model import data_manager
from model.store import store

# global variables go here: 

CUSTOMER_ID = 2
PRODUCT_ID = 3
NUMBER_OF_ITEMS = 4

STORE_PRODUCT_ID = 0
STORE_MANUFACTURER = 2

# sales.csv: 'id, employee_id, customer_id, product_id, number_of_items'

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
    id_list = []
    generated = ""
    for game in table:
        id = game[0]
        id_list.append(id)

    expected_length = 8
    while generated in id_list or len(generated) != expected_length:
        quantity = 2
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        characters = '!@#$%^&*()_+=-{}[]|\:"<>,.?/'
        random_letters = [random.choice(alphabet) for i in range (quantity)] + [random.choice(alphabet).upper() for i in range (quantity)]
        random_characters = [random.choice(characters) for i in range (quantity)]
        random_numbers = [str(random.randint(0, 9)) for i in range (quantity)]
        generated_list = [letter for letter in random_letters] + [character for character in random_characters] + [digit for digit in random_numbers]
        random.shuffle(generated_list)
        generated = "".join(generated_list)

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
    record = [id, store_id, hr_id, crm_id, quantity]
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


def filter_by_customer(table, customer):
    """
    As a user, I want to filter my transactions so that I can know deals with a specific customer.
    
    Args: 
        table (list): 
        customer (): customer's id

    Returns:
        transactions (list):        
    
    """
    transactions = []
    for record in table:
        if CUSTOMER_ID == customer:
            transactions.append(record)
    return transactions


def filter_by_manufacturer(table, manufacturer):
    """
    As a user, I want to filter my transactions so that I can know sales of games per a specific manufacturer.
    
    Args:
        table (list):
        manufacturer (string): 

    Returns:
        sales (): sales of games per a specific manufacturer
    """
    store_table = store.get_table()
    store_id_list = []
    for record in store_table:
        if record[STORE_MANUFACTURER] == manufacturer:
                store_id_list.append(record[STORE_PRODUCT_ID])
    
    sales = 0
    for record in table:
        if record[PRODUCT_ID] in store_id_list:
            sales += int(record[NUMBER_OF_ITEMS])

    return sales


def most_earned(table):
    pass

def rank_by_manufacturer(table):
    manufacturers_counts = {}
    product_id_index = 3
    amount_sold_index = 4
    id_index = 0
    manufacturer_index = 2

    store_table = store.get_table()
    store.check_table(store_table)

    for record in table:
        product_id = record[product_id_index]
        amount_sold = record[amount_sold_index]
        for game in store_table:
            game_id = game[id_index]
            manufacturer = game[manufacturer_index]
            if product_id == game_id:
                if manufacturer in manufacturers_counts:
                    manufacturers_counts[manufacturer] += int(amount_sold)
                else:
                    manufacturers_counts[manufacturer] = int(amount_sold)

    return manufacturers_counts


def gererate_rapoprt():
    pass