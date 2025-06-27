import os

def get_files_info(working_directory, directory=None):

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    working_directory_path = os.path.abspath(working_directory)
    directory_path = os.path.abspath(directory)
    print(working_directory_path)
    print(directory_path)
    if not directory_path.startswith(working_directory_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    os.listdir(directory_path)

print(get_files_info("calculator", "."))
print(os.path.abspath("test/test.txt"))