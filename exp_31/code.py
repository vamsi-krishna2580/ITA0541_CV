# Your Python code goes here
import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('image.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold segmentation
_, segmented = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Original Gray Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(segmented, cmap='gray')
plt.title("Segmented Image")
plt.axis('off')

plt.tight_layout()
plt.show()

# Save
plt.imsave("segmented_output.png", segmented, cmap='gray')