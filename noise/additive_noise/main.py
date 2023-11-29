from skimage import io
import numpy as np
import random

def compute_snr(image, noisy_image):
    signal_power = np.mean(image**2)
    noise_power = np.mean((image - noisy_image)**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

image_path = '../../Reference_Images/image1_reference.png'
image = io.imread(image_path)
normal_image = image.copy().astype(float) # Convert to float for accurate calculations


mean = 0
std_dev = 50

# The standard deviation of the noise
std_dev = input('Enter the standard deviation value (default="50") : ')
std_dev = 50 if std_dev == "" else float(std_dev)

# Iterate through each pixel in the image
for row in range(len(image)):
    for pixel in range(len(image[row])):
        noise = float(np.clip(random.normalvariate(mean, std_dev), -255, 255))
        #u + n
        image[row][pixel] = np.clip((image[row][pixel] + noise), 0, 255)

io.imsave('image_additive_noise.png', image)
print('Image saved as image_additive_noise.png\n')
computed_snr = compute_snr(normal_image, image.astype(float))
print(f'Computed SNR: {computed_snr:.4f}')