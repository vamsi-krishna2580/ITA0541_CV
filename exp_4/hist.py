import cv2
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Read Image
# -----------------------------
image = cv2.imread('image.jpg')  # Replace with your image path

if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully")

    # -----------------------------
    # Step 2: Convert BGR → RGB (for display)
    # -----------------------------
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # -----------------------------
    # Step 3: Convert to Grayscale
    # -----------------------------
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # -----------------------------
    # Step 4: Histogram Equalization
    # -----------------------------
    equalized = cv2.equalizeHist(gray)

    # -----------------------------
    # Step 5: Display Images
    # -----------------------------
    plt.figure(figsize=(12,6))

    plt.subplot(2,3,1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(2,3,2)
    plt.imshow(gray, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')

    plt.subplot(2,3,3)
    plt.imshow(equalized, cmap='gray')
    plt.title("Equalized Image")
    plt.axis('off')

    # -----------------------------
    # Step 6: Plot Histograms
    # -----------------------------
    plt.subplot(2,3,5)
    plt.hist(gray.ravel(), bins=256)
    plt.title("Original Histogram")

    plt.subplot(2,3,6)
    plt.hist(equalized.ravel(), bins=256)
    plt.title("Equalized Histogram")

    plt.tight_layout()
    plt.show()

    # -----------------------------
    # Step 7: Save Images
    # -----------------------------
    plt.imsave('original_rgb.png', image_rgb)
    plt.imsave('grayscale.png', gray, cmap='gray')
    plt.imsave('equalized.png', equalized, cmap='gray')

    print("All images saved successfully")