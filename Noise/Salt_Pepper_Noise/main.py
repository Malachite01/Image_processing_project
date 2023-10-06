from skimage import io
import numpy as np 

def compute_snr(image, noisy_image):
    signal_power = np.mean(image**2)
    noise_power = np.mean((image - noisy_image)**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

image_path = '../../Reference_Images/image1_reference.png'
image = io.imread(image_path)
normal_image = image.copy().astype(float)  # Convert to float for accurate calculations

valeur = input("Enter the additive noise value (0-1, the stronger the stronger): ")

for line in range(len(image)):
    for pixel in range(len(image[line])):
        if np.random.random() < float(valeur):
            if np.random.random() < 0.5:
                image[line][pixel] = 0
            else:
                image[line][pixel] = 255
    
io.imsave('image_salt_pepper.png', image)
print('Image saved as image_salt_pepper.png\n')
computed_snr = compute_snr(normal_image, image.astype(float))
print(f'Computed SNR: {computed_snr:.4f}')

