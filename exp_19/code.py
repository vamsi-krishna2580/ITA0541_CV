# Your Python code goes here
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('image.jpg')

# Convert to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Kernel
kernel = np.ones((5,5), np.uint8)

# Erosion
eroded = cv2.erode(image_rgb, kernel, iterations=1)

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(eroded)
plt.title("Erosion Output")
plt.axis('off')

plt.show()

# Save
plt.imsave("erosion_output.png", eroded)
print("Erosion image saved")