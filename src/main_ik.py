from simulation.environment import setup_environment
from simulation.robot_loader import load_robot
from simulation.joint_control import control_with_ik

def main():
    setup_environment()
    robot_id = load_robot()
    control_with_ik(robot_id)

if __name__ == "__main__":
    main()