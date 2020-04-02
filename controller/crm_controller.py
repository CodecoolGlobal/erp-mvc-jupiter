# everything you'll need is imported:
from view import terminal_view
from model.crm import crm

TABLE = crm.data_manager.get_table_from_file('model/crm/customers.csv')

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ["Get longest name id",
              "Get subscribed emails",
              "Get youngest customer", 
              "Get age of user with given surname",
              "Get email of user with given surname",
              "Get fistname of user with given surname",
              "Return to main menu"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            crm.get_longest_name_id(TABLE)
        elif choice == "2":
            crm.get_subscribed_emails(TABLE)
        elif choice == "3":
            crm.get_youngest_customer(TABLE)
        elif choice == "4":
            surname = terminal_view.get_inputs(["Surname: "], "Provide customer surname")
            crm.get_age_by(surname, TABLE)
        elif choice == "5":
            surname = terminal_view.get_inputs(["Surname: "], "Provide customer surname")
            crm.get_email_by(surname, TABLE)
        elif choice == "6":
            surname = terminal_view.get_inputs(["Surname: "], "Provide customer surname")
            crm.get_first_name_by(surname, TABLE)
        elif choice == "7":
            root_controller.run()
        else:
            terminal_view.print_error_message("There is no such choice.")