import numpy as np
def linear_trajectory(start, end, steps=100):
    trajectory = []
    for i in range(steps):
        t = i / (steps)
        points = [
            start[j] + t * (end[j] - start[j]) *t  for j in range(len(start))
        ]
        trajectory.append(points)
    return trajectory