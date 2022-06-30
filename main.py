import os, time, datetime
from modules.createFile import initFile, checkEmptyFile
from modules.delete import *
from modules.update import *
from modules.show import *
from modules.encrypt import *


def home(home_path, version, default_file):
    work_file = default_file
    while True:
        os.system("cls")
        # print(f"Current file '{work_file}'")
        print("TASK MASTER")
        showToDo(home_path, work_file)

        choice = input(f"""
Navigation:
    Press 1 to add
    Press 2 to delete
    Press 3 to show all contents of ToDoList
    Press 4 to update 
    Press 5 to create and change to do list
    Press 6 to change to do list
    Press 7 to delete to do list
    Press E to exit
Your choice: """)
        if choice == "1":
            while True:
                os.system("cls")
                print("Press !q to exit this mode.")
                showToDo(home_path, work_file)
                task = input("Task: ")
                if task == "!q": break
                note = input("Note: ")
                added = datetime.datetime.now().date()
                addToDo(home_path, work_file, task, note, added)

        elif choice == "2":
            if not checkEmptyFile(home_path, work_file):
                try:
                    index = int(input("Number of task you want to delete: "))
                    deleteToDo(home_path, work_file, index-1) # because index in list start from 0
                    print("Delete successfully!")
                except:
                    print("That task is not exists!")
            else:
                print("There are nothing in to do list!")

        elif choice == "3":
            showAllToDo(home_path)

        elif choice == "4":
            if not checkEmptyFile(home_path, work_file):
                try:
                    index = int(input("Number of task you want to update: "))
                    task = input("New task: ")
                    note = input("New note: ")
                    time = datetime.datetime.now().date()
                    updateToDo(home_path, work_file, task, note, time, index)
                    print("Update successfully!")
                except:
                    print("That task is not exists!")
            else:
                print("There are nothing in to do list!")
            

        elif choice == "5":
            new_work_file = input("Name of new to do list: ")+".txt"
            try:
                initFile(home_path, new_work_file)
                work_file = new_work_file
                print("Created successfully!")
            except:
                work_file = new_work_file
                print("There was an issue creating a new list!")

        elif choice == "6":
            pre_work_file = work_file
            work_file = changeToDoList(home_path)
            if work_file == -1: work_file = pre_work_file

        elif choice == "7":
            work_file = removeFile(home_path)

        elif choice.upper() == "E":
            break

        else:
            print("Your choice is not exists.")

        input("Press Enter to continue.")



def main():
    # get this file's dir
    full_path = (os.path.realpath(__file__))
    file_path = os.path.dirname(full_path)

    # home_path = os.path.expanduser('~')+r"\OneDrive - tuananhph\todolist"
    home_path = file_path+r"\data"

    version = "1.0.0"
    default_file = "default.txt"

    # init default data file if it not exist
    initFile(home_path, default_file)
    
    print("Starting program...")
    time.sleep(0.2)

    # UI
    home(home_path, version, default_file)


if __name__ == "__main__":
    main()