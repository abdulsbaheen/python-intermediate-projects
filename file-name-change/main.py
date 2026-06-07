# this program is about how to chnage the file name 
import os 

# give the path of the folder where the files are located
path = r"E:\friends photos&videos\videos with friends"

list_of_files = os.listdir(path)

print(list_of_files)

files =["png","jpg","jpeg","pdf","docx","txt","mp4","avi","mkv","mp3","wav","aac"]


#  rename files  with new name and extenstion
def rename_files_ext():
    # user input for file type and the type to convert to
    user1 = input("Enter the file type you want to rename: ").lower()
    # user input for the type to convert to
    user2 = input("Enter the type you want to convert to: ").lower()
    # user enter the new file name
    new_name = input("Enter the new file name (without extension): ")
    
    if user1 in files:
        for i in range(len(list_of_files)):
          if list_of_files[i].endswith(user1):
              old_file = os.path.join(path, list_of_files[i])
              new_file = os.path.join(path, new_name + "_" + str(i) + "." + user2)
              os.rename(old_file, new_file)
    else:
        print("File type not found in the list.")


# rename_files()        
def  rename_files():
    user_name_change = input("Enter the new file name (without extension): ")
    for i in range(len(list_of_files)):
        old_file = os.path.join(path, list_of_files[i])
        file_name, file_ext = os.path.splitext(list_of_files[i])
        new_file = os.path.join(path, user_name_change + "_" + str(i) + file_ext)
        os.rename(old_file, new_file)     
        

print("1. Rename files with new name and extension")
print("2. Rename files with new name and same extension")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    rename_files_ext()
elif choice == "2":
    rename_files()
else:
    print("Invalid choice.")
    
 