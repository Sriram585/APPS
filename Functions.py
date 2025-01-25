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