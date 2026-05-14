# Your Python code goes here
import cv2

# Open video
cap = cv2.VideoCapture('video.mp4')

frames = []

# Read all frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

# Play reverse slow motion
for frame in reversed(frames):

    cv2.imshow("Reverse Slow Motion", frame)

    # Slow motion delay
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()