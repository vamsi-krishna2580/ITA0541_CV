# Your Python code goes here
import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('image.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Smile Cascade
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

# Detect smiles
smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)

# Draw rectangles
for (x,y,w,h) in smiles:
    cv2.rectangle(image_rgb, (x,y), (x+w,y+h), (255,0,0), 2)

# Display
plt.imshow(image_rgb)
plt.title("Smile Detection")
plt.axis('off')
plt.show()