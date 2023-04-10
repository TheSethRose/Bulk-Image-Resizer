from PIL import Image
import os

# Configuration Variables
# Set the path to the folder containing the images you want to resize
path = "/Users/Username/Documents/Pictures"  # Replace with your desired path

# Set the target size for the images in inches (width x height)
size = {'width': 8, 'height': 10}  # Example: 8x10 inches, a standard photo size

folder_path = path
# Create an output folder path within the input folder to save the resized images
output_folder_path = os.path.join(folder_path, 'output')
# Calculate the max size of the images in pixels, assuming 300 DPI
max_size = {'width': size['width'] * 300, 'height': size['height'] * 300}  # Assuming 300 DPI

def resize_image(input_image_path, output_image_path, max_size):
    """
    Resizes an image while maintaining its aspect ratio.
    
    Args:
        input_image_path (str): The path to the input image file.
        output_image_path (str): The path where the resized image will be saved.
        max_size (dict): The maximum width and height of the resized image in pixels.
    """
    with Image.open(input_image_path) as image:
        width, height = image.size
        aspect_ratio = width / height

        # Determine new dimensions based on the aspect ratio
        if width > height:
            new_width = min(max_size['width'], width)
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = min(max_size['height'], height)
            new_width = int(new_height * aspect_ratio)

        # Resize the image and save it
        image = image.resize((new_width, new_height), Image.LANCZOS)
        image.save(output_image_path)

def bulk_resize_images(folder_path, output_folder_path, max_size):
    """
    Resizes all images in a folder and saves them in an output folder.
    
    Args:
        folder_path (str): The path to the folder containing the images to resize.
        output_folder_path (str): The path to the folder where the resized images will be saved.
        max_size (dict): The maximum width and height of the resized images in pixels.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # Iterate through all the images in the folder and resize them
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            input_image_path = os.path.join(folder_path, filename)
            output_image_path = os.path.join(output_folder_path, filename)
            print(f"Resizing {filename}")
            resize_image(input_image_path, output_image_path, max_size)

# Call the bulk_resize_images function to resize all images in the folder
bulk_resize_images(folder_path, output_folder_path, max_size)
print("All images have been resized and saved in the 'output' folder.")
