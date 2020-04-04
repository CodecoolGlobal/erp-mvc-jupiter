from model.sales import sales
from view import terminal_view
from model import data_manager

def run():

    options = ["Add a new transaction",
               "Filter transactions by the employee",
               "Filter transactions by the customer",
               "Get the sales of games by a manufacturer",
               "Get age of a game by its title",
               "Get the most earning employee",
               "Get a ranking of sold items per manufacturer",
               "Get a ranking of sold items and earned money",
               ]


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
        print(table)
        
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
            pass

        elif choice == "4":
            pass

        elif choice == "5":
            pass

        elif choice == "6":
           pass

        elif choice == "7":
            pass

        elif choice == "8":
             pass

        elif choice == "0":
            terminal_view.print_result("", "You are going back to the main menu")

        else:
            terminal_view.print_error_message("There is no such choice.")