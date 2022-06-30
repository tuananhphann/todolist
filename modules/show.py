import os
from modules.encrypt import decrypt

def maxLengthofLines(home_path, work_file, index):
    """
    Check for longest line in list of tasks or note based on index
    Returns:
    max (int): length of longest line
    """
    max = 0
    with open(f"{home_path}\{work_file}","r",encoding="utf-8") as f:
        for line in f:
            line = line.split(",")
            if (len(line[index]) > max):
                max = len(line[index])

    return max


def showToDo(home_path, work_file):
    """
    Show all of tasks in ToDoList
    """
    first_space = 10
    second_space = maxLengthofLines(home_path, work_file, 0) + 5
    third_space = maxLengthofLines(home_path, work_file, 1) + 5

    # os.system("cls")
    print(f"Content of '{work_file.split('.')[0]}'")

    print((len("Number" + " "*(first_space - 6) + "Task" + " "*(second_space - 4) + "Note" + " "*(third_space - 4) + "Added time")) * "-") # print -----
    print("Number" + " "*(first_space - 6) + "Task" + " "*(second_space - 4) + "Note" + " "*(third_space - 4) + "Added time") # print header
    print((len("Number" + " "*(first_space - 6) + "Task" + " "*(second_space - 4) + "Note" + " "*(third_space - 4) + "Added time")) * "-") # print -----

    i = 1
    with open(f"{home_path}\{work_file}","r",encoding="utf-8") as f:
        for line in f:
            line = line.split(",")
            # decrypt data and print it
            print(str(i) + " "*(first_space-len(str(i))) + decrypt(line[0], len(line[0])) + " "*(second_space-len(line[0])) + decrypt(line[1], len(line[1])) + " "*(third_space-len(line[1])) + line[2], end = "")
            i+=1

    print((len("Number" + " "*(first_space - 6) + "Task" + " "*(second_space - 4) + "Note" + " "*(third_space - 4) + "Added time")) * "-") # print -----

def showAllToDo(home_path):
    """
    Show all of tasks in all of ToDoLists
    """
    os.system("cls")
    file_list = os.listdir(home_path)
    for file in file_list:
        showToDo(home_path, file)
        print('\n')