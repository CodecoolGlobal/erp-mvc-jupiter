""" Sales module """

# modules import go here: 

from model import data_manager

# global variables go here: 

def get_table():
    file = "model/sales/sales.csv"
    table = data_manager.get_table_from_file(file)
    return table

def add_transaction():
    pass


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