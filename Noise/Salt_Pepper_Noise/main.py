from skimage import io
import numpy as np
import random

# Provide the path to your image file
image_path = '../../Reference_Images/image1_reference.png'

# Read the image
image = io.imread(image_path)

for line in range(len(image)):
    for pixel in range(len(image[line])):
        #print(image[line][pixel])
        if(random.random()) < 0.1: # Environ 10% des pixels seront modifiés
            if(random.random()) < 0.5: # Une fois qu'on sait que le pixel sera modifié, 1 chance sur 2 qu'il soit noir ou blanc
                image[line][pixel] = 0
            else:
                image[line][pixel] = 255
    
io.imsave('image_blanc.jpg',image)

