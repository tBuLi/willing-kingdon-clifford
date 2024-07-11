from kingdon import Algebra

alg3d = Algebra(3, 0, 1)
options = dict(
    lineWidth=4,
    pointRadius=2.5,
    fontSize=3,
)
animated_options = dict(animate=0, **options)
clrs = [0xff9900, 0xfed290, 0x009977, 0x000000]
PLANE = alg3d.vector(e3=1)
ORIGIN = alg3d.blades.e0.dual() | PLANE