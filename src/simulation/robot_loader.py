import os
import pybullet as p


def load_robot():
    urdf_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "assets", "urdf", "arm6dof.urdf")
    )
    robot_id = p.loadURDF(
        urdf_path,
        basePosition=[0, 0, 0],
        useFixedBase=True,
    )
    return robot_id