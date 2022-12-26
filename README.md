# webp-batch-converter

This script converts all .jpg and .png images in the current working directory to .webp format and saves them in an output directory. The user can specify the quality of the converted images, which should be entered as a percentage between 10 and 100.

Dependencies:
- os: for interacting with the operating system, such as creating directories and getting the current working directory
- PIL (Python Imaging Library): for opening and saving image files
- tqdm: for displaying a progress bar while converting the images

Usage:
To use this script, run the following command in the terminal:
    python script.py
The user will be prompted to enter the quality of the converted images. After entering the quality, the script will start converting the images and will display a progress bar showing the progress. When the script is finished, the converted images will be saved in the output directory.

Notes:
- The script will only convert .jpg and .png images in the current working directory. If there are other types of files in the directory, they will be ignored.
- The script will remove any leading zeros from the file names of the converted images before saving them in the output directory.
- If the output directory does not exist, the script will create it.


