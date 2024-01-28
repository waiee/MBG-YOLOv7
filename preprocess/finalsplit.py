import os
import shutil

# Set the path to the original train folder
original_train_folder = "path/to/original/train"

# Set the paths to the destination folders
destination_images_folder = "path/to/destination/images"
destination_labels_folder = "path/to/destination/labels"

# Create images/train and labels/train directories if they don't exist
os.makedirs(os.path.join(destination_images_folder, "train"), exist_ok=True)
os.makedirs(os.path.join(destination_labels_folder, "train"), exist_ok=True)

# Get the list of files in the original train folder
train_files = os.listdir(original_train_folder)

# Iterate through each file in the original train folder
for file in train_files:
    # Construct the source path
    source_path = os.path.join(original_train_folder, file)

    # Construct the destination paths for images and labels
    destination_images_path = os.path.join(destination_images_folder, "train", file)
    destination_labels_path = os.path.join(destination_labels_folder, "train", file)

    # Check if the file is an image (you may need to adjust the condition based on your file types)
    if file.endswith((".jpg", ".jpeg", ".png")):
        # Copy the image file to the images/train folder
        shutil.copy(source_path, destination_images_path)
    elif file.endswith(".txt"):
        # Copy the label file to the labels/train folder
        shutil.copy(source_path, destination_labels_path)

print("Copying and pasting completed.")