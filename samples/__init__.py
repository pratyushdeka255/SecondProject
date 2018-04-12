import os
from string import digits

"""
Project- A directory have images with their names encrypted by putting numbers in front of them. if we remove the
numbers from the file name then the files will be arranged in a order to give you the actual message.

"""
def rename_file():
    #file_name = os.listdir("C:\\Users\\HP\\Downloads\\prank")
    file_names = os.listdir(r"C:\Users\HP\Downloads\prank")
    print(file_names)

    current_working_directory = os.getcwd()
    print(current_working_directory)
    os.chdir(r"C:\Users\HP\Downloads\prank")
    current_working_directory = os.getcwd()
    print(current_working_directory)

    #os.rename("2chennai.jpg","chennai.jpg")
    for filename in file_names:
        os.rename(filename, filename.translate((str.maketrans('', '', "0123456789"))))
    new_file_list = os.listdir(r"C:\Users\HP\Downloads\prank")
    print(new_file_list)

rename_file()

#these are new codes
