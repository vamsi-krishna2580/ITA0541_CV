import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('image.jpg')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, _ = image_rgb.shape

print("Image Size:", width, "x", height)

# Crop ROI safely
roi = image_rgb[50:150, 50:150]

# Copy image
image_copy = image_rgb.copy()

# ROI dimensions
roi_h, roi_w, _ = roi.shape

# Safe paste position
x = width - roi_w - 10
y = height - roi_h - 10

# Paste ROI
image_copy[y:y+roi_h, x:x+roi_w] = roi

# Display
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(roi)
plt.title("Cropped ROI")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(image_copy)
plt.title("Copied & Pasted ROI")
plt.axis('off')

plt.tight_layout()
plt.show()

# Save output
plt.imsave("roi_output.png", image_copy)

print("ROI copied and saved successfully")