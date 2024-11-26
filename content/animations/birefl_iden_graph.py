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

L1 = alg3d.vector(e1=1).normalized() ^ PLANE
L2 = alg3d.vector(e2=1).normalized() ^ PLANE
axis = L1.cp(L2)

t0 = None

def birefl_iden_graph_func():
    global t0
    if t0 is None:
        t0 = timeit.default_timer()
    t = np.sin((timeit.default_timer() - t0)) / 50
    R = np.cos(t) + np.sin(t) * axis
    L1p = R >> L1
    _rpoints1 = L1p >> points1
    _rpoints2 = L1p >> points2
    rshape = list(zip(_rpoints1, _rpoints2))
    rlines = list(zip(_rpoints1, points1))
    return [
        L1p,
        clrs[0],
        *shape,
        '<G stroke-dasharray="0.02 0.02">', clrs[1],
        *rshape,
        '</G>',
        '<G stroke-width="0.002">',clrs[0],
        *rlines,
        '</G>',
        '<G stroke-dasharray="0.2 0.2">', clrs[2],
        *shape,
        '</G>',
        '<G stroke-dasharray="0.2 0.2">', 0xbbbbbb,
        L1p,
        '</G>',
    ]
