# everything you'll need is imported:
from view import terminal_view
from controller import store_controller
from controller import hr_controller
from controller import crm_controller
from controller import sales_controller


def run():
    options = ["Store manager",
               "Human resources manager",
               "Customer Relationship Management (CRM)",
               "Sales manager"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            store_controller.run()
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            crm_controller.run()
        elif choice =="4":
            sales_controller.run()
        elif choice == "0":
            terminal_view.print_result("", "Goodbye")
        else:
            terminal_view.print_error_message("There is no such choice.")