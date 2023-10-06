from skimage import io
import numpy as np

def compute_snr(image, noisy_image):
    signal_power = np.mean(image**2)
    noise_power = np.mean((image - noisy_image)**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

image_path = 'image1_reference.png'
normal_image = io.imread(image_path).astype(float)  # Convert to float for accurate calculations

image_path_noisy = 'image1_bruitee_snr_16.4138.png'
noisy_image = io.imread(image_path_noisy).astype(float)  # Convert to float for accurate calculations
real_snr = float(image_path_noisy.split("_snr_")[1].split(".png")[0])  # Convert to float

print(f'The SNR should be {real_snr}')
computed_snr = compute_snr(normal_image, noisy_image)
print(f'Computed SNR: {computed_snr:.4f}')
