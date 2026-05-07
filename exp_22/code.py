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

# Closing
closing = cv2.morphologyEx(image_rgb, cv2.MORPH_CLOSE, kernel)

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(closing)
plt.title("Closing Operation")
plt.axis('off')

plt.tight_layout()
plt.show()

# Save
plt.imsave("closing_output.png", closing)