import os
from modules.encrypt import encrypt

def isDuplicate(home_path, work_file, check_data):
    """
    Check if data duplicate in a file
    Returns:
    bool: 
    """
    data = []
    with open(f"{home_path}\{work_file}","r",encoding="utf-8") as f:
        for line in f:
            data.append(line)

    for item in data:
        if item == check_data:
            return True
    
    return False


def changeToDoList(home_path):
    """
    Change ToDoList based on index of that ToDoList's file
    Return -1 if that file does not exists.
    """
    file_list = os.listdir(home_path)
    i = 1
    for file in file_list:
        print(i, file.split(".")[0])
        i+=1
    choice = int(input("Index of file you want to change: "))
    try:
        return file_list[choice-1]
    except:
        print("That work file is not exists.")
        return -1


def addToDo(home_path, work_file, task: str, note: str, time):
    """
    Add new task.
    """
    
    # Check for requirements
    if task == "":
        print("Task can not be empty!")
        return
    if note == "": note = "None"

    data = f"{encrypt(task, len(task))},{encrypt(note, len(note))},{time}\n"

    if isDuplicate(home_path, work_file, data):
        print("This task is already exists.")
        return
    
    # Process of add new task
    f = open(f"{home_path}\{work_file}","a",encoding="utf-8")
    f.write(data)
    f.close()
    
    print("Added task successfully!")


def updateToDo(home_path, work_file, task, note, time, index):
    """
    Update a selected task in ToDoList.
    """

    # Check for requirements
    if task == "":
        print("Task can not be empty!")
        return
    if note == "": note = "None"

    data = f"{encrypt(task, len(task))},{encrypt(note, len(note))},{time}\n"

    if isDuplicate(home_path, work_file, data):
        print("This task is already exists.")
        return
    
    # Process of update
    tasks = []
    with open(f"{home_path}\{work_file}", "r", encoding='utf-8') as f:
        for line in f:
            tasks.append(line)

    tasks[index-1] = data

    with open(f"{home_path}\{work_file}", "w", encoding='utf-8') as f:
        for item in tasks:
            f.write(item)

