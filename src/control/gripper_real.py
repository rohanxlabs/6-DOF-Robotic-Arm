import pybullet as p

def open_gripper(robot_id, left_joint,right_joint):
    p.setJointMotorControl2(robot_id, left_joint, p.POSITION_CONTROL, targetPosition=0.04, force=100)
    p.setJointMotorControl2(robot_id, right_joint, p.POSITION_CONTROL, targetPosition=-0.04, force=100)

def close_gripper(robot_id, left_joint,right_joint):
    p.setJointMotorControl2(robot_id, left_joint, p.POSITION_CONTROL, targetPosition=0.0, force=100)
    p.setJointMotorControl2(robot_id, right_joint, p.POSITION_CONTROL, targetPosition=0.0, force=100)