# Your Python code goes here
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rows, cols = image_rgb.shape[:2]

pts1 = np.float32([[50,50],[200,50],[50,200],[200,200]])
pts2 = np.float32([[10,100],[200,50],[100,250],[220,220]])

M = cv2.getPerspectiveTransform(pts1, pts2)

perspective = cv2.warpPerspective(image_rgb, M, (cols, rows))

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(perspective)
plt.title("Perspective Transform")
plt.axis('off')

plt.show()

plt.imsave("perspective_output.png", perspective)