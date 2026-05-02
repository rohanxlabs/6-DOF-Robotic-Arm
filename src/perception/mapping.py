def pixel_to_world(cx,cy,width,height):
    center_x = width /2
    center_y = height /2

    scale = 0.0015

    x=(cx - center_x) * scale
    y=(cy - center_y) * scale

    z=0.1

    return [x,y,z]