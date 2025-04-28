def get_todos(file_path='todos.txt'):
    with open(file_path,'r') as file:
        todos_local = file.readlines()
    return todos_local
