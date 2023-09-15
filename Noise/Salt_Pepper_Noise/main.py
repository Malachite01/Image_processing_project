from skimage import io

# Provide the path to your image file
image_path = '../../Reference_Images/image1_reference.png'

# Read the image
image = io.imread(image_path)


print(image[1][1])