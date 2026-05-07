import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image
image = cv2.imread('watch.jpg')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur image
blur = cv2.GaussianBlur(gray, (9,9), 2)

# Detect circles
circles = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=300,
    param1=100,
    param2=50,
    minRadius=80,
    maxRadius=150
)

# Draw only largest circle
if circles is not None:

    circles = np.round(circles[0, :]).astype("int")

    # Select largest circle
    largest = max(circles, key=lambda c: c[2])

    x, y, r = largest

    cv2.circle(image_rgb, (x, y), r, (255,0,0), 4)

    cv2.putText(
        image_rgb,
        'Watch Detected',
        (x-60, y-r-15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,0,0),
        2
    )

# Display
plt.figure(figsize=(8,6))

plt.imshow(image_rgb)
plt.title("Watch Recognition")
plt.axis('off')

plt.show()

# Save output
plt.imsave("watch_detection_output.png", image_rgb)