
import FreeSimpleGUI as fsg
import Functions

label=fsg.Text("Type in your To-Do")
input_box=fsg.InputText(tooltip="Enter To-do")
add_button=fsg.Button("ADD")


window=fsg.Window("My To-Do APP",layout=[[label,input_box],[add_button]])
window.read()
window.close()