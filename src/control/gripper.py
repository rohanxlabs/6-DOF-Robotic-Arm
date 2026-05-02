import pybullet as p 
def grasp_object(robot_id,object_id,end_effector_index):
    ee_state = p.getLinkState(robot_id,end_effector_index)
    ee_pos = ee_state[0]
    obj_pos,_=p.getBasePositionAndOrientation(object_id)

    distance = ((ee_pos[0]-obj_pos[0])**2+(ee_pos[1]-obj_pos[1])**2+(ee_pos[2]-obj_pos[2])**2)**0.5
    if distance < 0.05:
        constraint_id = p.createConstraint(
            parentBodyUniqueId=robot_id,
            parentLinkIndex=end_effector_index,
            childBodyUniqueId=object_id,
            childLinkIndex=-1,
            jointType=p.JOINT_FIXED,
            jointAxis=[0, 0, 0],
            parentFramePosition=[0, 0, 0],
            childFramePosition=[0, 0, 0]
        )
        print("Object grasped!")
        return constraint_id
    return None

def release_object(constraint_id):
    if constraint_id is not None:
        p.removeConstraint(constraint_id)
        print("Object released!")