from skimage import io
import numpy as np

def compute_snr(image, noisy_image):
    signal_power = np.mean(image**2)
    noise_power = np.mean((image - noisy_image)**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

def median_filter(image, kernel_size):
    image_height, image_width = image.shape
    kernel_half = kernel_size // 2

    output_image = np.zeros_like(image)

    for y in range(image_height):
        for x in range(image_width):
            # Extraire la région autour du pixel
            region = image[max(0, y - kernel_half):min(image_height, y + kernel_half + 1),
                           max(0, x - kernel_half):min(image_width, x + kernel_half + 1)]
            
            # Appliquer la médiane
            median_value = np.median(region)
            output_image[y, x] = median_value

    return output_image

# Read the image
choice = input("1. Additive\n2. Gaussian\n3. Multiplicative\n4. Salt & Pepper\nChoose a noise type to denoise: ")
image_path = ''
if choice == '1':
    image_path = 'noisy_images/image_additive_noise.png'
elif choice == '2':
    image_path = 'noisy_images/image_gaussian.png'
elif choice == '3':
    image_path = 'noisy_images/image_multiplicative_noise.png'
elif choice == '4':
    image_path = 'noisy_images/image_salt_pepper.png'
else:
    print('Invalid choice')
    exit()
image = io.imread(image_path)
print('Valid choice, loading...\n')

# Apply median filter
kernel_size=0

while (kernel_size %2 != 1): 
    kernel_size_input = input("Enter the kernel size (odd number only, default=3): ")
    kernel_size = 3 if kernel_size_input == "" else int(kernel_size_input)
output_image_median = median_filter(image, kernel_size)

# Save the denoised image
io.imsave('image_denoised.png', output_image_median)
print('Image saved as image_denoised.png\n')

# SNR
image_path_base = '../../Reference_Images/image1_reference.png'
image_base = io.imread(image_path_base)
normal_image = image_base.copy().astype(float)  # Convert to float for accurate calculations

original_snr = compute_snr(normal_image, image.astype(float))
final_snr = compute_snr(normal_image, output_image_median.astype(float))
print(f'Original SNR with noised image: {original_snr:.4f}')
print(f'Final SNR with denoised image: {final_snr:.4f}')
