import pybullet as p
import time
import cv2

from simulation.environment import setup_environment
from simulation.robot_loader import load_robot
from perception.camera import get_camera_image
from perception.detect import detect_objects
from perception.mapping import pixel_to_world

def main():
    physics_client = setup_environment()
    robot_id = load_robot()

    cube_id = p.loadURDF("cube.urdf", [0.2, 0, 0.1])

    camera_state = {
        "target": [0.0, 0.0, 0.0],
        "radius": 0.8,
        "yaw": 0.0,
        "pitch": -25.0,
        "roll": 0.0,
        "fov": 60,
    }

    print("Controls: A/D rotate, W/S zoom, R/F pitch, Q/E roll, +/- FOV, ESC to exit")

    while True:
        frame = get_camera_image(camera_state, physics_client)
        if frame is None:
            break

        result = detect_objects(frame)
        if result:
            x, y, w, h = result
            cx = x + w // 2
            cy = y + h // 2
            world_pos = pixel_to_world(cx, cy, frame.shape[1], frame.shape[0])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 4, (0, 255, 0), -1)
            cv2.putText(
                frame,
                f"World: {world_pos[0]:.3f}, {world_pos[1]:.3f}, {world_pos[2]:.3f}",
                (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.45,
                (255, 255, 255),
                1,
                cv2.LINE_AA,
            )

        cv2.putText(
            frame,
            f"A/D rotate, W/S zoom, R/F pitch, Q/E roll, +/- FOV, ESC",
            (10, 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )
        cv2.putText(
            frame,
            f"radius:{camera_state['radius']:.2f} yaw:{camera_state['yaw']:.0f} pitch:{camera_state['pitch']:.0f} roll:{camera_state['roll']:.0f} fov:{camera_state['fov']}",
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
        elif key == ord('w'):
            camera_state["radius"] = max(0.2, camera_state["radius"] - 0.05)
        elif key == ord('s'):
            camera_state["radius"] += 0.05
        elif key == ord('a'):
            camera_state["yaw"] -= 5
        elif key == ord('d'):
            camera_state["yaw"] += 5
        elif key == ord('r'):
            camera_state["pitch"] = min(80, camera_state["pitch"] + 5)
        elif key == ord('f'):
            camera_state["pitch"] = max(-80, camera_state["pitch"] - 5)
        elif key == ord('q'):
            camera_state["roll"] -= 5
        elif key == ord('e'):
            camera_state["roll"] += 5
        elif key in (ord('+'), ord('=')):
            camera_state["fov"] = max(20, camera_state["fov"] - 5)
        elif key == ord('-'):
            camera_state["fov"] = min(120, camera_state["fov"] + 5)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

        
