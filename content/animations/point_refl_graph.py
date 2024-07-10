import numpy as np

from .config import alg3d, clrs, PLANE


# Initiate a shape
np.random.seed(42)
coords = np.ones((3, 5))
coords[1:3] = np.random.uniform(0.5, 1.5, size=(2, 5))
points1 = alg3d.vector(coords, keys=('e0', 'e1', 'e2')).dual()
points2 = points1.map(lambda v: np.roll(v, 1, axis=-1))
shape = list(zip(points1, points2))

p1 = alg3d.vector(e0=1, e1=0, e2=0).dual()

def point_refl_graph_func():
    # Create the reflected shape and the lines between them
    point_reflected_points1 = p1 >> points1
    point_reflected_points2 = p1 >> points2
    rshape = zip(point_reflected_points1, point_reflected_points2)
    rlines = zip(point_reflected_points1, points1)
    
    return [
        p1,
        clrs[0],
        *shape, 
        clrs[2],
        *rshape,
        '<G stroke-width="0.002">',clrs[0],
        *rlines,
        '</G>',
    ]