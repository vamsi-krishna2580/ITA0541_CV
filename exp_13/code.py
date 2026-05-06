# Your Python code goes here
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rows, cols = image_rgb.shape[:2]

# Points
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

# Affine matrix
M = cv2.getAffineTransform(pts1, pts2)

# Transform
affine = cv2.warpAffine(image_rgb, M, (cols, rows))

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(affine)
plt.title("Affine Transform")
plt.axis('off')

plt.show()

plt.imsave("affine_output.png", affine)