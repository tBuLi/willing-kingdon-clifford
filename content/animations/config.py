from kingdon import Algebra

alg3d = Algebra(3, 0, 1)
alg2d = Algebra(2, 0, 1)
options = dict(
    lineWidth=4,
    pointRadius=2.5,
    fontSize=3,
    # clip=5,
)
animated_options = dict(animate=1, **options)
clrs = [
    0x1F91CA, 0x57BFED,  # blue
    0xF69B28, 0xFEC074,  # orange
    0x0C3353, 0x1A5B8F,
    0x34BAC4, 0x82DFE4,
    0xBF0E1C, 0xEA575C,
    0x640021, 0x941F4B,
    0x000000
]  # ECM colors
# clrs = [0xff9900, 0xfed290, 0x009977, 0x000000]
PLANE = alg3d.vector(e3=1)
ORIGIN = alg3d.blades.e0.dual() | PLANE