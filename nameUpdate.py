import os

# Set the directory where your files are located
directory = "./images"

# Loop over all files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    # Check if it's a file
    if os.path.isfile(file_path):
            new_name = filename.replace(" ","-").lower() # filename[:-4] + "1.png"
            new_path = os.path.join(directory, new_name)
            os.rename(file_path, new_path)
            # os.remove(file_path)