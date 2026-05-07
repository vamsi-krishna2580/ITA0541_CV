# Your Python code goes here
import cv2

cap = cv2.VideoCapture('video.mp4')

frames = []

# Read all frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

# Reverse frames
frames.reverse()

# Video writer
height, width, _ = frames[0].shape

out = cv2.VideoWriter(
    'reverse_video.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    20,
    (width, height)
)

# Save reverse video
for frame in frames:
    out.write(frame)

out.release()

print("Reverse video saved")