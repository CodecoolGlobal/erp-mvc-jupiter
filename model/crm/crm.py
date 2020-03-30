""" Customer Relationship Management (CRM) module """

# everything you'll need is imported:
import random
import datetime

from model import data_manager

ID = 0
NAME = 1
EMAIL = 2
BIRTHDATE = 3
SUBSCRIBED = 4

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

    for printables_set in printables:
        choices = random.choices(printables_set, k = 2)
        generated = generated + choices[0] + choices[1]
        generated = ''.join(random.sample(generated, len(generated)))
    return generated


def create(table, record):
    """
    Adds new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    table.append(record)
    return table


def read(table, id_):
    """
    Get the record from the table by id

    Args:
        table (list): table to get from the record
        id_ (str): id of the record

    Returns:
        list: record
    """
    for record in table:
        if record[ID] == id_:
            return record


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """
    for row in table:
        if row[ID] == id_:
            for index in range(len(record)):
                record[index] = row[index]
    return table


def delete(table, id_):
    """
    Removes a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    for record_index in range(len(table)):
        if table[record_index][ID] == id_:
            table.pop(record_index)
            return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    longest_name = ""
    longest_name_id = ""

    for record in table: 
        if len(table[NAME]) > len(longest_name):
            longest_name = record[NAME]
            longest_name_id = record[ID]
        elif len(table[NAME]) == len(longest_name):
            if longest_name > record[NAME]:
                longest_name_id = record[ID]
    
    return longest_name_id


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """
    subscribed_list = []    
    for record in table:
        if record[SUBSCRIBED]:
            subscriber_record = record[EMAIL].rstrip() + ";" + record[NAME]
            subscribed_list.append(subscriber_record)

    return subscribed_list


def get_youngest_customer(table):
    """
        Question: What is the name of the youngest customer?

        Args:
            table (list): data table to work on

        Returns:
            int: age of the yougest customer (full years)
        """

    
    youngest_birthdate ='0001-01-01'
    youngest_customer = []

    for record in table:
        current_birthdate = record[BIRTHDATE].translate([None, "-"])
        if current_birthdate > youngest_birthdate.translate([None, "-"]):
            youngest_birthdate = current_birthdate
            youngest_customer = record

    return youngest_customer


def get_age_by(surname, table):
    """ Return age of username with given surname
    
    Args:
    string: customer surname
    table (list): data table to work on

    Return:
    int: age of customer
     """

    current_firstname = 0
    current_surname = 1
    user_birthdate = ""

    for record in table:
        name = record[NAME].split(" ")
        if name[current_surname] == surname:
            user_birthdate = record[BIRTHDATE]

    year = 0
    month = 1
    day = 2

    user_birthdate = user_birthdate.split("-")

    today = datetime.date.today()
    today_conversion = today.strftime('%Y/%m/%d')
    today_conversion = today_conversion.split("/")
    this_year_birthday = datetime.date(int(today_conversion[year]), int(user_birthdate[month]), int(user_birthdate[day]))
    if this_year_birthday > today:
        years = int(today_conversion[year]) - int(user_birthdate[year])
    else:
        years = int(today_conversion[year]) - int(user_birthdate[year]) - 1

    return years


def get_email_by(surname, table):
    """ Return email of user with given surname.

        Args: 
        str: user surname 
        table (list): data table to work on

        Return:
        str: user email"""

    current_firstname = 0
    current_surname = 1
    user_email = ""

    for record in table:
        name = record[NAME].split(" ")
        if name[current_surname] == surname:
            user_email = record[EMAIL]

    return user_email


def get_first_name_by(surname, table):
    """ Return email of user with given surname.

        Args: 
        str: user surname 
        table (list): data table to work on

        Return:
        str: user email"""

    current_firstname = 0
    current_surname = 1
    user_firstname = ""

    for record in table:
        name = record[NAME].split(" ")
        if name[current_surname] == surname:
            user_firstname = name[current_firstname]

    return user_firstname
