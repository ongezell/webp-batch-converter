import os
from PIL import Image
from tqdm import tqdm

quality = int(input("Enter the quality of the converted images (in percentage, from 10 to 100): "))
cwd = os.getcwd()
if not os.path.exists("output"):
    os.makedirs("output")
files = os.listdir(cwd)
for file in tqdm(files, "Saving images"):
  
    if file.endswith(".jpg") or file.endswith(".png"):
        
        image = Image.open(file)
                
        filename = file.lstrip("0")
        
        image.save("output/" + filename.split(".")[0] + ".webp", "webp", quality=quality)
