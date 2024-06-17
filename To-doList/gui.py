import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("Black")
label0 = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button(size=10, image_source="add.png", mouseover_colors="DarkGrey",
                       tooltip="Add todo", key="Add")
listbox = sg.Listbox(values=functions.get_todos(), key='todos',
                     enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(size=10, image_source='complete.png',
                            mouseover_colors="DarkGrey", key="Complete",
                            tooltip="Complete")
exit_button = sg.Button("Exit")

window = sg.Window(title='The ToDo App',
                   layout=[[label0],
                           [label], [input_box, add_button],
                           [listbox, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))

while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select a todo first.", font=("Helvetica", 10))
        case "todos":
            window['todo'].update(value=value['todos'][0])
        case "Complete":
            try:
                completed_todo = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(completed_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select a todo first.", font=("Helvetica", 10))
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
window.close()
