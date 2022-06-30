import os, time

def checkFileExists(home_path, work_file):
    isExists = os.path.exists(f"{home_path}\{work_file}")
    return isExists


def checkEmptyFile(home_path, work_file):
    data = []
    with open(f"{home_path}\{work_file}","r",encoding="utf-8") as f:
        for line in f:
            data.append(line)

    if data == []:
        return True
    return False


def createFile(home_path, work_file):
    """
    Just create a file and dir
    """
    try:
        os.mkdir(f"{home_path}")
    except FileExistsError:
        print("This directory has been created.")
    f = open(f"{home_path}\{work_file}","w",encoding="utf-8")
    f.close()


def initFile(home_path, work_file):
    """
    Check if file exist or not and create file
    """
    if not checkFileExists(home_path, work_file):
        createFile(home_path, work_file)
        print(f"File created in {home_path}\{work_file}")
        time.sleep(0.2)
    else:
        print("File is already exists")
        time.sleep(0.2)