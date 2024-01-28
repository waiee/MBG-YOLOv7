# import os
# import shutil
# from sklearn.model_selection import train_test_split

# # Set the path to the dataset directory
# dataset_directory = "path/to/dataset"

# # Set the paths for image and label folders
# image_folder = os.path.join(dataset_directory, "image")
# label_folder = os.path.join(dataset_directory, "label")

# # Set the paths for the training and validation folders
# train_directory = os.path.join(dataset_directory, "train")
# val_directory = os.path.join(dataset_directory, "val")

# # Create train and val directories if they don't exist
# os.makedirs(train_directory, exist_ok=True)
# os.makedirs(val_directory, exist_ok=True)

# # Get lists of image and label files
# image_files = os.listdir(image_folder)
# label_files = os.listdir(label_folder)

# # Ensure the lists are sorted for consistency
# image_files.sort()
# label_files.sort()

# # Split the data into train and val sets
# image_train, image_val, label_train, label_val = train_test_split(image_files, label_files, test_size=0.5, random_state=42)

# # Copy the training set to the train directory
# for image_file, label_file in zip(image_train, label_train):
#     shutil.copy(os.path.join(image_folder, image_file), os.path.join(train_directory, image_file))
#     shutil.copy(os.path.join(label_folder, label_file), os.path.join(train_directory, label_file))

# # Copy the validation set to the val directory
# for image_file, label_file in zip(image_val, label_val):
#     shutil.copy(os.path.join(image_folder, image_file), os.path.join(val_directory, image_file))
#     shutil.copy(os.path.join(label_folder, label_file), os.path.join(val_directory, label_file))

import os
import shutil
from sklearn.model_selection import train_test_split

# Set the path to the dataset directory
dataset_directory = "C:/Users/user/Downloads/projects/MBG-YOLOv7/datasets"

# Set the paths for image and label folders
image_folder = os.path.join(dataset_directory, "imageframes")
label_folder = os.path.join(dataset_directory, "labelframes")

# Set the paths for the training, validation, and test folders
train_directory = os.path.join(dataset_directory, "train")
val_directory = os.path.join(dataset_directory, "val")
test_directory = os.path.join(dataset_directory, "test")

# Create train, val, and test directories if they don't exist
os.makedirs(train_directory, exist_ok=True)
os.makedirs(val_directory, exist_ok=True)
os.makedirs(test_directory, exist_ok=True)

# Get lists of image and label files
image_files = os.listdir(image_folder)
label_files = os.listdir(label_folder)

# Ensure the lists are sorted for consistency
image_files.sort()
label_files.sort()

# # Split the data into train, val, and test sets
# image_train, image_temp, label_train, label_temp = train_test_split(image_files, label_files, test_size=0.4, random_state=42)
# image_val, image_test, label_val, label_test = train_test_split(image_temp, label_temp, test_size=0.333, random_state=42)

#First split to get 20% as test set
image_train, image_test, label_train, label_test = train_test_split(image_files, label_files, test_size=0.6, random_state=1)
image_train, image_val, label_train, label_val = train_test_split(image_train, label_train, test_size=0.333, random_state=1)
# 33.3% of 60% is 20% of the whole dataset (0.333 x 0.6 = 0.2)

# Copy the training set to the train directory
for image_file, label_file in zip(image_train, label_train):
    shutil.copy(os.path.join(image_folder, image_file), os.path.join(train_directory, image_file))
    shutil.copy(os.path.join(label_folder, label_file), os.path.join(train_directory, label_file))

# Copy the validation set to the val directory
for image_file, label_file in zip(image_val, label_val):
    shutil.copy(os.path.join(image_folder, image_file), os.path.join(val_directory, image_file))
    shutil.copy(os.path.join(label_folder, label_file), os.path.join(val_directory, label_file))

# Copy the test set to the test directory
for image_file, label_file in zip(image_test, label_test):
    shutil.copy(os.path.join(image_folder, image_file), os.path.join(test_directory, image_file))
    shutil.copy(os.path.join(label_folder, label_file), os.path.join(test_directory, label_file))
