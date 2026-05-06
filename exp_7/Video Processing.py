import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('video.mp4')

frames = []
count = 0

while cap.isOpened() and count < 3:
    ret, frame = cap.read()
    if not ret:
        break
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frames.append(frame_rgb)
    count += 1

cap.release()

# Plot frames
plt.figure(figsize=(10,4))

for i in range(len(frames)):
    plt.subplot(1,3,i+1)
    plt.imshow(frames[i])
    plt.title(f"Frame {i+1}")
    plt.axis('off')

plt.show()

print("Frames displayed (Normal speed concept)")