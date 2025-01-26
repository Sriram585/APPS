FilePath="TODOS.txt"

def get_todos(filepath=FilePath):
    """Read a text file 
            and 
       return the todos list"""
    with open(filepath,"r") as file:
        todos_local=file.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FilePath):
    """Write the todo items list 
        to the text file"""
    with open("TODOS.txt","w") as file:
        file.writelines(todos_arg)

def search_index(todos_arg,todo_to_edit):
    """Search for the index of the todo item"""
    for index,todo in enumerate(todos_arg):
        if todo==todo_to_edit:
            return index
    return None