import cv2
from perception.camera import get_camera_image

def show_camera():
    
    while True:
        frame = get_camera_image()
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()