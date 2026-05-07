# Your Python code goes here
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(sobelx, cmap='gray')
plt.title("Sobel X")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(sobely, cmap='gray')
plt.title("Sobel Y")
plt.axis('off')

plt.show()