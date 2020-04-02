# everything you'll need is imported:
from model.store import store
from view import terminal_view

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ["Get counts of all manufacturers",
               "Get the oldest game",
               "Get cheapest game",
               "Get average games sold by a manufacturer",
               "Get age of a game by its title",
               "Find a game by a keyword"]


    welcome =   """
                 _______.___________.  ______   .______       _______    ____    __    ____  ___      .______       _______     _______.
                /       |           | /  __  \  |   _  \     |   ____|   \   \  /  \  /   / /   \     |   _  \     |   ____|   /       |
               |   (----`---|  |----`|  |  |  | |  |_)  |    |  |__       \   \/    \/   / /  ^  \    |  |_)  |    |  |__     |   (----`
                \   \       |  |     |  |  |  | |      /     |   __|       \            / /  /_\  \   |      /     |   __|     \   \    
            .----)   |      |  |     |  `--'  | |  |\  \----.|  |____       \    /\    / /  _____  \  |  |\  \----.|  |____.----)   |   
            |_______/       |__|      \______/  | _| `._____||_______|       \__/  \__/ /__/     \__\ | _| `._____||_______|_______/    
                                                                                                                                        
    """

    table = store.get_table()

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice_store(welcome, options)

        if choice == "1":
            print(store.get_counts_by_manufacturers(table))

        elif choice == "2":
            print(store.get_oldest_game(table))

        elif choice == "3":
            print(store.get_cheapest_game(table))

        elif choice == "4":
            manufacturer = terminal_view.get_inputs(["Manufacturer: "], "Provide a valid name of a manufacturer")
            all_manufacturers = store.get_counts_by_manufacturers(table)
            while manufacturer[0] not in all_manufacturers:
                manufacturer = terminal_view.get_inputs(["Manufacturer: "], "The manufacturer provided doesn't exist in the file, provide a valid one")
            print(store.get_average_by_manufacturer(table, manufacturer[0]))

        elif choice == "5":
            title = terminal_view.get_inputs(["Title: "], "Provide a valid game title")
            all_titles = []
            for game in table:
                game_title = game[1]
                all_titles.append(game_title)
            while title[0] not in all_titles:
                title = terminal_view.get_inputs(["Title: "], "No such title in the file. Provide a valid game title")
            print(store.get_age_by(title[0], table))

        elif choice == "6":
            keyword = terminal_view.get_inputs(["Keyword: "], "Provide a keyword to search the game by")
            print(store.get_game_by(keyword[0], table))

        else:
            terminal_view.print_error_message("There is no such choice.")
