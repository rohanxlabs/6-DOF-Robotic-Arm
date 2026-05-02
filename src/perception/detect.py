import cv2
import numpy as np

def detect_objects(frame):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the color you want to detect (e.g., red)
    lower = np.array([0, 120, 70])
    upper = np.array([10, 255, 255])

    # Create a mask using the defined color range
    mask = cv2.inRange(hsv, lower, upper)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        return x, y, w, h
    return None

    