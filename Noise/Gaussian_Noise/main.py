import random
import math
from skimage import io
import numpy as np 


# Définir la moyenne et l'écart-type du bruit gaussien
mu = input("Enter the mean of the gaussian noise (between -255 and 255): ")
sigma = input("Enter the standard deviation of the gaussian noise (between 0 and 255): ")

# Fonction pour générer du bruit gaussien
def generate_gaussian_noise(mu, sigma):
    u1 = random.random()
    u2 = random.random()
    x = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    return mu + sigma * x


# Provide the path to your image file
image_path = '../../Reference_Images/image1_reference.png'

# Read the image
image = io.imread(image_path)

for line in range(len(image)):
    for pixel in range(len(image[line])):
            x = generate_gaussian_noise(float(mu), float(sigma))
            #print("la valeur de x est : ", x)
            image[line][pixel] = np.clip((image[line][pixel] + x), 0, 255)
    
io.imsave('image_gaussian.png', image)