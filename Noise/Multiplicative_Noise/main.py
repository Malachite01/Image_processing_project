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

# The strength of the multiplicative noise
multiplicative_noise = input('Enter the multiplicative noise value (0-255) : ')
while multiplicative_noise == '' or float(multiplicative_noise) < 0 or float(multiplicative_noise) > 255:
    multiplicative_noise = input('Enter the multiplicative noise value (0-255) : ')
multiplicative_noise = float(multiplicative_noise)

# The probability of the noise
noise_probability = input('Enter the noise probability (0-1, the lower the stronger) : ')
while noise_probability == '' or float(noise_probability) < 0 or float(noise_probability) > 1:
    noise_probability = input('Enter the noise probability (0-1, the lower the stronger) : ')
noise_probability = float(noise_probability)

# Iterate through each pixel in the image and apply multiplicative noise
for row in range(len(image)):
    for pixel in range(len(image[row])):
        if np.random.random() > noise_probability:
            noise = np.random.uniform(-multiplicative_noise/255, multiplicative_noise/255)
            # Apply the multiplicative noise: u * (1 + n)
            image[row][pixel] = np.clip(image[row][pixel] * (1 + noise), 0, 255)

io.imsave('image_multiplicative_noise.png', image)
print('Image saved as image_multiplicative_noise.png\n')
computed_snr = compute_snr(normal_image, image.astype(float))
print(f'Computed SNR: {computed_snr:.4f}')
