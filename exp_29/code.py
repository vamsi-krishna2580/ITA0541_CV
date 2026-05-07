# Your Python code goes here
import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('image.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Eye Cascade
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

# Detect eyes
eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangles
for (x,y,w,h) in eyes:
    cv2.rectangle(image_rgb, (x,y), (x+w,y+h), (0,255,0), 2)

# Display
plt.imshow(image_rgb)
plt.title("Eye Detection")
plt.axis('off')
plt.show()