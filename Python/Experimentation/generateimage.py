from PIL import Image
import random
import numpy as np

# Create a 2D list representing pixel data (e.g., a grayscale image)
# Values typically range from 0 (black) to 255 (white) for 8-bit images
m=10000
n=10000
l=[]
for i in range(m):
  l.append([])
  for j in range(n):
    l[i].append((i+j)%256)

# Convert the 2D list to a NumPy array
image_array = np.array(l, dtype=np.uint8) # Use uint8 for image data

# Create a PIL Image object from the NumPy array
# 'L' mode is for grayscale images (8-bit pixels, black and white)
image = Image.fromarray(image_array, mode='L')

# Display the image (this opens a separate image viewer)
image.show()

# Save the image to a file
image.save("output_image_pillow.png")