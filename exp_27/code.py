import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('download.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml'
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=6,
    minSize=(80,80)
)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(image_rgb, (x,y), (x+w,y+h), (255,0,0), 3)

# Display
plt.figure(figsize=(8,6))
plt.imshow(image_rgb)
plt.title("Face Detection")
plt.axis('off')
plt.show()

print("Faces detected:", len(faces))