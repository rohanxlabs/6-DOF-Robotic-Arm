import pybullet as p

def move_to_target(robot_id, target_position, end_effector_index):
    joint_angles = p.calculateInverseKinematics(robot_id, end_effector_index, target_position)
    return joint_angles