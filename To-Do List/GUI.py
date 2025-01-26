import FreeSimpleGUI as sg
import Functions
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")
clock = sg.Text(time.strftime("%b %d, %Y"), key="time")
label = sg.Text("Type in your To-Do")
input_box = sg.InputText(tooltip="Enter To-do", key="todo")
list_box = sg.Listbox(values=Functions.get_todos(), size=(40, 10),
                      key="todos", enable_events=True)

add_button = sg.Button("Add", size=(10, 1))
edit_button = sg.Button("Edit", size=(10, 1))
complete_button = sg.Button("Completed", size=(10, 1))
exit_button = sg.Button("Exit", size=(10, 1))

window = sg.Window("My To-Do APP",
                   layout=[[clock], [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

try:
    while True:
        event, values = window.read(timeout=100)
        window["time"].update(time.strftime("%b %d, %Y"))
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        if event == "Add":
            todos = Functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
            window["todos"].update(values=todos)
        elif event == "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = Functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                Functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first")
        elif event == "todos":
            window["todo"].update(value=values["todos"][0])
        elif event == "Completed":
            try:
                todos = Functions.get_todos()
                todo_to_complete = values["todos"][0]
                index = todos.index(todo_to_complete)
                todos.pop(index)
                Functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first")
finally:
    window.close()
print("Thank you for using our APP")