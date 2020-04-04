# everything you'll need is imported:
from view import terminal_view
from model.crm import crm

# TABLE = crm.data_manager.get_table_from_file('model/crm/customers.csv')
TABLE = crm.get_table('model/crm/customers.csv')

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

    while choice != "7":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            label = "Id of user with longest name id:"
            result = crm.get_longest_name_id(TABLE)
            terminal_view.print_result(result, label)

        elif choice == "2":
            label = "Customers subscribed to newsletter:"
            result = crm.get_subscribed_emails(TABLE)
            terminal_view.print_result(result, label)

        elif choice == "3":
            label = "Youngest customer name:"
            result = crm.get_youngest_customer(TABLE)
            terminal_view.print_result(result, label)

        elif choice == "4":
            surname = terminal_view.get_inputs(["Surname: "], "Provide customer surname")
            label = "Age of this customer is:"
            surnames = crm.read_surname(TABLE)
            
            while surname[0] not in surnames:
                surname = terminal_view.get_inputs(["Surname: "], "Provide correct customer surname")
 
            result = crm.get_age_by(surname, TABLE)
            terminal_view.print_result(result, label)

        elif choice == "5":
            surname = terminal_view.get_inputs(["Surname: "], "Provide customer surname")
            label = "Email of this customer is:"
            result = crm.get_email_by(surname, TABLE)
            terminal_view.print_result(result, label)

        elif choice == "6":
            surname = terminal_view.get_inputs(["Surname: "], "Provide customer surname")
            label = "Firstname of this customer is:"
            result = crm.get_first_name_by(surname, TABLE)
            terminal_view.print_result(result, label)

        elif choice == "7":
            terminal_view.print_result("Returning to main menu", "")

        elif choice == "0":
            terminal_view.print_result("", "Goodbye")
            quit()

        else:
            terminal_view.print_error_message("There is no such choice.")