import os

def get_files_info(working_directory, directory=None):

    abs_working_directory = os.path.abspath(working_directory)
    target_directory = abs_working_directory

    if directory:
        target_directory = os.path.abspath(os.path.join(abs_working_directory, directory))
        

print(get_files_info("calculator", "."))
print(os.path.abspath("test/test.txt"))