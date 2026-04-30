import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image using OpenCV
image = cv2.imread('image.jpg')  # Replace with your image path

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully")

    # Step 2: Convert BGR → RGB (for correct display)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Step 3: Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 4: Display images using matplotlib
    plt.figure(figsize=(8,4))

    plt.subplot(1,2,1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.imshow(gray, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')

    plt.show()

    # Step 5: Save grayscale image using matplotlib
    plt.imsave('grayscale_matplotlib.png', gray, cmap='gray')
    print("Grayscale image saved successfully using matplotlib")