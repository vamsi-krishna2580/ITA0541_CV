import cv2

cap = cv2.VideoCapture('video.mp4')
speed = 1

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    key = cv2.waitKey(speed)

    if key == ord('s'):
        speed = 100   # Slow

    elif key == ord('f'):
        speed = 1     # Fast

    elif key == ord('n'):
        speed = 30    # Normal

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()