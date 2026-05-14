import numpy as np
import cv2
import matplotlib.pyplot as plt

# User input
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Draw rectangle
cv2.rectangle(
    image,
    (50,50),
    (250,200),
    (255,0,0),
    3
)

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display
plt.imshow(image_rgb)
plt.title("Rectangle")
plt.axis('off')

plt.show()

# Save
plt.imsave("rectangle_output.png", image_rgb)