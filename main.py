from functions import get_todos, update_todos

while True:
    user_input = input("Enter your choice (Add, Edit, Complete, Show, Exit): ")
    user_input = user_input.capitalize()

    match user_input:
        case "Add":
            new_todo = input("Enter new todo: ")
            todos = get_todos()
            todos.append(new_todo.capitalize() + "\n")
            update_todos(todos)
        case "Edit":
            edit_index = int(input("Enter index of item to edit: "))
            new_value = input("Enter new To-DO: ")
            todos = get_todos()
            todos[edit_index - 1] = new_value.capitalize() + "\n"
            update_todos(todos)
        case "Complete":
            completed_index = int(input("Enter index of completed item: "))
            todos = get_todos()
            todos.pop(completed_index - 1)
            update_todos(todos)
        case "Show":
            todos_list = get_todos()
            for j, i in enumerate(todos_list):
                i = i.strip("\n")
                print(f"{j + 1}-{i}")
        case "Exit":
            exit()





