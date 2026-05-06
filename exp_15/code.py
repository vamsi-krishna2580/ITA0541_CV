# Your Python code goes here
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.png')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

# Harris Corner Detection
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Mark corners
image_rgb[corners > 0.01 * corners.max()] = [255,0,0]

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(image_rgb)
plt.title("Harris Corner Detection")
plt.axis('off')

plt.show()

plt.imsave("harris_corner_output.png", image_rgb)
print("Corner detected image saved")