import numpy as np
import cv2
import matplotlib.pyplot as plt

# User input
height = int(input("Enter image height: "))
width = int(input("Enter image width: "))
text = input("Enter text: ")

# Create white image
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Dynamic font size based on image size
font_scale = min(height, width) / 500
thickness = int(font_scale * 2)

# Text position
x = width // 10
y = height // 2

# Put text
cv2.putText(
    image,
    text,
    (x, y),
    cv2.FONT_HERSHEY_TRIPLEX,
    font_scale,
    (255, 0, 0),
    thickness
)

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display
plt.figure(figsize=(8,8))

plt.imshow(image_rgb)
plt.title("Text on Image")

plt.axis('off')
plt.show()

# Save output
plt.imsave("text_output.png", image_rgb)

print("Image saved successfully")