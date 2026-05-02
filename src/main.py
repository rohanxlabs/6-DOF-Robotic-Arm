import pybullet as p
import time
import cv2

#Simulation
from simulation.environment import setup_environment
from simulation.robot_loader import load_robot
from control.gripper import grasp_object, release_object
#Perception
from perception.camera import get_camera_image
from perception.detect import detect_objects
from perception.mapping import pixel_to_world

#kinematics
from kinematics.inverse_kinematics import move_to_target

# gripper
from control.gripper_real import open_gripper, close_gripper

def get_joint_index_by_name(robot_id, joint_name):
    for i in range(p.getNumJoints(robot_id)):
        info = p.getJointInfo(robot_id, i)
        if info[1].decode("utf-8") == joint_name:
            return i
    raise ValueError(f"Joint '{joint_name}' not found")


def get_link_index_by_name(robot_id, link_name):
    for i in range(p.getNumJoints(robot_id)):
        info = p.getJointInfo(robot_id, i)
        if info[12].decode("utf-8") == link_name:
            return i
    raise ValueError(f"Link '{link_name}' not found")


def main():
    setup_environment()
    robot_id = load_robot()

    cube_id = p.loadURDF("cube.urdf", [0.2, 0, 0.1])

    width, height = 640, 480
    end_effector_index = get_link_index_by_name(robot_id, "link6")
    left_finger_joint = get_joint_index_by_name(robot_id, "joint8")
    right_finger_joint = get_joint_index_by_name(robot_id, "joint9")
    constraint_id = None
    print("System Running: Vision Motion Control")
    print(f"End effector link 'link6' mapped to index {end_effector_index}")
    print(f"Left finger joint 'joint8' mapped to index {left_finger_joint}, right finger joint 'joint9' mapped to index {right_finger_joint}")
    print("Press 'g' to grasp the object, 'r' to release it, 'o' to open the gripper, and 'c' to close it.")
    p.addUserDebugText("LF", [0, 0, 0], textColorRGB=[1, 0, 0], parentObjectUniqueId=robot_id, parentLinkIndex=left_finger_joint, textSize=1.2)
    p.addUserDebugText("RF", [0, 0, 0], textColorRGB=[0, 0, 1], parentObjectUniqueId=robot_id, parentLinkIndex=right_finger_joint, textSize=1.2)

    camera_state = {
        "target": [0.0, 0.0, 0.0],
        "radius": 0.8,
        "yaw": 0.0,
        "pitch": -25.0,
        "roll": 0.0,
        "fov": 60,
    }

    while True:
        frame = get_camera_image(camera_state)
        if frame is None:
            break

        result = detect_objects(frame)
        if result:
            x, y, w, h = result
            cx = x + w // 2
            cy = y + h // 2
            target = pixel_to_world(cx, cy, width, height)
            joint_angels = move_to_target(robot_id, end_effector_index, target)
            for i in range(len(joint_angels)):
                p.setJointMotorControl2(robot_id, i, p.POSITION_CONTROL, joint_angels[i])

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 4, (0, 255, 0), -1)

        cv2.imshow("vision", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('g'):
            constraint_id = grasp_object(robot_id, cube_id, end_effector_index)
        elif key == ord('r'):
            release_object(constraint_id)
            constraint_id = None
        elif key == ord('o'):
            open_gripper(robot_id, left_finger_joint, right_finger_joint)
        elif key == ord('c'):
            close_gripper(robot_id, left_finger_joint, right_finger_joint)
        elif key == 27:
            break

        p.stepSimulation()
        time.sleep(1.0 / 240.0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
