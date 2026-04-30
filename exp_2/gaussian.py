import cv2
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Read Image (Handling)
# -----------------------------
image = cv2.imread('image.jpg')  # Replace with your image path

if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully")

    # -----------------------------
    # Step 2: Convert BGR → RGB
    # -----------------------------
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # -----------------------------
    # Step 3: Apply Gaussian Blur (Preprocessing)
    # (kernel size must be odd: (5,5), (7,7), etc.)
    # -----------------------------
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Convert blurred image for display
    blurred_rgb = cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB)

    # -----------------------------
    # Step 4: Display Images
    # -----------------------------
    plt.figure(figsize=(8,4))

    plt.subplot(1,2,1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.imshow(blurred_rgb)
    plt.title("Gaussian Blurred Image")
    plt.axis('off')

    plt.show()

    # -----------------------------
    # Step 5: Save Blurred Image
    # -----------------------------
    plt.imsave('gaussian_blur_output.png', blurred_rgb)
    print("Blurred image saved successfully")