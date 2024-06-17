import functions
while True:
    user_input = input("Type add or show or edit or complete or exit:\t")
    user_input = user_input.strip()

    todos = functions.get_todos()

    if user_input.startswith('add'):
        todo = user_input[4:] + "\n"
        todos.append(todo)

        functions.write_todos(local_todos=todos)

    elif user_input.startswith('show'):
        print("TO-DO's are:")
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f"{index+1}. {item}")

    elif user_input.startswith('edit'):
        if len(todos) == 0:
            print("There are no todos to edit!")
        else:
            try:
                number = int(user_input[4:])
                if number-1 > len(user_input):
                    print(f"todo number {number} doesn't exist, enter a valid todo")
                else:
                    change = input("Enter the todo to replace it:\t")
                    todos[number-1] = change + "\n"

                functions.write_todos(local_todos=todos)
            except ValueError:
                print("Invalid command!")
                continue

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[8:])
            if number-1 >= len(todos):
                print(f"todo number {number} doesn't exist, enter a valid todo")
            else:
                removed_todo = todos[number-1].strip('\n')
                print(f"{removed_todo} is removed from the to-do list!")
                todos.pop(number-1)

            functions.write_todos(local_todos=todos)

        except ValueError:
            print("Enter a number not the todo")

    elif user_input.startswith('exit'):
        break

    else:
        print("Type an valid prompt")

print("Buh bye!!")
