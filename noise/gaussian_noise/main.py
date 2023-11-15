import random
import math
from skimage import io
import numpy as np 

def compute_snr(image, noisy_image):
    signal_power = np.mean(image**2)
    noise_power = np.mean((image - noisy_image)**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

image_path = '../../Reference_Images/image1_reference.png'
image = io.imread(image_path)
normal_image = image.copy().astype(float) # Convert to float for accurate calculations

# Définir la moyenne et l'écart-type du bruit gaussien
mu = input("Enter the mean of the gaussian noise (between -255 and 255): ")
sigma = input("Enter the standard deviation of the gaussian noise (between 0 and 255): ")

for line in range(len(image)):
    for pixel in range(len(image[line])):
            x = random.normalvariate(float(mu), float(sigma))
            #print("la valeur de x est : ", x)
            image[line][pixel] = np.clip((image[line][pixel] + x), 0, 255)
    
io.imsave('image_gaussian.png', image)
print('Image saved as image_gaussian.png\n')
computed_snr = compute_snr(normal_image, image.astype(float))
print(f'Computed SNR: {computed_snr:.4f}')