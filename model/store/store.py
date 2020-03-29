""" Store module """

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
    id_index = 0
    for game in table:
        id = game[id_index]
        if id == id_:
            return game



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
    updated_list = []
    id_index = 0
    for game in table:
        id = game[id_index]
        if id == id_:
            updated_record = []
            updated_record.append(id)
            updated_record = updated_record + record
            updated_list.append(updated_record)
        else:
            updated_list.append(game)
    
    return updated_list


def delete(table, id_):
    """
    Removes a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    updated_list = []
    id_index = 0
    for game in table:
        id = game[id_index]
        if id != id_:
            updated_list.append(game)
    
    return updated_list


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different games are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    game_index = 0
    manufacturer_index = 2
    manufacturers_counts = {}

    for game in table:
        game_manufacturer = table[game_index][manufacturer_index]
        manufacturers_counter = 0
        compare_game_index = 0
        if not game_manufacturer in manufacturers_counts:
            for game in table:
                compare_manufacturer = table[compare_game_index][manufacturer_index]
                if game_manufacturer == compare_manufacturer:
                    manufacturers_counter +=1
                compare_game_index +=1
            manufacturers_counts[game_manufacturer] = manufacturers_counter
        game_index +=1
    return manufacturers_counts


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average price of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    pass


def get_oldest_game(table):
    pass


def get_cheapest_game(table):
    pass


def get_age_by(title, table):
    pass


def get_game_by(keyword, table):
    pass
