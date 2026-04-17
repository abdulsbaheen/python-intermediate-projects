import os 
import shutil

folder_path = "downloads"

file_type = {
    "images": [".jpg",".png",".jpeg"],
    "documents" :[".pdf","docx",".txt"],
    "videos": [".mp4",".avi",".mkv"],
    "music": [".mp3",".wav",".aac"]
}

# make the folder 
def create_folders():
   for folder in file_type.keys():
       path = os.path.join (folder_path, folder)
       if not os.path.exists(path):
           os.mkdir(path)
    # others files
   others_path = os.path.join(folder_path, "others")
   if not os.path.exists(others_path):
       os.mkdir(others_path)
       
# get a file category
def get_category(extension):
    for category, extensions in file_type.items():
        if extension.lower() in extensions:
            return category
    return "others"

#organize files
def organize_files():
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        if os.path.isdir(file_path):
            continue
        
        _,extension = os.path.splitext(file)
        
        category = get_category(extension)
        
        dest_path = os.path.join(folder_path, category)
        
        try:
            shutil.move(file_path, dest_path)
            print(f"Moved: {file} to {category}")
        except Exception as e:
            print(f"Error occurred while moving {file}: {e}")
            
print("🗂 File Organizer Started...")

create_folders()
organize_files()

print("✅ Files Organized Successfully!")         