import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('image.jpg')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, channels = image_rgb.shape

print("Image Width  :", width)
print("Image Height :", height)

# Copy image
watermarked = image_rgb.copy()

# Watermark text
text = "Made by You"

# Font settings
font = cv2.FONT_HERSHEY_TRIPLEX
font_scale = 0.4
thickness = 1

# Get text size
(text_width, text_height), baseline = cv2.getTextSize(
    text,
    font,
    font_scale,
    thickness
)

# Bottom-right position calculation
x = width - text_width - 10
y = height - 10

print("Watermark Position :", x, y)

# Add watermark
cv2.putText(
    watermarked,
    text,
    (x, y),
    font,
    font_scale,
    (0, 0, 0),      # Black text
    thickness,
    cv2.LINE_AA
)

# Display images
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(watermarked)
plt.title("Watermarked Image")
plt.axis('off')

plt.tight_layout()
plt.show()

# Save output
plt.imsave("watermarked_output.png", watermarked)

print("Watermarked image saved successfully")