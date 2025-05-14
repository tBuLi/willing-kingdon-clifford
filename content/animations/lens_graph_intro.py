import timeit
import numpy as np
import ipywidgets as ipy

from .config import alg2d, clrs

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

lens = alg2d.vector(e0=0, e1=1, e2=0, e3=0).normalized()
axis = alg2d.vector(e0=0, e1=0, e2=1, e3=0).normalized()

# It is these lines that we will regret later
focal = alg2d.vector(e0=1, e1=-0.8, e2=0, e3=0).dual()  # Focal point of the lens
center = center_point = alg2d.vector(e0=1, e1=0, e2=0, e3=0).dual()  # Center of the lens
world = alg2d.vector(e0=1, e1=-2, e2=-1, e3=0).dual() # World to image
# Arbitrary point
arbitrary = alg2d.vector(e0=1, e1=-1, e2=-1.7, e3=0).dual()

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
        img, 'img',
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
        img, 'img',
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
        wc, 'w ∨ c',
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
        wf, 'w ∨ f',
        wc, #'w ∨ c',
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
        wf, #'w ∨ f',
        wc, #'w ∨ c',
        wfl, '(w ∨ f) ∧ ℓ',
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
        wfl, #'(w ∨ f) ∧ ℓ',
        # lens | wfl,
        wfl_dot_l, '((w ∨ f) ∧ ℓ) ⋅ ℓ',
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
        img,'(w ∨ c) ∧ [((w ∨ f) ∧ ℓ) ⋅ ℓ]',
    ]

def lens_graph_intro_func_01():    
    return ([
        *lens_graph_intro_func_0(),
        clrs[9], arbitrary, 'O',
        arrow(arbitrary, center),
    ])

def lens_graph_intro_func_02():
    return ([
        *lens_graph_intro_func_01(),
        arrow(arbitrary, world),
    ])

def lens_graph_intro_func_03():
    return ([
        *lens_graph_intro_func_02(),
        arrow(arbitrary, focal),
    ])

def lens_graph_intro_func_04():
    return ([
        *lens_graph_intro_func_03(),
        clrs[8],
        arrow(center_point, focal), 'a',
        arrow(center_point, world), 'b',
    ])
