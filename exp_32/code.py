# Your Python code goes here
import numpy as np
import cv2
import matplotlib.pyplot as plt

# User input
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Box size
box_h = height // 10
box_w = width // 10

# Black box (top-left)
image[0:box_h, 0:box_w] = [0,0,0]

# Blue box (top-right)
image[0:box_h, width-box_w:width] = [0,0,255]

# Green box (bottom-left)
image[height-box_h:height, 0:box_w] = [0,255,0]

# Red box (bottom-right)
image[height-box_h:height, width-box_w:width] = [255,0,0]

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display
plt.imshow(image_rgb)
plt.title("Colored Corner Boxes")
plt.axis('off')

plt.show()

# Save
plt.imsave("colored_boxes.png", image_rgb)