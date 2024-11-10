'''
This script iterates through each image in the bird folders and renames them following the image_#.jpg scheme for uniformity.
Then each image is renamed following the [bird]_#.jpg scheme. The day is to ensure the rename is processed and displayed before moving on to the next name.
'''
import os
import time

folders = {
    './starling': 'starling',
    './grackle': 'grackle',
    './blackbird': 'blackbird',
    './cowbird': 'cowbird'
}
def rename_to_numbers(folder_path):
    #Rename files to a simple sequence
    existing_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for count, filename in enumerate(existing_files, start=1):
        #Create a new name based on the count
        new_name = f"images_{count}.jpg" #If encountering renaming issues, replace with any word before the count, such as "something_else_goes_here_{count}.jpg" and run script again

        #Get the full paths for old and new file names
        old_file = os.path.join(folder_path, filename.strip())
        new_file = os.path.join(folder_path, new_name)

        os.rename(old_file, new_file) #Rename the files
        time.sleep(0.5)  #Add a delay of 0.5 seconds between renames
        print(f"Renamed '{filename}' to '{new_name}'")

def rename_to_birds(folder_path, bird):
    #Rename the numbered files to the bird name format
    numbered_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for count, filename in enumerate(numbered_files, start=1):
        #Create a new name with the corresponding bird
        bird_new_name = f"{bird}_{count}.jpg"

        #Get the full paths for old and new file names
        old_file = os.path.join(folder_path, filename.strip())
        new_file = os.path.join(folder_path, bird_new_name)

        #Rename the file to include the bird name
        os.rename(old_file, new_file)
        time.sleep(0.75)  #Add a delay of 1 second between renames
        print(f"Renamed '{filename}' to '{bird_new_name}'")

#Loop through each folder and rename files
for folder_path, bird in folders.items():
    rename_to_numbers(folder_path)
    rename_to_birds(folder_path, bird)