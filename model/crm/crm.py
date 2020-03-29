""" Customer Relationship Management (CRM) module """

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
    row = table[-1].copy()

    for index in range(len(row)):
        row[index] = record[index]
    
    table.append(row)
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

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    pass


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

    pass


def get_youngest_customer(table):
    pass


def get_age_by(surname, table):
    pass


def get_email_by(surname, table):
    pass


def get_first_name_by(surname, table):
    pass


# TEMPORARY FUNCTIONS BELOW----------------------------------- 
def main():
    table = [[1, 'John', 'Orange'],[2, 'Mark', 'Kiwi'],[3, 'Susan', 'Grapes']]
    row = [4, 'Joanna', 'Apple']

    table = create(table, row)
    print(table)


if __name__ == '__main__':
    main()