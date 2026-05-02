import pybullet as p
from simulation.environment import setup_environment
from simulation.robot_loader import load_robot
from simulation.joint_control import control_joints

def main():
    physics_client = setup_environment(gui=True)
    robot_id = load_robot()
    control_joints(robot_id, num_steps=2400)
    p.disconnect(physics_client)

if __name__ == "__main__":
    main()