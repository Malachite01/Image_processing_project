# Imports
from skimage import io
import numpy as np

# Variables
image_path = '../../Reference_Images/image1_reference.png'
image = io.imread(image_path)

additive_noise = input('Enter the additive noise value : ')
while additive_noise == '':
    additive_noise = input('Enter the additive noise value : ')
additive_noise = float(additive_noise)

for row in range(len(image)):
    for pixel in range(len(image[row])):
      if np.random.random() > 0.5:
        image[row][pixel] = np.clip((image[row][pixel] + additive_noise), 0, 255)
      else:
        image[row][pixel] = np.clip((image[row][pixel] - additive_noise), 0, 255)

io.imsave('image_additive_noise.png', image)
io.imshow(image)
io.show()
