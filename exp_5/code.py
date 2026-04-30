import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    # Step 1: Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
        return

    # Step 2: Split into color channels (BGR)
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')

    plt.figure(figsize=(6,4))
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    # Step 3: Calculate histogram for each channel
    for channel, color in zip(channels, colors):
        hist = cv2.calcHist([channel], [0], None, [256], [0,256])
        plt.plot(hist, color=color)

    plt.show()

# Call the function
analyze_histogram('image.jpg')