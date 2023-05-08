import cv2
import numpy as np

# Load the image
frame = cv2.imread("frame.png")

# Preprocess the image
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Detect the different elements of the game
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w > 10 and h > 10:
        if w > h:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), -1) # Black rectangle for moving objects
        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (165, 42, 42), -1) # Brown rectangle for blocks Mario can stand on
            if w > 50 and h > 50:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) # Red rectangle for Mario's body

# Display the simplified image
cv2.imshow("Super Mario Bros.", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
