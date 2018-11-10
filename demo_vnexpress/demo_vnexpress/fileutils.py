import os

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        return True
    else: 
        return False

def create_file_to_write(folder_path, file_name, mode='w'):
    if not os.path.exists(folder_path):
        create_folder(folder_path)
    
    file_path = folder_path + '/' + file_name
    file = open(file_path, mode)
    return file
