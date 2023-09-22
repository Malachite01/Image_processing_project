from skimage import io
import numpy as np 

# Provide the path to your image file
image_path = '../../Reference_Images/image1_reference.png'

valeur = input("Enter the additive noise value (between 0 and 1): ")
# Read the image
image = io.imread(image_path)

for line in range(len(image)):
    for pixel in range(len(image[line])):
        if np.random.random() < float(valeur):
            if np.random.random() < 0.5:
                image[line][pixel] = 0
            else:
                image[line][pixel] = 255
    
io.imsave('image_salt_pepper.png', image)
io.imshow(image)
io.show()

