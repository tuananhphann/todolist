import os

def removeFile(home_path):
    """
    Remove a ToDoList based on its index
    Return -1 if that file does not exists
    """
    file_list = os.listdir(home_path)

    # If only one file
    if len(file_list) == 1:
        print("You can't delete more!")
        return file_list[0]
    
    # Print list of files
    i = 1
    for file in file_list:
        print(i, file)
        i+=1
    
    choice = int(input("Index of file you want to delete: "))
    try:
        os.remove(f"{home_path}\{file_list[choice - 1]}")
        print(f"Deleted!")
        file_list = os.listdir(home_path)
        return file_list[0]
    except:
        print("That work file is not exists.")
        return -1


def deleteToDo(home_path, work_file, index):
    """
    Delete a selected task in a ToDoList based on its index.
    """
    data = []
    with open(f"{home_path}\{work_file}","r",encoding="utf-8") as f:
        for line in f:
            data.append(line)
    
    data.pop(index)

    with open(f"{home_path}\{work_file}","w",encoding="utf-8") as f:
        for line in data:
            f.write(line)