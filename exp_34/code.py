# Your Python code goes here
import numpy as np
import cv2
import matplotlib.pyplot as plt

# User input
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Draw circle
cv2.circle(
    image,
    (width//2, height//2),
    100,
    (0,0,255),
    3
)

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display
plt.imshow(image_rgb)
plt.title("Circle")
plt.axis('off')

plt.show()

# Save
plt.imsave("circle_output.png", image_rgb)