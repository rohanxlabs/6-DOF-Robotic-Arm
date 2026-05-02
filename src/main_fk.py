import time
import pybullet as p
from simulation.environment import setup_environment
from simulation.robot_loader import load_robot
from kinematics.forward_kinematics import get_end_effector_pose


def main():
    setup_environment()
    robot_id = load_robot()
    num_joints = p.getNumJoints(robot_id)
    end_effector_index = max(num_joints - 1, 0)
    print(f"Robot has {num_joints} joints; using link index {end_effector_index} for end-effector.")

    try:
        while p.isConnected():
            result = get_end_effector_pose(robot_id, end_effector_index)
            if result is None:
                print("Forward kinematics returned no state; ending loop.")
                break

            pos, ori = result
            print(f"End-Effector Position: {pos}, Orientation: {ori}")
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("Forward kinematics loop interrupted by user.")
    finally:
        if p.isConnected():
            p.disconnect()
            print("Disconnected from physics server.")


if __name__ == "__main__":
    main()