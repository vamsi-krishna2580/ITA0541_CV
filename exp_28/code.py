import cv2
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('image.jpg')

# Check image loaded
if image is None:
    print("Image not found")
    exit()

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load vehicle cascade
car_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_car.xml'
)

# Check cascade loaded
if car_cascade.empty():
    print("XML file not loaded")
    exit()

# Detect vehicles
cars = car_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=3,
    minSize=(40,40)
)

# Draw rectangles
for (x, y, w, h) in cars:

    cv2.rectangle(
        image_rgb,
        (x, y),
        (x + w, y + h),
        (255, 0, 0),
        3
    )

    cv2.putText(
        image_rgb,
        'Vehicle',
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 0, 0),
        2
    )

# Display
plt.figure(figsize=(10,6))

plt.imshow(image_rgb)
plt.title("Vehicle Detection using Haar Cascade")

plt.axis('off')

plt.show()

# Save output
plt.imsave("vehicle_detection_output.png", image_rgb)

print("Vehicle detection completed")