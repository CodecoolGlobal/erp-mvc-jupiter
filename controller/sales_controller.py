from model.sales import sales
from view import terminal_view
from model import data_manager


def run():

    options = ["Add a new transaction",
               "Filter transactions by the employee",
               "Filter transactions by the customer",
               "Get the sales of games by a manufacturer",
               "Get the most earning employee",
               "Get a ranking of sold items per manufacturer",
               "Get a ranking of sold items and earned money",
               "Get the worst earning employee"]

    welcome = """
              #####     #        #####     #
             #     #   # #      #     #   # #
             #        #   #     #        #   #
              #####  #     #     #####  #     #
                   # #######          # #######
             #     # #     #    #     # #     #
              #####  #     #     #####  #     #

             #       #######    #       #######
             #       #          #       #
             #       #          #       #
             #       #####      #       #####
             #       #          #       #
             #       #          #       #
             ####### #######    ####### #######

    """

    choice = None

    while choice != "0":
        choice = terminal_view.get_choice_store(welcome, options)
        table = sales.get_table()

        if choice == "1":
            label = "Provide new record /n"
            id = sales.generate_random(table)

            store_id = terminal_view.get_inputs(["Store ID: "], "Provide product ID")
            hr_id = terminal_view.get_inputs(["Employee ID: "], "Provide employee ID")
            crm_id = terminal_view.get_inputs(["Customer ID: "], "Provide customer ID")
            qty = terminal_view.get_inputs(["Quantity: "], "Provide item quantity")
            table_updated = sales.add_transaction(table, id, store_id[0], hr_id[0], crm_id[0], qty[0])
            data_manager.write_table_to_file("model/sales/sales.csv", table_updated)

        elif choice == "2":
            label = "The transactions made by given employee: "
            employee_id = terminal_view.get_inputs(["Employee ID: "], "Provide the employee ID to search for his/her transactions")
            result = sales.filter_by_employee(table, employee_id[0])
            terminal_view.print_result(result, label)

        elif choice == "3":
            label = "The transactions made by given customer: "
            customer_id = terminal_view.get_inputs(["Customer ID: "], "Provide the customer ID to search for his/her transactions")
            result = sales.filter_by_customer(table, customer_id[0])
            terminal_view.print_result(result, label)

        elif choice == "4":
            label = "Number of games sold by a given manufacturer: "
            manufacturer = terminal_view.get_inputs(["Manufacturer: "], "Provide the manufacturer's name")
            result = sales.filter_by_manufacturer(table, manufacturer[0])
            terminal_view.print_result(result, label)

        elif choice == "5":
            label = "Most earning employee"
            result = sales.most_earned(table)
            terminal_view.print_result(result, label)

        elif choice == "6":
            label = "Manufacurer | sold copies"
            result = sales.rank_by_manufacturer(table)
            terminal_view.print_result(result, label)

        elif choice == "7":
            raport = sales.generate_raport(table)
            raport_header = ["title", "total earnings"]
            terminal_view.print_table(raport, raport_header)
            data_manager.write_table_to_file("model/sales/raport.csv", raport)

        elif choice == "8":
            label = "Min earning employee"
            result = sales.min_earned(table)
            terminal_view.print_result(result, label)

        elif choice == "0":
            terminal_view.print_result("", "You are going back to the main menu")

        else:
            terminal_view.print_error_message("There is no such choice.")
