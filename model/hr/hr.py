""" Human resources module"""

# everything you'll need is imported:
import random
from model import data_manager

ID = 0
NAME = 1
EMAIL = 2
BIRTH_DATE = 3
SALARY = 4
FUTURE = [2019, 11, 20]  # Blade Runner's action setting time

def get_table(table_adress):
    """ 
    Loads table from file using data mangager
    
    Args:
        table_adress (string): Table path

    Return:
        list: Module database
    """

    table = data_manager.get_table_from_file(table_adress)
    if table[0][0] == 'id':
        table = table[1:]

    return table


def read_surname(table):
    """ 
    Read column of surnames into variable
    
    Args:
        table (list) - Database

    Return:
        list - Column of surnames
    """

    surnames = []
    names = []
    surname_id = 1

    for row in table:
        names.append(row[NAME].split(" "))
    
    for row in names:
        surnames.append(row[surname_id])
    
    return surnames


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
    # todo: redo to meet requirements

    generated = ''

    printables_letters_lower = 'abcdefghijklmnopqrstuvwxyz'
    printables_letters_upper = printables_letters_lower.upper()
    printables_numbers = '0123456789'
    printables_specials = '!"#$%&\'()*+,-./:?@[\]^_`{|}~'

    printables = printables_letters_lower + printables_letters_upper + printables_numbers + printables_specials
    generated = "".join(random.choices(printables, k = 8)) 
    return generated
    

def create(table, record):
    """
    Adds new record to table

    Args:
        table (list): Table to add new record to
        record (list): New record

    Returns:
        list: Table with a new record
    """
    table.append(record)
    return table


def read(table, id_):
    """
    Get the record from the table by id

    Args:
        table (list): Table to get from the record
        id_ (str): Id of the record

    Returns:
        list: Record
    """
    for record in table:
        if record[ID] == id_:
            return record
    

def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: List in which record should be updated
        id_ (str): Id of a record to update
        record (list): Updated record

    Returns:
        list: Table with updated record
    """
    for row in table:
        if row[ID] == id_:
            for index in range(len(record)):
                row[index + 1] = record[index]
    return table
    

def delete(table, id_):
    """
    Removes a record with a given id from the table.

    Args:
        table (list): Table to remove a record from
        id_ (str): Id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    for record_index in range(len(table)):
        if table[record_index][ID] == id_:
            del table[record_index]
            return table

# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): Data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    oldest_birth_date = FUTURE
    for row in table:
        splited_birth_date = row[BIRTH_DATE].split('-')
        if int(splited_birth_date[0]) <= int(oldest_birth_date[0]):
            if int(splited_birth_date[0]) == int(oldest_birth_date[0]) and int(splited_birth_date[1]) <= int(oldest_birth_date[1]):
                if int(splited_birth_date[1]) == int(oldest_birth_date[1]) and int(splited_birth_date[2]) <= int(oldest_birth_date[2]):
                    oldest_birth_date = splited_birth_date
                oldest_birth_date = splited_birth_date
            oldest_birth_date = splited_birth_date
                 
    oldest_persons = []
    for row in table:
        if row[BIRTH_DATE] == '-'.join(oldest_birth_date):
            oldest_persons.append(row[NAME])
    
    return oldest_persons


def get_persons_closest_to_average_salary(table):
    """
    Question: Who is the closest to the average salary?

    Args:
        table (list): Data table to work on

    Returns:
        list: List of strings (name or names if there are two more with the same value)
    """

    # calculate average salary
    sum = 0
    for row in table:
        sum += int(row[SALARY])
    average_salary = sum / len(table)

    # genarate list of differences with regard to the average salary
    diff_list = []
    for row in table:
        diff = abs(int(row[SALARY]) - average_salary)
        diff_list.append(diff)
    
    # find the smallest difference and so the closest salary
    smallest_diff = diff_list[0]
    for row_index in range(len(diff_list)):
        if diff_list[row_index] < smallest_diff:
            smallest_diff = diff_list[row_index]
            closest_salary = table[row_index][SALARY]
    
    # generate list of names of empleyees' with salary closest to average
    persons_closest_to_average_salary = []
    for row in table:
        if row[SALARY] == closest_salary:
            persons_closest_to_average_salary.append(row[NAME])

    return persons_closest_to_average_salary


def get_shortest_surname(table):
    """
    Question: Who's got the shortest surname

    Args:
        table: Data table to work on

    Returns:
        list: List of strings with names

    """

    # get list of surnames
    names_list = []
    splited_name = []
    for row in table:
        splited_name = row[NAME].split(' ')
        names_list.append(splited_name[1])
    
    # get shortest name's lenght
    shortest_name_lenght = len(names_list[0])
    for i in range(len(names_list)):
        if len(names_list[i]) < shortest_name_lenght:
            shortest_name_lenght = len(names_list[i])
    
    # create list of shortest surnames
    shortest_surnames = []
    for i in range(len(names_list)):
        if len(names_list[i]) == shortest_name_lenght:
            shortest_surnames.append(names_list[i])
    
    return shortest_surnames[0]


def get_age_by(surname, table):
    """
    Provides age of the employee specified by surname

    Args:
        surname (string): Employee's surname
        table (list): Data table to work on
    Returns:
        integer: Age
    """
    
    for row in table:
        splited_name = row[NAME].split(' ')
        if splited_name[1] == surname:
            age = 2019 - int(row[BIRTH_DATE][:4])

    return age
    

def get_email_by(surname, table):
    """
    Provides email of the employee specified by surname

    Args:
        surname (string): Employee's surname
        table (list): Data table to work on
    Returns:
        string: Employee's email 
    """

    record_index = get_record_by_surname(surname, table)
    email = table[record_index][EMAIL]
    return email


def get_first_name_by(surname, table):
    """
    Provides first name of the employee specified by surname

    Args:
        surname (string): Employee's surname
        table (list): Data table to work on
    Returns:
        string: Employee's first name

    """
    record_index = get_record_by_surname(surname, table)
    splited_name = table[record_index][NAME].split(' ')
    return splited_name[0]
    

def get_record_by_surname(surname, table):
    """
    What it does: Gets record index by given surname

    Args:
        table (list) : Data table to work on
        surname (string): Employee's surname
    Returns:
        integer: Record index
    """

    for i in range(len(table)):
        splited_name = table[i][NAME].split(' ')
        if splited_name[1] == surname:
            record_index = i
    return record_index

