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
               "Get cheapest game"]


    welcome = """
                 _______.___________.  ______   .______       _______    .___  ___.   ______    _______   __    __   __       _______ 
                /       |           | /  __  \  |   _  \     |   ____|   |   \/   |  /  __  \  |       \ |  |  |  | |  |     |   ____|
               |   (----`---|  |----`|  |  |  | |  |_)  |    |  |__      |  \  /  | |  |  |  | |  .--.  ||  |  |  | |  |     |  |__   
                \   \       |  |     |  |  |  | |      /     |   __|     |  |\/|  | |  |  |  | |  |  |  ||  |  |  | |  |     |   __|  
            .----)   |      |  |     |  `--'  | |  |\  \----.|  |____    |  |  |  | |  `--'  | |  '--'  ||  `--'  | |  `----.|  |____ 
            |_______/       |__|      \______/  | _| `._____||_______|   |__|  |__|  \______/  |_______/  \______/  |_______||_______|
                                                                                                                                      
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
        else:
            terminal_view.print_error_message("There is no such choice.")
