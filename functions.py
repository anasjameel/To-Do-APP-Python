FILE_PATH = "data/todo.txt"


def get_todos(filepath=FILE_PATH):
    """Returns list of To-Do List"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos


def update_todos(new_value, filepath=FILE_PATH):
    """Updates the todo list"""
    with open(filepath, 'w') as file:
        file.writelines(new_value)
