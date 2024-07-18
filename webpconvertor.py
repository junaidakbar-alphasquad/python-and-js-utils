import os
from PIL import Image

def convert_images_to_webp(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        input_image_path = os.path.join(input_dir, filename)
        if os.path.isfile(input_image_path):
            # Open the image file
            with Image.open(input_image_path) as img:
                # Get the file name without extension
                file_name = os.path.splitext(filename)[0]
                # Define the output path with .webp extension
                output_image_path = os.path.join(output_dir, f"{file_name}.webp")
                # Convert and save the image to WebP format
                img.save(output_image_path, 'webp', quality=100)
                print(f"Converted {input_image_path} to {output_image_path}")

# Example usage
input_directory = './images'  # Replace with your input directory
output_directory = './webp_images'  # Replace with your desired output directory
convert_images_to_webp(input_directory, output_directory)
