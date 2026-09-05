#Python file detection

import os #Helps interact with operating system (Its is  module)

file_path = "test.txt" #if put pdf than wont work (Relative file path)
#file_path = "foldername/test.txt" #in same path ish (Relative file path)
#file_path = "C:/Users/HP/Desktop/test.txt" (Absolute file path)

if os.path.exists(file_path): #Returns boolen value if file exists or not
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path): #Here the file path will be .txt .pdf .doc etc
        print("This is a file") 
    elif os.path.isdict(file_path): #Since directory (Folder) no .txt .pdf etc
        print("It is a directory")
else:
    print("File location does not exist")

# print(os.getcwd()) #Shows path of file
# print(os.path.exists("test.txt"))