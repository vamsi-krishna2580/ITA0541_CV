import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('video.mp4')

frames = []
count = 0
max_frames = 12 # Number of frames you want

while cap.isOpened() and count < max_frames:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frames.append(frame_rgb)
    count += 1

cap.release()

# Display frames
cols = 4
rows = (len(frames) + cols - 1) // cols

plt.figure(figsize=(15, 8))

for i in range(len(frames)):
    plt.subplot(rows, cols, i + 1)
    plt.imshow(frames[i])
    plt.title(f"Frame {i+1}")
    plt.axis('off')

plt.tight_layout()
plt.show()

print(f"{len(frames)} frames displayed")