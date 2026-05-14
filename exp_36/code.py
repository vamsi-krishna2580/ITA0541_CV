# Your Python code goes here
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('image.jpg')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define background color range (example: white background)
lower = np.array([0, 0, 200])
upper = np.array([180, 40, 255])

# Create mask
mask = cv2.inRange(hsv, lower, upper)

# Remove background
result = image_rgb.copy()
result[mask != 0] = [0, 0, 0]

# Display
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(result)
plt.title("Background Removed")
plt.axis('off')

plt.show()

# Save output
plt.imsave("background_removed.png", result)