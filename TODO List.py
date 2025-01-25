#from Functions import get_todos,write_todos
import Functions as f
import time

now=time.strftime("%b %d,%Y %H:%M:%S")
print(now)
while True:
    user_action=input("Enter add,show,edit or exit....").strip()
    if user_action.startswith("add"):
        todo=user_action[4:]
        todos=f.get_todos()
        todos.append(todo+"\n")
        f.write_todos(todos)
    elif user_action.startswith("show"):
        todos=f.get_todos()
        new_todos=[i.strip("\n") for i in todos]
        for i,j in enumerate(new_todos):
            row=f"{i+1}-{j}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            loc=int(user_action[5:])
            new=input("Enter new todo: ")
            todos[loc-1]=new+"\n"
            f.write_todos(todos)
            print("The TODOS list has been changed")
            print("The new list is ")
            todos=f.get_todos()
            new_todos=[i.strip("\n") for i in todos]
            for i,j in enumerate(new_todos):
                row=f"{i+1}-{j}"
                print(row)
        except ValueError:
            print("Invalid Command")
            continue
    elif user_action.startswith("complete"):
        try:
            num=int(user_action[9:])
            todo_to_remove=todos[num-1].strip("\n")
            todos.pop(num-1)
            f.write_todos(todos)
            message=f"The Todo {todo_to_remove} was removed from the list"
            print(message)
        except ValueError:
            print("Invalid Command")
            continue
        except IndexError:
            print("There is no todo with that number")
            continue
    elif "exit" in user_action:
        break
    else:
        print("Invalid Command given")
print("Thank you for Using our APP")