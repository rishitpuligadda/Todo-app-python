def get_todos(filename='todos.txt'):
    """Reads the text file and returns the elements
    in the file.
    """
    with open(filename, 'r') as local_file:
        """Writes the elements in the text file."""
        local_todos = local_file.readlines()
    return local_todos


def write_todos(local_todos, filename='todos.txt'):
    with open(filename, 'w') as local_file:
        local_file.writelines(local_todos)