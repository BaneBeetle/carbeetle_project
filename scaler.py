# Brian Phan
# 84609992
# Downscale carbeetle images to 32x32!

import os
from PIL import Image # Using pillow to downscale!

def downscale(input_folder, output_folder):
    size = (64, 64)

    os.makedirs(output_folder, exist_ok=True) # If the folder doesnt exist, itll create it here too

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            try:
                with Image.open(input_path) as img:
                    # Resize / downscale here
                    img_resized = img.resize(size, Image.LANCZOS)
                    img_resized.save(output_path)
                    print(f"I just downscaled {filename}!")
            except Exception as e:
                print(f"ERROR ON {filename}: {e}")

def rename_files(input_folder, base_name):
    items = os.listdir(input_folder)
    files = [f for f in items if os.path.isfile(os.path.join(input_folder, f))]
    files.sort()

    for counter, filename in enumerate(files, start=1):
        _, ext = os.path.splitext(filename)
        new_filename = f"{base_name}{counter}{ext}"
        old_path = os.path.join(input_folder, filename)
        new_path = os.path.join(input_folder, new_filename)
        os.rename(old_path, new_path)


if __name__ == '__main__':

    #input_folder = "carbeetle" # INSERT YO FOLDER HERE
    #output_folder = "64_carbeetle" # PUT YO OUTPUT HERE
    #downscale(input_folder, output_folder)

    # rename_files("64_carbeetle", "carbeetle_") # I messed up the naming convention 
    pass

