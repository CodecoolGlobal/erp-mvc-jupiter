def get_table_from_file(file_name):
    """
    Reads csv file and returns it as a list of lists.
    Lines are rows columns are separated by ","

    Args:
        file_name (str): name of file to read

    Returns:
         list: List of lists read from a file.
    """

    with open(file_name, "r") as file:
        lines = file.read().splitlines()

    list_of_lists = []
    for game in lines:
        splitted_score = game.split(", ")
        list_of_lists.append(splitted_score)
    
    return list_of_lists

def write_table_to_file(file_name, table):
    """
    Writes list of lists into a csv file.

    Args:
        file_name (str): name of file to write to
        table (list): list of lists to write to a file

    Returns:
         None
    """

    with open(file_name, "w") as export_file:
        export_file.write

    with open(file_name, "a") as export_file:
        for game in table:
            row = ", ".join(game)
            export_file.write(row + "\n")
