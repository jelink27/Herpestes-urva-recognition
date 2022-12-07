import os
from PIL import Image
import numpy as np
import imgaug as ia
from imgaug import augmenters as iaa


# Check if the path exists
path = "C:/Users/jelin/OneDrive/桌面/Data_test"
if not os.path.exists(path):
    print(f"Error: directory {path} does not exist.")
    exit()

# Get a list of image files in the directory
files = [f for f in os.listdir(path) if f.endswith(".jpg") or f.endswith(".png")]
if len(files) == 0:
    print(f"Error: no image files found in directory {path}.")
    exit()

# Loop through the image files
for file in files:
    # Open the image file and convert it to a numpy array
    with Image.open(os.path.join(path, file)) as image:
        image = np.array(image)

    # Define the image augmentation transformer
    seq = iaa.Sequential([
        iaa.Flipud(0.0), # Vertical flip 垂直翻轉
        iaa.Fliplr(0.5), # Horizontal flip 水平翻轉
        iaa.Affine(rotate=(-20, 20)), # Rotation
        iaa.Multiply((0.5, 1.5)), # Brightness adjustment
        iaa.GaussianBlur(sigma=(0, 0.5)) # Blurring
    ])

    # Apply the transformer to the image
    augmented_images = seq.augment_images([image] * 5)

    # Loop through the augmented images
    for i, augmented_image in enumerate(augmented_images):
        # Convert the augmented image to a PIL image
        image = Image.fromarray(augmented_image)

        # Generate the file name for the augmented image
        basename, ext = os.path.splitext(file)
        filename = f"{basename}_{i}{ext}"

        # Save the augmented image to a file
        image.save(os.path.join(path, filename))