from skimage import io
import numpy as np
from scipy.signal import convolve2d

# Définir le noyau (vous devez le spécifier)
# Matrix for identity
# kernel = np.array([[0, 0, 0],
#                    [0, 1, 0],
#                    [0, 0, 0]])

# Définir le noyau (vous devez le spécifier)
# Matrix for edge detection
# kernel = np.array([[-1, -1, -1],
#                    [-1,  8, -1],
#                    [-1, -1, -1]])

def apply_kernel(kernel, image, divider):
    # Dimensions de l'image et du noyau
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # Calculer les marges du noyau pour un centrage correct
    kernel_margin_y = kernel_height // 2
    kernel_margin_x = kernel_width // 2
    
    # Initialiser l'image de sortie avec des zéros
    output_image = np.zeros_like(image)

    # Itérer à travers chaque pixel de l'image d'entrée
    for y in range(image_height):
        for x in range(image_width):
            accumulator = 0.0
            # Parcourir le noyau et appliquer la convolution
            for ky in range(kernel_height):
                for kx in range(kernel_width):
                    # Coordonnées de l'image correspondant au noyau
                    image_y = y + ky - kernel_margin_y
                    image_x = x + kx - kernel_margin_x

                    # Vérifier si les coordonnées sont valides
                    if 0 <= image_y < image_height and 0 <= image_x < image_width:
                        # Appliquer la convolution
                        accumulator += kernel[ky, kx] * image[image_y, image_x]
            # Mettre la valeur de l'accumulateur dans l'image de sortie
            if divider == 0:
                output_image[y, x] = np.clip(accumulator, 0, 255)
            else:
                output_image[y, x] = np.clip(accumulator/divider, 0, 255)
    return output_image
            
# Read the image
image_path = 'image_additive_noise.png'
image = io.imread(image_path)

# Matrix for blurring the image
kernel_blurr = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]])

# Matrix for sharpening the image
kernel_sharp = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]])

output_image_blurr = apply_kernel(kernel_blurr, image, 9)
output_image_sharp = apply_kernel(kernel_sharp, output_image_blurr, 0)
# Enregistrez l'image de sortie blurried.png
io.imsave('image_convolved.png', output_image_sharp)
print('Image saved as image_convolved.png\n')
