# everything you'll need is imported:
from view import terminal_view
from model.hr import hr

TABLE = hr.get_table('model/hr/persons.csv')

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    
    options = ["Get oldest person",
              "Get person closest to average salary",
              "Get shortest surname", 
              "Get age by surname",
              "Get email by surname",
              "Get first name by surname",
              "Return to main menu"]

    choice = None

    while choice != "7":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            label = "The oldest person: "
            result = hr.get_oldest_person(TABLE)
            terminal_view.print_result(result, label)

        elif choice == "2":
            label = "Person with salary closest to average: "
            result = hr.get_persons_closest_to_average_salary(TABLE)
            terminal_view.print_result(result, label)

        elif choice == "3":
            label = "Person with the shortest surname: "
            result = hr.get_shortest_surname(TABLE)
            terminal_view.print_result(result, label)

        elif choice == "4":
            surname = terminal_view.get_inputs(["Surname: "], "Provide workers surname")
            label = "Age of this worker is:"
            result = hr.get_age_by(surname, TABLE)
            terminal_view.print_result(result, label)

        elif choice == "5":
            surname = terminal_view.get_inputs(["Surname: "], "Provide workers surname")
            label = "Email of this worker is:"
            result = hr.get_email_by(surname, TABLE)
            terminal_view.print_result(result, label)

        elif choice == "6":
            surname = terminal_view.get_inputs(["Surname: "], "Provide workers surname")
            label = "Firstname of this worker is:"
            result = hr.get_first_name_by(surname, TABLE)
            terminal_view.print_result(result, label)

        elif choice == "7":
            terminal_view.print_result("Returning to main menu", "")

        elif choice == "0":
            terminal_view.print_result("", "Goodbye")
            quit()

        else:
            terminal_view.print_error_message("There is no such choice.")

  