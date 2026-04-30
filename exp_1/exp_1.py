# Import required library
import cv2

# Step 1: Read the image
image = cv2.imread('image.jpg')  # Replace with your file path

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully")

    # Step 2: Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 3: Save the grayscale image
    output_path = 'grayscale_output.jpg'
    saved = cv2.imwrite(output_path, gray_image)

    # Step 4: Check if saved successfully
    if saved:
        print(f"Grayscale image saved successfully at: {output_path}")
    else:
        print("Error: Failed to save image")

    # Step 5: Display images (optional)
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    