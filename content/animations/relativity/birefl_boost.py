import timeit
import numpy as np

from ..config import clrs, ptap, ltap

np.random.seed(42)
alg = ltap
coords = np.ones((3, 5))
# coords[1:3] = np.random.uniform(0.5, 1.5, size=(2, 5))
coords[1:3] = np.random.uniform(0.5, 1.5, size=(2, 5))
points1 = alg.vector(coords, keys=('e0', 'e1', 'e2')).dual()
points1 = alg.evenmv(e=1, e01=-0.5) >> points1
points2 = points1.map(lambda v: np.roll(v, 1, axis=-1))
shape = list(zip(points1, points2))


# PLANE = alg.blades.e2
def normalized(x):
    sq = x.normsq().e
    if sq >= 0:
        return x / sq**0.5
    return x / (-sq)**0.5

# L1 = normalized(alg.vector(e1=-0.2, e2=1.))
# # L2 = alg.blades.e12 | L1
# L2 = normalized(alg.vector(e1=0.2, e2=1.))
L1 = normalized(alg.vector(e1=1))
L2 = alg.blades.e12 | L1
# L2 = normalized(alg.vector(e1=1, e2=0.2))
intersection = L1.cp(L2)
R = lambda t: np.cosh(t) + intersection*np.sinh(t)
ep, em = alg.vector(e1=1, e2=1), alg.vector(e1=1, e2=-1)

boost = normalized(1 + alg.blades.e1 / normalized(points1[2] & alg.blades.e0.dual()))
hyperbola_seed = boost >> points1[2]

Rs = R(np.linspace(-2, 3, 30))
hyperbola_points = Rs >> hyperbola_seed
hyperbola = list(zip(hyperbola_points[1:], hyperbola_points[:-1]))

def birefl_boost_func():
    t = 0.1 * np.sin(timeit.default_timer() / 2)
    # t=0.
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
        '<G rotate(45)">',
        '<G stroke-dasharray="0.05 0.05" stroke-opacity="0.2" >', clrs[-1],
        ep, em,
        *hyperbola,
        '</G>',
        '<G stroke-opacity="0.4" fill-opacity="0.4">', clrs[-1],
        L1p,
        L2p,
        intersection,
        '</G>',
        clrs[0],
        *shape, 
        '<G stroke-dasharray="0.02 0.02">',clrs[1],
        *rshape,
        '</G>',
        '<G stroke-width="0.002">',clrs[1],
        *rlines,
        *rrlines,
        '</G>',
        clrs[2],
        *rrshape,
        '</G>',
    ]