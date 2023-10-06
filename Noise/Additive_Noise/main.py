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

# The strength of the additive noise
additive_noise = input('Enter the additive noise value (0-255) : ')
while additive_noise == '' or float(additive_noise) < 0 or float(additive_noise) > 255:
    additive_noise = input('Enter the additive noise value (0-255) : ')
additive_noise = float(additive_noise)

# The probability of the noise
noise_probability = input('Enter the noise probability (0-1, the lower the stronger) : ')
while noise_probability == '' or float(noise_probability) < 0 or float(noise_probability) > 1:
    noise_probability = input('Enter the noise probability (0-1, the lower the stronger) : ')
noise_probability = float(noise_probability)

# Iterate through each pixel in the image and randomly add or subtract the random additive noise value (min 0, max 255)
for row in range(len(image)):
    for pixel in range(len(image[row])):
        if np.random.random() > noise_probability:
            noise = np.random.uniform(-additive_noise, additive_noise)
            #u + n
            image[row][pixel] = np.clip((image[row][pixel] + noise), 0, 255)

io.imsave('image_additive_noise.png', image)
print('Image saved as image_additive_noise.png\n')
computed_snr = compute_snr(normal_image, image.astype(float))
print(f'Computed SNR: {computed_snr:.4f}')