""" Terminal view module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    row_width = []
    for width in title_list:
        row_width.append(len(width))
    for line in range(0, len(table)):
        for index in range(0, len(table[line])):
            if len(table[line][index]) > row_width[index]:
                row_width[index] = len(table[line][index])

    table_lenght = 0
    for index in range(0, len(row_width)):
        row_width[index] += 2
        table_lenght += row_width[index]

    print("/" + "-" * (table_lenght+len(title_list)-1) + "\\")

    for i in range(0, len(title_list)):
        temp = round((row_width[i] - len(title_list[i]))/2)
        print("|" + " " * temp + title_list[i] + " " * (row_width[i] - (temp + len(title_list[i]))), end='')
    print("|")

    for line in range(0, len(table)):
        for width in row_width:
            print("|" + "-" * width, end='')
        print("|")
        for index in range(0, len(table[line])):
            temp = round((row_width[index] - len(table[line][index]))/2)
            print("|" + " " * temp + table[line][index] + " " * (row_width[index]-temp-len(table[line][index])), end='')
        print("|")

    print("\\" + "-" * (table_lenght+len(title_list)-1) + "/")

    input("Please insert anything to continue:")


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    if isinstance(result, list):
        print(label)
        for element in result:
            print(element, end=' | ')
    elif isinstance(result, dict):
        print(label)
        for key in result:
            print(key, ":", result[key])
    else:
        print(label, result)


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    order_number = 1
    print(title)
    for option in list_options:
        print("     (" + str(order_number) + ") ", option)
        order_number += 1
    print("     (0) ", exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    for label in list_labels:
        user_input = input(label)
        inputs.append(user_input)
    return inputs


def get_choice(options):
    print_menu("Main menu", options, "Exit program")
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]


def get_choice_store(welcome, options):
    print_menu(welcome, options, "Go back to the main menu")
    inputs = get_inputs(["Please choose your function: "], "")
    return inputs[0]


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print("Error: " + message)
