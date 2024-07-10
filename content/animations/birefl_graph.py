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
p2 = alg3d.vector(e0=1, e1=0, e2=1).dual()
u = lambda: ((p1 & p2).normalized())
L1 = alg3d.vector(e1=1).normalized() ^ PLANE

def birefl_graph_func():
    # Reflect the points once and then once more.
    rpoints1 = u >> points1
    rrpoints1 = L1 >> rpoints1
    rpoints2 = u >> points2
    rrpoints2 = L1 >> rpoints2
    
    # Create the reflected shape and the lines between them
    rshape = zip(rpoints1, rpoints2)
    rrshape = zip(rrpoints1, rrpoints2)
    rlines = zip(rpoints1, points1)
    rrlines = zip(rpoints1, rrpoints1)
    
    return [
        p1, p2,
        u,
        L1,
        clrs[0],
        *shape, 
        '<G stroke-dasharray="0.02 0.02">',clrs[1],
        *rshape,
        '</G>',
        '<G stroke-width="0.002">',clrs[0],
        *rlines,
        *rrlines,
        '</G>',
        clrs[2], 
        *rrshape,
    ]