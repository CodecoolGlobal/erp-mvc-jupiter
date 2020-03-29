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

    table[:] = updated_list
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
    updated_list = []
    id_index = 0
    for game in table:
        id = game[id_index]
        if id != id_:
            updated_list.append(game)
    
    table[:] = updated_list
    return table
   

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
    
    manufacturer_index = 2
    price_index = 3
    manufacturers_counter = 0
    whole_price = 0

    for game in table:
        game_manufacturer = game[manufacturer_index]
        game_price = int(game[price_index])
        if manufacturer == game_manufacturer:
            whole_price = whole_price + game_price
            manufacturers_counter += 1

    average_price = whole_price / manufacturers_counter
    return average_price

def get_oldest_game(table):
    
    date_index = 4
    first_date = table[1][date_index]
    first_list = first_date.split("-")
    oldest_date = int(str(first_list[0]) + str(first_list[1]) + str(first_list[2]))
    title_index = 1

    for game in table[1:]:
        game_date = game[date_index]
        date_list = game_date.split("-")
        date_formatted = int(str(date_list[0]) + str(date_list[1]) + str(date_list[2]))
                
        if date_formatted < oldest_date:
            oldest_date = date_formatted
            oldest_game = []
            oldest_game.append(game[title_index])
            oldest_game.append(game[date_index])
    
    return oldest_game

def get_cheapest_game(table):

    price_index = 3
    first_cheapest = table[1][price_index]
    cheapest_price = int(first_cheapest)
    title_index = 1

    for game in table[1:]:
        game_price = int(game[price_index])
                
        if game_price < cheapest_price:
            cheapest_price = game_price
            cheapest_game = []
            cheapest_game.append(game[title_index])
            cheapest_game.append(game_price)
    
    return cheapest_game


def get_age_by(title, table):
    current_year = 2020
    current_month = 4
    title_index = 1
    date_index = 4

    for game in table:
        game_title = game[title_index]
        game_date = game[date_index]
        if game_title == title:
            game_date_list = game_date.split("-")
            game_year = int(game_date_list[0])
            game_month = int(game_date_list[1])
            if (current_month - game_month) < 0:
                age = current_year - game_year - 1
            else:
                age = current_year - game_year

            age_by_title = []
            age_by_title.append(game[title_index])
            age_by_title.append(age)
            
    return age_by_title


def get_game_by(keyword, table):
    pass
