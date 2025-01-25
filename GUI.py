import FreeSimpleGUI as fsg
import Functions

label=fsg.Text("Type in your To-Do")
input_box=fsg.InputText(tooltip="Enter To-do",key="todo")
add_button=fsg.Button("Add")
list_box=fsg.Listbox(values=Functions.get_todos(),size=(40,10),
                      key="todos",enable_events=True)
edit_button=fsg.Button("Edit")


window=fsg.Window("My To-Do APP",
                  layout=[[label],[input_box,add_button],
                  [list_box,edit_button]],
                  font=("Helvetica",20))
while True:
    event,values=window.read()
    match event:
        case "Add":
            todos=Functions.get_todos()
            new_todo=values["todo"]+"\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
        case "Edit":
            todo_to_edit=values["todos"]
            new_todo=values["todo"]+"\n"
            todos=Functions.get_todos()
            index=todos.index(todo_to_edit)
        case fsg.WIN_CLOSED:
            break
window.close()