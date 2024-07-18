import timeit
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
L1 = alg3d.vector(e1=1).normalized() ^ PLANE
L2 = alg3d.vector(e2=1).normalized() ^ PLANE
axis = L1.cp(L2)

# Create the point-reflected shape and the lines between them
point_reflected_points1 = p1 >> points1
point_reflected_points2 = p1 >> points2
pshape = list(zip(point_reflected_points1, point_reflected_points2))
plines = list(zip(point_reflected_points1, points1))

t0 = None

def birefl_point_graph_func():
    global t0
    if t0 is None:
        t0 = timeit.default_timer()
    t = np.sin((timeit.default_timer() - t0)) / 50
    R = np.cos(t) + np.sin(t) * axis
    L1p, L2p = R >> L1, R >> L2
    # Reflect the points in lines once and then once more.
    rpoints1 = L1p >> points1
    rrpoints1 = L2p >> rpoints1
    rpoints2 = L1p >> points2
    rrpoints2 = L2p >> rpoints2
    # Create the reflected shape and the lines between them
    rshape = list(zip(rpoints1, rpoints2))
    rrshape = list(zip(rrpoints1, rrpoints2))
    rlines = list(zip(rpoints1, points1))
    rrlines = list(zip(rpoints1, rrpoints1))

    return [
        p1,
        L1p, 
        L2p,
        clrs[0],
        *shape,
        clrs[2],
        *pshape,
        *rrshape,
        '<G stroke-width="0.002">',clrs[0],
        *plines,
        *rlines,
        *rrlines,
        '</G>',
        '<G stroke-dasharray="0.02 0.02">', clrs[1],
        *rshape,
        '</G>',
    ]