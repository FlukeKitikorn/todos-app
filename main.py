import function
from function import get_todos
from function import write_todos

todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = input("Enter a todo: ") + "\n"
        todo = user_action[4:] + "\n"

        todos = get_todos()

        # print(todos)
        todos.append(todo.title())
        # print(todos)

        write_todos(todos)

    elif 'show' in user_action:
            
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif 'edit' in user_action:
        try:
            number = int(user_action[5:])
            number = int(number) - 1

            with open('todos.txt','r') as file:
                todos = file.readlines() 

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo.title() + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos) 
        except ValueError:
            print("Your command is not valid.")
            continue       

    elif 'complete' in user_action:
        number = int(user_action[9:])
        index = int(number) - 1

        todos = get_todos()

        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        write_todos(todos)

        message = f"Todo {todo_to_remove} was removed from the list." 
        print(message)


    elif 'exit' in user_action:
        break

    else:
        print("Command is not valid")
        
print('Bye!')
