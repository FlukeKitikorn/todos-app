import streamlit as st
import function

st.title("To do app") #h1
st.subheader("This is my first to do app")
st.write("This app can add, edit, delete todo")

st.info("Python code of create app")
st.warning('Python code of create app')
st.error('Python code of create app')

todos = function.get_todos()

# def add_todos(todo):
#     todos = get_todos()
    
#     todos.append(todo.title())

#     write_todos(todos)

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo.title())
    function.write_todos(todos)


for index, i in enumerate(todos):
    st.checkbox(f"{index + 1} - {i}", key = i)
    st.write(st.state)
    if st.session_state[index] == True:
        # todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
function.write_todos(todos)

st.text_input(label = "", 
            placeholder = "Enter new todo",
            on_change = add_todo,
            key = "new_todo")

st.session_state