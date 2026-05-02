import pybullet as p
import time
from kinematics.inverse_kinematics import move_to_target
from kinematics.forward_kinematics import get_end_effector_pose
from control.trajectory import linear_trajectory

def smooth_move(robot_id):

    joint_count = p.getNumJoints(robot_id)
    if joint_count == 0:
        raise RuntimeError("Loaded robot has no joints to control.")

    end_effector_index = joint_count - 1

    result = get_end_effector_pose(robot_id, end_effector_index)
    if result is None:
        raise RuntimeError(f"Failed to get end-effector pose for link {end_effector_index}.")

    current_pos, _ = result
    target_pos = [0.3, -0.2, 0.5]
    trajectory = linear_trajectory(current_pos, target_pos, steps=200)
    for point in trajectory:
        joint_angles = move_to_target(robot_id, point, end_effector_index)
        for i in range(len(joint_angles)):
            p.setJointMotorControl2(
                bodyIndex=robot_id,
                jointIndex=i,
                controlMode=p.POSITION_CONTROL,
                targetPosition=joint_angles[i],
            )
        p.stepSimulation()
        time.sleep(1.0 / 240.0)