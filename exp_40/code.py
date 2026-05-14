# Your Python code goes here
import cv2
import pytesseract

# Path to tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open video
cap = cv2.VideoCapture('video.mp4')

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1

    # Process every 30th frame
    if frame_count % 30 == 0:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(gray)

        print(f"\nFrame {frame_count}")
        print(text)

cap.release()
cv2.destroyAllWindows()