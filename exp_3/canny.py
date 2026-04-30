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
    # Step 3: Convert to Grayscale
    # -----------------------------
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # -----------------------------
    # Step 4: Apply Canny Edge Detection
    # threshold1 = 100, threshold2 = 200
    # -----------------------------
    edges = cv2.Canny(gray, 100, 200)

    # -----------------------------
    # Step 5: Display Images
    # -----------------------------
    plt.figure(figsize=(10,4))

    plt.subplot(1,3,1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1,3,2)
    plt.imshow(gray, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')

    plt.subplot(1,3,3)
    plt.imshow(edges, cmap='gray')
    plt.title("Canny Edge Output")
    plt.axis('off')

    plt.show()

    # -----------------------------
    # Step 6: Save Edge Image
    # -----------------------------
    plt.imsave('canny_edges_output.png', edges, cmap='gray')
    print("Edge-detected image saved successfully")