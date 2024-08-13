import timeit
import numpy as np
import ipywidgets as ipy

from .config import alg3d, clrs, PLANE, ORIGIN

lens = alg3d.vector(e0=0, e1=1, e2=0, e3=0).normalized()
axis = alg3d.vector(e0=0, e1=0, e2=1, e3=0).normalized() ^ PLANE

# It is these lines that we will regret later
focal = alg3d.vector(e0=1, e1=-0.8, e2=0, e3=0).dual()  # Focal point of the lens
center = center_point = alg3d.vector(e0=1, e1=0, e2=0, e3=0).dual()  # Center of the lens
world = alg3d.vector(e0=1, e1=-2, e2=-1, e3=0).dual() # World to image

wf = lambda: world & focal
wc = lambda: world & center
wfl = lambda: wf ^ lens  # world on lens through focal
wfl_dot_l = lambda: wfl | (center_point & wfl)
img = lambda: alg3d.op(wfl_dot_l, wc)

def lens_graph_func_0():
    # 2d lens formula
    return [
        '<G stroke-opacity="0.5">',
        axis, 
        '</G>',
        clrs[2],
        world,
        clrs[0],
        lens ^ PLANE,
        center,
        focal, 'f',
        '<G stroke-dasharray="0.1 0.1">', clrs[1],
        wf,
        wc,
        wfl,
        lens | wfl,
        '</G>',
        '<G fill-opacity="0.2">', clrs[1],
        [world, img, wfl],
        '</G>',
        clrs[3],
        img,
    ]
