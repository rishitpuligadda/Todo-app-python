import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
listbox = sg.Listbox(values=functions.get_todos(), key='todos',
                     enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window(title='The ToDo App',
                   layout=[[label], [input_box, add_button],
                           [listbox, edit_button]],
                   font=('Helvetica', 12))

while True:
    event, value = window.read()
    print(event)
    print(value)
    #window['todo'].update(value="")
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = value['todos'][0]
            new_todo = value['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=value['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()
