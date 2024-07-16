import timeit
import numpy as np

from .config import alg3d, clrs, PLANE

# Input for the graph showing point-reflections in 1D, tilting into 2D.
pa = alg3d.vector(e0=1, e1=0.5, e2=0).dual()
pb = alg3d.vector(e0=1, e1=-1.5, e2=0).dual()
L4 = alg3d.vector(e2=1).normalized()

line = (L4 ^ PLANE).normalized()
T1 = alg3d.evenmv(e=1.0, e01=0.4)
T2 = alg3d.evenmv(e=1.0, e03=-1.0)
_begin_point_line = alg3d.evenmv(e=1.0, e01=-5) >> pa
_end_point_line = alg3d.evenmv(e=1.0, e01=5) >> pa
vanishing_point = ((line | pa) ^ L4) ^ alg3d.blades.e0

line_point_end = alg3d.vector(e0=1, e1=2, e2=0).dual().normalized()
line_point_begin = alg3d.vector(e0=2, e1=2, e2=0).dual().normalized()
line_segment = [line_point_begin, line_point_end]
line_segment_a = [pa >> point for point in line_segment]
line_segment_b = [pb >> point for point in line_segment_a]

grid_lines = [
    [T1.reverse() >> (T2 >> pa), vanishing_point], 
    [T2.reverse() >> _begin_point_line, T2.reverse() >> _end_point_line]
]
for i in range(5):
    gl1 = grid_lines[-2]
    gl2 = grid_lines[-1]
    grid_lines.append([T1 >> gl1[0], gl1[1]])
    grid_lines.append([~T2 >> gl2[0], ~T2 >> gl2[1]])
t0 = None


def refl_1d_graph_func_0():
    return [
        [_begin_point_line, _end_point_line],
        pa, 'a',
        '<G stroke-width="0.05">',
        clrs[0],
        line_segment,
        line_segment[-1],
        '</G>',
    ]

def refl_1d_graph_func_1():
    return [
        [_begin_point_line, _end_point_line],
        pa, 'a',
        '<G stroke-width="0.05">',
        clrs[0],
        line_segment,
        line_segment[-1],
        '</G>',
        '<G stroke-width="0.05">',
        clrs[2],
        line_segment_a,
        line_segment_a[-1],
        '</G>',
    ]

def refl_1d_graph_func_2():
    return [
        [_begin_point_line, _end_point_line],
        pa, 'a',
        pb, 'b',
        '<G stroke-width="0.05">',
        clrs[0],
        line_segment,
        line_segment[-1],
        '</G>',
        '<G stroke-width="0.05">',
        clrs[2],
        line_segment_a,
        line_segment_a[-1],
        '</G>',
        '<G stroke-width="0.05">',
        clrs[0],
        line_segment_b,
        line_segment_b[-1],
        '</G>',
    ]

def refl_1d_graph_func_3():
    global t0
    if t0 is None:
        t0 = timeit.default_timer()
    t = timeit.default_timer() - t0
    if t > 10:
        t0 = None

    omega = -min(t / 25, np.pi / 20)
    R = np.cos(omega) + line * np.sin(omega)
    
    return [
        [_begin_point_line, _end_point_line],
        '<G stroke-width="0.02" stroke-opacity="0.5">',
        *[[R >> gl[0], R >> gl[1]] for gl in grid_lines],
        '</G>',
        '<G stroke-width="0.05">',
        pa, 'a',
        pb, 'b',
        '</G>',
        '<G stroke-width="0.05">',
        clrs[0],
        line_segment,
        line_segment[-1],
        '</G>',
        '<G stroke-width="0.05">',
        clrs[2],
        line_segment_a,
        line_segment_a[-1],
        '</G>',
        '<G stroke-width="0.05">',
        clrs[0],
        line_segment_b,
        line_segment_b[-1],
        '</G>',
    ]