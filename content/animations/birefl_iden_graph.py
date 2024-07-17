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
_rpoints1 = L1 >> points1
_rpoints2 = L1 >> points2
rshape = list(zip(_rpoints1, _rpoints2))
rlines = list(zip(_rpoints1, points1))

def birefl_iden_graph_func():   
    return [
        L1,
        clrs[0],
        *shape,
        clrs[1],
        *rshape,
        '<G stroke-width="0.002">',clrs[0],
        *rlines,
        '</G>',
        '<G stroke-dasharray="0.2 0.2">', clrs[2],
        *shape,
        '</G>',
        '<G stroke-dasharray="0.2 0.2">', 0xbbbbbb,
        L1,
        '</G>',
    ]
