import os
from PIL import Image
from tqdm import tqdm

quality = int(input("Enter the quality of the converted images (in percentage, from 10 to 100): "))

# Get the current working directory
cwd = os.getcwd()

# Create the output directory if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")

# Get a list of all the files in the directory
files = os.listdir(cwd)

# Loop through the list of files
for file in tqdm(files, "Saving images"):
    # Check if the file is an image
    if file.endswith(".jpg") or file.endswith(".png"):
        # Open the image
        image = Image.open(file)
        
        # Remove any leading zeros from the file name
        filename = file.lstrip("0")
        
        # Save the image in the output directory with the modified file name and in webp format
        image.save("output/" + filename.split(".")[0] + ".webp", "webp", quality=quality)
