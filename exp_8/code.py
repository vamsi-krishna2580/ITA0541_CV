# Your Python code goes here
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('image.jpg')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply dilation
dilated = cv2.dilate(image_rgb, kernel, iterations=1)

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(dilated)
plt.title("Dilated Image")
plt.axis('off')

plt.show()

# Save image
plt.imsave("dilated_output.png", dilated)
print("Dilated image saved")