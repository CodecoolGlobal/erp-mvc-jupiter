from model.sales import sales
from view import terminal_view


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
    table = sales.get_table()


    choice = None

    while choice != "0":
        choice = terminal_view.get_choice_store(welcome, options)
        
        if choice == "1":
           pass

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