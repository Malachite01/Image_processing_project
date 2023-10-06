import random
import math
from skimage import io
import numpy as np 

# Fonction pour générer du bruit gaussien
def generate_gaussian_noise(mu, sigma):
    u1 = random.random()
    u2 = random.random()
    x = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    return mu + sigma * x

def compute_snr(image, noisy_image):
    signal_power = np.mean(image**2)
    noise_power = np.mean((image - noisy_image)**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

image_path = '../../Reference_Images/image1_reference.png'
image = io.imread(image_path)
normal_image = image.copy()

# Définir la moyenne et l'écart-type du bruit gaussien
mu = input("Enter the mean of the gaussian noise (between -255 and 255): ")
sigma = input("Enter the standard deviation of the gaussian noise (between 0 and 255): ")

for line in range(len(image)):
    for pixel in range(len(image[line])):
            x = generate_gaussian_noise(float(mu), float(sigma))
            #print("la valeur de x est : ", x)
            image[line][pixel] = np.clip((image[line][pixel] + x), 0, 255)
    
io.imsave('image_gaussian.png', image)
print('Image saved as image_gaussian.png\n')
print('SNR : ' + str(compute_snr(normal_image, image)))