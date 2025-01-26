import FreeSimpleGUI as fsg
import Functions
import time

fsg.theme("DarkPurple4")
clock=fsg.Text(time.strftime("%b %d,%Y %H:%M:%S"),key="time")
label=fsg.Text("Type in your To-Do")
input_box=fsg.InputText(tooltip="Enter To-do",key="todo")
list_box=fsg.Listbox(values=Functions.get_todos(),size=(40,10),
                      key="todos",enable_events=True)

add_button=fsg.Button("Add")
edit_button=fsg.Button("Edit")
complete_button=fsg.Button("complete")
exit_button=fsg.Button("Exit")


window=fsg.Window("My To-Do APP",
                  layout=[[clock],[label],[input_box,add_button],
                  [list_box,edit_button,complete_button],
                  [exit_button]],
                  font=("Helvetica",20))
try:
    while True:
        event,values=window.read(timeout=100)
        window["time"].update(time.strftime("%b %d,%Y %H:%M:%S"))
        match event:
            case "Add":
                todos=Functions.get_todos()
                new_todo=values["todo"]+"\n"
                todos.append(new_todo)
                Functions.write_todos(todos)
                window["todos"].update(values=todos)
            case "Edit":
                try:
                    todo_to_edit=values["todos"][0]
                    print(type(todo_to_edit))
                    new_todo=values["todo"]+"\n"
                    todos=Functions.get_todos()
                    print(todos)
                    index=todos.index(todo_to_edit)
                    todos[index]=new_todo
                    Functions.write_todos(todos)
                    window["todos"].update(values=todos)
                except IndexError:
                    fsg.popup("please select an item first")
            case "todos":
                window["todo"].update(value=values["todos"][0])
            case "complete":
                try:
                    todos=Functions.get_todos()
                    todo_to_complete=values["todos"][0]
                    index=todos.index(todo_to_complete)
                    todos.pop(index)
                    Functions.write_todos(todos)
                    window["todos"].update(values=todos)
                    window["todo"].update(value="")
                except IndexError:
                    fsg.popup("Please select an item first")
            case fsg.WIN_CLOSED:
                break
            case "Exit":
                break
finally:
    window.close()