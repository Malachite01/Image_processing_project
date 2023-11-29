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

mean = 1# Multiplicative noise mean is usually 1
std_dev = 1  # Adjust this value based on the desired level of noise

# The standard deviation of the noise
std_dev = input('Enter the standard deviation value (default="1") : ')
std_dev = 1 if std_dev == "" else float(std_dev)

# Iterate through each pixel in the image and apply multiplicative noise
for row in range(len(image)):
    for pixel in range(len(image[row])):
        noise = float(np.random.normal(mean, std_dev))
        noise = np.clip(noise, -0.5, 0.5)  # Adjust the range of noise factor as needed
        # Apply the multiplicative noise: u * (1 + n)
        image[row][pixel] = np.clip(image[row][pixel] + image[row][pixel] * noise, 0, 255)

io.imsave('image_multiplicative_noise.png', image)
print('Image saved as image_multiplicative_noise.png\n')
computed_snr = compute_snr(normal_image, image.astype(float))
print(f'Computed SNR: {computed_snr:.4f}')
