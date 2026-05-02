import cv2
import math
import pybullet as p
import numpy as np

def get_camera_image(camera_state, physics_client_id=None):
    width, height = 640, 480
    radius = camera_state.get("radius", 0.8)
    yaw = camera_state.get("yaw", 0.0)
    pitch = camera_state.get("pitch", 0.0)
    roll = camera_state.get("roll", 0.0)
    target = camera_state.get("target", [0.0, 0.0, 0.0])

    yaw_rad = math.radians(yaw)
    pitch_rad = math.radians(pitch)
    roll_rad = math.radians(roll)

    eye = [
        target[0] + radius * math.cos(pitch_rad) * math.cos(yaw_rad),
        target[1] + radius * math.cos(pitch_rad) * math.sin(yaw_rad),
        target[2] + radius * math.sin(pitch_rad),
    ]

    forward = np.array(target) - np.array(eye)
    forward /= np.linalg.norm(forward)
    world_up = np.array([0.0, 0.0, 1.0])
    right = np.cross(forward, world_up)
    if np.linalg.norm(right) < 1e-6:
        right = np.array([1.0, 0.0, 0.0])
    else:
        right /= np.linalg.norm(right)
    up = np.cross(right, forward)
    up = up / np.linalg.norm(up)

    # Apply roll around the view direction
    up = up * math.cos(roll_rad) + np.cross(forward, up) * math.sin(roll_rad)

    view_matrix = p.computeViewMatrix(
        cameraEyePosition=eye,
        cameraTargetPosition=target,
        cameraUpVector=up.tolist(),
    )
    projection_matrix = p.computeProjectionMatrixFOV(
        fov=camera_state.get("fov", 60),
        aspect=width / height,
        nearVal=0.1,
        farVal=100,
    )
    if physics_client_id is not None:
        img = p.getCameraImage(
            width,
            height,
            view_matrix,
            projection_matrix,
            physicsClientId=physics_client_id,
        )
    else:
        img = p.getCameraImage(
            width,
            height,
            view_matrix,
            projection_matrix,
        )
    if img is None or img[2] is None:
        return None
    rgba = np.reshape(img[2], (height, width, 4)).astype(np.uint8)
    bgr = cv2.cvtColor(rgba, cv2.COLOR_RGBA2BGR)
    return bgr