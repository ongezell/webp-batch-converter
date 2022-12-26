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

## Adding Support for More File Types

If you want to add support for more file types to the script, you can modify the following line of code:

'if file.endswith(".jpg") or file.endswith(".png"):'


This line of code checks if the file is a `.jpg` or `.png` image. To add support for more file types, you can add additional conditions to this line of code using the `or` operator. For example, to add support for `.gif` and `.bmp` file types, you can modify the line of code like this:

'if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".bmp"):'


You can add as many file types as you want by separating them with the `or` operator. Just make sure to include the dot (`.`) before the file extension.

Note that this will only modify the file types that the script will consider when converting images. To actually save the images in the desired format, you will also need to modify the line of code that saves the images in the `output` directory:

'image.save("output/" + filename.split(".")[0] + ".webp", "webp", quality=quality)'

To save the images in a different format, you will need to change the file extension and the format parameter in the `save` function. For example, to save the images in `.gif` format, you can modify the line of code like this:

'image.save("output/" + filename.split(".")[0] + ".gif", "gif", quality=quality)'



