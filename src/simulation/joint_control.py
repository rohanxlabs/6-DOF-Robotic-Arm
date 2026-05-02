import pybullet as p
import time
from kinematics.inverse_kinematics import move_to_target


def control_joints(robot_id, num_steps=2400):
    joint_count = p.getNumJoints(robot_id)
    if joint_count == 0:
        raise RuntimeError("Loaded robot has no joints to control.")

    end_effector_index = joint_count - 1  # Use the last joint index as the end effector
    target_position = [0.3, 0.2, 0.5]  # Desired position for the end effector

    for step in range(num_steps):
        joint_angles = move_to_target(robot_id, target_position, end_effector_index)

        for joint_index in range(min(len(joint_angles), joint_count)):
            p.setJointMotorControl2(
                bodyIndex=robot_id,
                jointIndex=joint_index,
                controlMode=p.POSITION_CONTROL,
                targetPosition=joint_angles[joint_index],
                force=500,
            )

        p.stepSimulation()
        time.sleep(1.0 / 240.0)


# Inverse kinematics 
def control_with_ik(robot_id):
    joint_count = p.getNumJoints(robot_id)
    if joint_count == 0:
        raise RuntimeError("Loaded robot has no joints to control.")

    end_effector_index = joint_count - 1
    target = [0.3, 0.2, 0.5]

    while True:
        joint_angles = p.calculateInverseKinematics(robot_id, end_effector_index, target)
        for i in range(min(len(joint_angles), joint_count)):
            p.setJointMotorControl2(
                bodyIndex=robot_id,
                jointIndex=i,
                controlMode=p.POSITION_CONTROL,
                targetPosition=joint_angles[i],
            )
        p.stepSimulation()
        time.sleep(1.0 / 240.0)
