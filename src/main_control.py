from simulation.environment import setup_environment
from simulation.robot_loader import load_robot
from control.smooth_control import smooth_move

def main():
    setup_environment()
    robot_id = load_robot()
    smooth_move(robot_id)
    input("Simulation complete. Press Enter to exit...")

if __name__ == "__main__":
    main()