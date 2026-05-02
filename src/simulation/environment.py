import pybullet as p
import pybullet_data

def setup_environment(gui=True):
    if gui:
        physics_client = p.connect(p.GUI)
    else:
        physics_client = p.connect(p.DIRECT)

    p.resetSimulation()
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.8)
    p.setTimeStep(1.0 / 240.0)
    p.setRealTimeSimulation(0)
    p.loadURDF("plane.urdf")

    return physics_client