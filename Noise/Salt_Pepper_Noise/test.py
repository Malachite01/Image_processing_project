from skimage import io
import random

# Provide the path to your image file
image_path = 'image_salt_pepper.png'

# Read the image
image = io.imread(image_path)

for line in range(len(image)):
    for pixel in range(len(image[line])):
        print(image[line][pixel])
    
