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

L1 = alg3d.vector(e1=1).normalized() ^ PLANE
L2 = alg3d.vector(e1=1, e2=0.5).normalized() ^ PLANE
L3 = alg3d.vector(e1=1, e0=0.5).normalized() ^ PLANE

# Gauge degree in bireflections animation. # TODO: Show both rotation and translation.
def _birefl_gauge_func(L1, L2):   
    intersection = L1.cp(L2)
    if not intersection**2:
        R = lambda t: 1 + intersection*np.sin(5*t)
    else:
        R = lambda t: np.cos(t) + intersection*np.sin(t)
        
    def _graph_func():
        t = timeit.default_timer() / 30
        L1p = R(t) >> L1
        L2p = R(t) >> L2
        # Reflect the points once and then once more.
        rpoints1 = L1p >> points1
        rrpoints1 = L2p >> rpoints1
        rpoints2 = L1p >> points2
        rrpoints2 = L2p >> rpoints2
        # Create the reflected shape and the lines between them
        rshape = zip(rpoints1, rpoints2)
        rrshape = zip(rrpoints1, rrpoints2)
        rlines = zip(rpoints1, points1)
        rrlines = zip(rpoints1, rrpoints1)
        
        return [
            '<G stroke-opacity="0.4">', clrs[-1],
            L1p,
            L2p,
            '</G>',
            0xff9900,
            *shape, 
            '<G stroke-dasharray="0.02 0.02">',0xfed290,
            *rshape,
            '</G>',
            '<G stroke-width="0.002">',0xff9900,
            *rlines,
            *rrlines,
            '</G>',
            0x009977, 
            *rrshape,
        ]
    return _graph_func

birefl_gauge_rot_func = _birefl_gauge_func(L1, L2)
birefl_gauge_trans_func = _birefl_gauge_func(L1, L3)