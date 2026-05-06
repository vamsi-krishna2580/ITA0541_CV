# Image Scaling using OpenCV and Matplotlib

import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('image.jpg')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Resize Bigger
bigger = cv2.resize(image_rgb, None, fx=2, fy=2)

# Resize Smaller
smaller = cv2.resize(image_rgb, None, fx=0.5, fy=0.5)

# Print dimensions
print("Original Image Size :", image_rgb.shape)
print("Bigger Image Size   :", bigger.shape)
print("Smaller Image Size  :", smaller.shape)

# Display images
plt.figure(figsize=(15,5))

# Original
plt.subplot(1,3,1)
plt.imshow(image_rgb)
plt.title(f"Original Image\nSize: {image_rgb.shape[1]} x {image_rgb.shape[0]}")
plt.axis('off')

# Bigger
plt.subplot(1,3,2)
plt.imshow(bigger)
plt.title(f"Bigger Image\nSize: {bigger.shape[1]} x {bigger.shape[0]}")
plt.axis('off')

# Smaller
plt.subplot(1,3,3)
plt.imshow(smaller)
plt.title(f"Smaller Image\nSize: {smaller.shape[1]} x {smaller.shape[0]}")
plt.axis('off')

plt.tight_layout()
plt.show()

# Save images
plt.imsave("bigger_image.png", bigger)
plt.imsave("smaller_image.png", smaller)

print("Images saved successfully")