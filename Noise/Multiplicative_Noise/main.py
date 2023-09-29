from skimage import io
import numpy as np

image_path = 'Reference_Images/image1_reference.png'
image = io.imread(image_path)
additive_noise = input('Enter the additive noise value : ')

while additive_noise == '':
    additive_noise = input('Enter the additive noise value : ')
additive_noise = float(additive_noise)

# Iterate through each pixel in the image and randomly add or subtract the additive noise value (min 0, max 255)
for row in range(len(image)):
    for pixel in range(len(image[row])):
      if np.random.random() > 0.8:
        image[row][pixel] = np.clip(image[row][pixel] + (image[row][pixel] * additive_noise), 0, 255)

io.imsave('image_additive_noise.png', image)

