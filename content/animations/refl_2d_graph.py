# Graph showing a single reflection in 2D.

import timeit
import numpy as np

from .config import alg3d, clrs, PLANE, ORIGIN

# Initiate a shape
np.random.seed(42)
coords = np.ones((3, 5))
coords[1:3] = np.random.uniform(0.5, 1.5, size=(2, 5))
points1 = alg3d.vector(coords, keys=('e0', 'e1', 'e2')).dual()
points2 = points1.map(lambda v: np.roll(v, 1, axis=-1))
shape = list(zip(points1, points2))

t0 = None
L1 = alg3d.vector(e1=1).normalized() ^ PLANE


def refl_2d_graph_func():
    t = timeit.default_timer() / 50
    # Create the reflected shape and the lines between them
    R = np.cos(t) + ORIGIN*np.sin(t)
    L1p = R >> L1
    _rpoints1 = L1p >> points1
    _rpoints2 = L1p >> points2
    rshape = zip(_rpoints1, _rpoints2)
    rlines = zip(_rpoints1, points1)
    
    return [
        L1p,
        clrs[0],
        *shape, 
        clrs[2],
        *rshape,
        '<G stroke-width="0.002">',clrs[0],
        *rlines,
        '</G>',
    ]