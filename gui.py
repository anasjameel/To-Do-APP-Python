import functions
import PySimpleGUI as sg

label1 = sg.Text("Enter To-Do Item")
user_input = sg.Input(key="todo")
add_button = sg.Button("Add")
listbox = sg.Listbox(values=functions.get_todos(), tooltip="ToDo Items", size=[45,10], enable_events=True, key="listbox")
edit_btn = sg.Button("Edit")
complete_btn = sg.Button("Complete")
window = sg.Window("To-Do App", layout=[[label1], [user_input, add_button],[listbox, edit_btn, complete_btn]], font=("Verdana", 16))

while True:
    event, value = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(value['todo'] + "\n")
            print(todos)
            functions.update_todos(todos)
            window['listbox'].update(values=todos)
        case 'Edit':
            try:
                new_value = value['todo']
                value_to_be_edited = value["listbox"][0]
                todos = functions.get_todos()
                index = todos.index(value_to_be_edited)
                todos[index] = new_value + "\n"
                functions.update_todos(todos)
                window['listbox'].update(values=todos)
                print(todos)
            except IndexError:
                sg.popup('Select item to edit', keep_on_top=True, font=("Verdana", 16))
        case 'listbox':
            window['todo'].update(value['listbox'][0].strip("\n"))
        case 'Complete':
            try:
                todos = functions.get_todos()
                index = todos.index(value["listbox"][0])
                todos.pop(index)
                functions.update_todos(todos)
                window['listbox'].update(values=todos)
            except IndexError:
                sg.popup('Select item to complete', keep_on_top=True, font=("Verdana", 16))
        case sg.WIN_CLOSED:
            exit()