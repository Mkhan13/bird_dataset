'''
Script to rename and renumber the images in each bird folder
'''
import os

folders = {
    './starling': 'starling',
    './grackle': 'grackle',
    './blackbird': 'blackbird',
    './cowbird': 'cowbird'
}

def get_next_available_name(folder_path, bird, count):
    '''Function to find the next available file name by checking for conflicts'''
    new_name = f"{bird}_{count}.jpg"
    new_file = os.path.join(folder_path, new_name)
    
    while os.path.exists(new_file):
        count += 1  #Increment count until a non-conflicting name is found
        new_name = f"{bird}_{count}.jpg"
        new_file = os.path.join(folder_path, new_name)
    return new_name

def rename_files_in_folder(folder_path, bird):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]  #Get a list of all files in the directory
    files.sort()
    
    start_count = 1 #Start counting from 1 for each folder

    for count, filename in enumerate(files, start=start_count):
        new_name = get_next_available_name(folder_path, bird, count)  #Create new file name

        #Get the full path of the current file and the new file
        old_file = os.path.join(folder_path, filename.strip())  #Strip spaces from the old file name
        new_file = os.path.join(folder_path, new_name)
        
        os.rename(old_file, new_file)  #Rename the file
        print(f"Renamed '{filename}' to '{new_name}'")

#Loop through each folder and rename files
for folder_path, bird in folders.items():
    rename_files_in_folder(folder_path, bird)
