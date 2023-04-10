# Bulk Image Resizer
Bulk Image Resizer is a Python script that allows you to resize multiple images in a folder while maintaining their aspect ratio. This is particularly useful when you have a collection of high-resolution images that you'd like to convert to a smaller size for web usage, sharing, or printing.

## Features
* Automatically resizes multiple images in a folder
* Maintains aspect ratio during the resizing process
* Supports various image formats, including JPEG, PNG, BMP, and GIF
* Allows you to specify a target size in inches

## Requirements
* Python 3.6 or later
* Pillow (Python Imaging Library)

## Installation
* Make sure you have Python 3.6 or later installed on your system. You can check your Python version by running python --version in your command prompt or terminal.
* Install Pillow (Python Imaging Library) by running the following command
```bash
pip install Pillow
```

## Usage
Download the bulk_image_resizer.py script from this repository.

Open the script in your favorite text editor and set the configuration variables:
* path: The path to the folder containing the images you want to resize.
* size: The target size for the images in inches (width x height).

Example:
```python
path = "/Users/Username/Documents/Pictures"  # Replace with your desired path
size = {'width': 8, 'height': 10}  # Example: 8x10 inches, a standard photo size
```
* Save the changes and close the text editor.

Run the script by executing the following command in your command prompt or terminal:
```bash
python3 bulk_image_resizer.py
```
The script will resize all images in the specified folder and save them in a new folder named 'output' within the original folder.
