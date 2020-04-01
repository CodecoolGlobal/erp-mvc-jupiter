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
    options = ["Function 1",
               "Function 2",
               "Function 3"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            store_controller.run()
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            crm_controller.run()
        else:
            terminal_view.print_error_message("There is no such choice.")
