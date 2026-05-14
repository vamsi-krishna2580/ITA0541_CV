# Your Python code goes here
import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('faces.jpg')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load Haarcascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(
        image_rgb,
        (x, y),
        (x+w, y+h),
        (255, 0, 0),
        3
    )

# Display
plt.figure(figsize=(8,6))

plt.imshow(image_rgb)
plt.title(f"Faces Count = {len(faces)}")
plt.axis('off')

plt.show()

# Save output
plt.imsave("face_detection_output.png", image_rgb)

print("Number of faces detected:", len(faces))