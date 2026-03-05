from kingdon import Algebra

alg3d = Algebra(3, 0, 1)
alg2d = Algebra(2, 0, 1)
ltap = Algebra(signature=[0, -1, 1])
# ltap = Algebra(signature=[0, 1, -1])
ptap = Algebra(signature=[0, -1, -1, 1])
stap = Algebra(signature=[0, -1, -1, -1, 1])
# ptap = Algebra(signature=[0, -1, 1], basis=['e', 'e0', 'e2', 'e1', 'e01', 'e02', 'e12', 'e012'])
# ltap = Algebra(signature=[0, -1, -1, 1])
# stap = Algebra(signature=[0, -1, -1, -1, 1])

CAMERA = alg3d.blades.e
options = dict(
    lineWidth=4,
    pointRadius=2.5,
    fontSize=3,
    style=dict(background='transparent')
    # clip=5,
)
animated_options = dict(animate=1, **options)
science_options = dict(grid=1, labels=1, **options)
clrs = [
    0x8BE9FD, 0x50FA7B,  # cyan, green
    0xFFB86C, 0xF1FA8C,  # orange, yellow
    0xFF79C6, 0xBD93F9,  # pink, purple
    0xFF5555, 0x6272A4,  # red, comment
    0xF8F8F2, 0x44475A,  # foreground, current line
    0x282A36             # background
]  # Dracula colors
# clrs = [0xff9900, 0xfed290, 0x009977, 0x000000]
PLANE = alg3d.vector(e3=1)
ORIGIN = alg3d.blades.e0.dual() | PLANE

def arrow( from_point, to_point, w=0.03, aspect=0.8, camera=1):
    alg = from_point.algebra
    e0 = alg.blades.e0
    from_point = from_point/(-from_point|e0.dual())
    to_point = to_point/(-to_point|e0.dual())
    line = ( from_point & to_point )
    l = line.norm().e
    shape = [
        alg.vector(e0=1, e1=x, e2=y).dual()
        for x, y in [[0,w],[l-5*w,w],[l-5*w,aspect*5*w],[l,0],[l-5*w,-aspect*5*w],[l-5*w,-w],[0,-w]]
    ]
    sqrt = lambda R: alg.blades.e12 if abs(R.e + 1.0) < 1e-8 else (1+R).normalized()
    R = ((to_point - from_point).undual()).normalized() * alg.blades.e1
    R2 = sqrt(from_point/e0.dual()) * sqrt(R.filter())
    return R2 >> shape