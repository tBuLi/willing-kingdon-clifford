import timeit
import numpy as np
import ipywidgets as ipy

from .config import alg2d, clrs

lens = alg2d.vector(e0=0, e1=1, e2=0, e3=0).normalized()
axis = alg2d.vector(e0=0, e1=0, e2=1, e3=0).normalized()

# It is these lines that we will regret later
focal = alg2d.vector(e0=1, e1=-0.8, e2=0, e3=0).dual()  # Focal point of the lens
center = center_point = alg2d.vector(e0=1, e1=0, e2=0, e3=0).dual()  # Center of the lens
world = alg2d.vector(e0=1, e1=-2, e2=-1, e3=0).dual() # World to image

wf = lambda: world & focal
wc = lambda: world & center
wfl = lambda: wf ^ lens  # world on lens through focal
wfl_dot_l = lambda: wfl | (center_point & wfl)
img = lambda: alg2d.op(wfl_dot_l, wc)

def lens_graph_intro_func_0():
    # 2d lens formula
    return [
        '<G stroke-opacity="0.5">',
        axis, 
        '</G>',
        clrs[2],
        world, 'w',
        clrs[0],
        lens, 'ℓ',
        center, 'c',
        focal, 'f',
        '<G stroke-dasharray="0.1 0.1">', clrs[1],
        wf,
        wc,
        wfl,
        # lens | wfl,
        wfl_dot_l,
        '</G>',
        '<G fill-opacity="0.2">', clrs[1],
        [world, img, wfl],
        '</G>',
        clrs[3],
        img,
    ]

def lens_graph_intro_func_1():
    # 2d lens formula
    return [
        '<G stroke-opacity="0.5">',
        axis, 
        '</G>',
        clrs[2],
        world, 'w',
        clrs[0],
        lens, 'ℓ',
        center, 'c',
        focal, 'f',
        '<G fill-opacity="0.2">',
        clrs[3],
        img,
        '</G>',
    ]

def lens_graph_intro_func_2():
    # 2d lens formula
    return [
        '<G stroke-opacity="0.5">',
        axis, 
        '</G>',
        clrs[2],
        world, 'w',
        clrs[0],
        lens, 'ℓ',
        center, 'c',
        focal, 'f',
        '<G stroke-dasharray="0.1 0.1">', clrs[1],
        wc,
        '</G>',
        '<G fill-opacity="0.2">',
        clrs[3],
        img,
        '</G>',
    ]

def lens_graph_intro_func_3():
    # 2d lens formula
    return [
        '<G stroke-opacity="0.5">',
        axis, 
        '</G>',
        clrs[2],
        world, 'w',
        clrs[0],
        lens, 'ℓ',
        center, 'c',
        focal, 'f',
        '<G stroke-dasharray="0.1 0.1">', clrs[1],
        wf,
        wc,
        # wfl,
        # # lens | wfl,
        # wfl_dot_l,
        '</G>',
        '<G fill-opacity="0.2">',
        clrs[3],
        img,
        '</G>',
    ]

def lens_graph_intro_func_4():
    # 2d lens formula
    return [
        '<G stroke-opacity="0.5">',
        axis, 
        '</G>',
        clrs[2],
        world, 'w',
        clrs[0],
        lens, 'ℓ',
        center, 'c',
        focal, 'f',
        '<G stroke-dasharray="0.1 0.1">', clrs[1],
        wf,
        wc,
        wfl,
        # # lens | wfl,
        # wfl_dot_l,
        '</G>',
        '<G fill-opacity="0.2">',
        clrs[3],
        img,
        '</G>',
    ]

def lens_graph_intro_func_5():
    # 2d lens formula
    return [
        '<G stroke-opacity="0.5">',
        axis, 
        '</G>',
        clrs[2],
        world, 'w',
        clrs[0],
        lens, 'ℓ',
        center, 'c',
        focal, 'f',
        '<G stroke-dasharray="0.1 0.1">', clrs[1],
        wf,
        wc,
        wfl,
        # lens | wfl,
        wfl_dot_l,
        '</G>',
        '<G fill-opacity="0.2">',
        clrs[3],
        img,
        '</G>',
    ]

def lens_graph_intro_func_6():
    # 2d lens formula
    return [
        '<G stroke-opacity="0.5">',
        axis, 
        '</G>',
        clrs[2],
        world, 'w',
        clrs[0],
        lens, 'ℓ',
        center, 'c',
        focal, 'f',
        '<G stroke-dasharray="0.1 0.1">', clrs[1],
        wf,
        wc,
        wfl,
        # lens | wfl,
        wfl_dot_l,
        '</G>',
        clrs[3],
        img,
    ]