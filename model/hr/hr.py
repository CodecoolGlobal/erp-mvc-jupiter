""" Human resources module"""

# everything you'll need is imported:
import random
from model import data_manager


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

    pass




def create(table, record):
    """
    Adds new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    pass




def read(table, id_):
    """
    Get the record from the table by id

    Args:
        table (list): table to get from the record
        id_ (str): id of the record

    Returns:
        list: record
    """
    pass




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

    pass




def delete(table, id_):
    """
    Removes a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    pass


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    pass


def get_persons_closest_to_average_salary(table):
    """
    Question: Who is the closest to the average salary?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    pass


def get_shortest_surname(table):
    pass


def get_age_by(surname, table):
    pass


def get_email_by(surname, table):
    pass


def get_first_name_by(surname, table):
    pass
