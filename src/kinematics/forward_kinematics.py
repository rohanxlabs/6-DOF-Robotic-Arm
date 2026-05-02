import pybullet as p

def get_end_effector_pose(robot_id, end_effector_link_index):
    if not p.isConnected():
        return None

    state = p.getLinkState(robot_id, end_effector_link_index)
    if state is None:
        return None

    position = state[0]  # End-effector position
    orientation = state[1]  # End-effector orientation (quaternion)
    return position, orientation