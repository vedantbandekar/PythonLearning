#Python writing files (.txt, .json, .csv)

txt_data = "I love bikes!"

file_path = "output.txt" #for relative file path
#file_path = "C:/Users/VEDANT/OneDrive/Desktop/output.txt" #for absolute

# w = write
# x = also write if doesnt exist if exist error
# a = append a file
#r = read

# with open(file=file_path, mode="w") as file:  #open = func will return file object 
#     file.write(txt_data)                      #with = will open file as well as close it after done
#     print(f"Text file '{file_path}' was created")

# try:
#     with open(file=file_path, mode="x") as file:   
#         file.write(txt_data)                     
#         print(f"Text file '{file_path}' was created")
# except FileExistsError:
#     print(f"File '{file_path}' already exists")

try:
    with open(file=file_path, mode="a") as file:   #appends data into file (w will overwrite the file)
        file.write("\n" + txt_data)                     
        print(f"Text file '{file_path}' was created")
except FileExistsError:
    print(f"File '{file_path}' already exists")