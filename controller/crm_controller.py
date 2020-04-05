# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from model import data_manager

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
              "Create record",
              "Read record",
              "Upodate record", 
              "Delete record",
              "Return to main menu"]

    choice = None

    while choice != "11":
        table = crm.get_table('model/crm/customers.csv')
        choice = terminal_view.get_choice(options)

        if choice == "1":
            label = "Id of user with longest name id:"
            result = crm.get_longest_name_id(table)
            terminal_view.print_result(result, label)

        elif choice == "2":
            label = "Customers subscribed to newsletter:"
            result = crm.get_subscribed_emails(table)
            terminal_view.print_result(result, label)

        elif choice == "3":
            label = "Youngest customer name:"
            result = crm.get_youngest_customer(table)
            terminal_view.print_result(result, label)

        elif choice == "4":
            surname = terminal_view.get_inputs(["Surname: "], "Provide customer surname")
            label = "Age of this customer is:"
            surnames = crm.read_surname(table)
            
            while surname[0] not in surnames:
                surname = terminal_view.get_inputs(["Surname: "], "Provide correct customer surname")
 
            result = crm.get_age_by(surname[0], table)
            terminal_view.print_result(result, label)

        elif choice == "5":
            surname = terminal_view.get_inputs(["Surname: "], "Provide customer surname")
            label = "Email of this customer is:"
            result = crm.get_email_by(surname[0], table)
            terminal_view.print_result(result, label)

        elif choice == "6":
            surname = terminal_view.get_inputs(["Surname: "], "Provide customer surname")
            label = "Firstname of this customer is:"
            result = crm.get_first_name_by(surname[0], table)
            terminal_view.print_result(result, label)

        elif choice == "7":
            id = crm.generate_random(table)
            name = terminal_view.get_inputs(["Name: "], "Provide customer name")[0]
            email = terminal_view.get_inputs(["Email: "], "Provide customer email")[0]
            birthdate = terminal_view.get_inputs(["Birthdate: "], "Provide customer birthdate")[0]
            subscribed_letter = terminal_view.get_inputs(["Subsciribed: "], "Is customer subscribed to newsletter [y/n]")[0]
            
            if subscribed_letter == "y":
                subscirbed = "1"
            else: 
                subscirbed = "0" 
            record = [id, name, email, birthdate, subscirbed]
            
            table = crm.create(table, record)
            data_manager.write_table_to_file('model/crm/customers.csv', table)

        elif choice == "8":
            id_ = terminal_view.get_inputs(["ID: "], "Provide customer id")[0]
            result = crm.read(table, id_)
            label = ""
            terminal_view.print_result(result, label)

        elif choice == "9":
            id_ = terminal_view.get_inputs(["ID: "], "Provide customer id")[0]
            name = terminal_view.get_inputs(["Name: "], "Provide customer name")[0]
            email = terminal_view.get_inputs(["Email: "], "Provide customer email")[0]
            birthdate = terminal_view.get_inputs(["Birthdate: "], "Provide customer birthdate")[0]
            subscribed_letter = str(terminal_view.get_inputs(["Subsciribed: "], "Is customer subscribed to newsletter [y/n]")[0])

            if subscribed_letter == "y":
                subscirbed = "1"
            else: 
                subscirbed = "0" 

            updated_record = [name, email, birthdate, subscirbed]

            table = crm.update(table, id_, updated_record)
            data_manager.write_table_to_file('model/crm/customers.csv', table)

        elif choice == "10":
            id_ = terminal_view.get_inputs(["ID: "], "Provide customer id")[0]
            table = crm.delete(table, id_)
            data_manager.write_table_to_file('model/crm/customers.csv', table)
        
        elif choice == "11":
            terminal_view.print_result("Returning to main menu", "")

        elif choice == "0":
            terminal_view.print_result("", "Goodbye")
            quit()

        else:
            terminal_view.print_error_message("There is no such choice.")