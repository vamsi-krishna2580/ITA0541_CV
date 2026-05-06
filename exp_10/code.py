# Your Python code goes here
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rotated = cv2.rotate(image_rgb, cv2.ROTATE_90_CLOCKWISE)

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(rotated)
plt.title("90 Degree Rotated")
plt.axis('off')

plt.show()

plt.imsave("rotate90.png", rotated)