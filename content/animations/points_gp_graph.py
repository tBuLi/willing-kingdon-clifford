import timeit
import numpy as np
import ipywidgets as ipy

from .config import alg3d, clrs, PLANE, ORIGIN, CAMERA

# Product of two points, with sliders. # TODO: also show the 3D perspective?
p1plane1 = alg3d.vector(e0=1.0, e1=1.0, e2=0.0).normalized()
p1plane2 = alg3d.vector(e0=1.0, e1=0.0, e2=1.0).normalized()
p2plane1 = alg3d.vector(e0=-1.0, e1=1.0, e2=0.0).normalized()
p2plane2 = alg3d.vector(e0=-1.0, e1=0.0, e2=1.0).normalized()
p1l1 = p1plane1 ^ PLANE
p1l2 = p1plane2 ^ PLANE
axis1 = p1plane1 ^ p1plane2
p1 = axis1 ^ PLANE
p2l1 = p2plane1 ^ PLANE
p2l2 = p2plane2 ^ PLANE
axis2 = p2plane1 ^ p2plane2
p2 = axis2 ^ PLANE
p1plane3 = axis1 | p1
p2plane3 = axis2 | p2

p1_slider = ipy.FloatSlider(
    value=0.0,
    min=-1.0,
    max=1.0,
    step=0.05,
    description='',
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)
p2_slider = ipy.FloatSlider(
    value=0.0,
    min=-1.0,
    max=1.0,
    step=0.05,
    description='',
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)


def planeat(p, x, y=0.5):
    [a,b,c,d] = [alg3d.vector(e0=1, e1=pair[0], e2=pair[1]).dual() for pair in [(y, y), (y, -y), (-y, -y), (-y, y)]]
    rot = (1 + alg3d.blades.e3 / p).normalized()
    trans = (1 + x / alg3d.blades.e123).normalized()
    return trans*rot >> [[a,b,c],[a,c,d]]

def cross(x,y=0.75):
    return [*planeat(alg3d.blades.e2,x,y), *planeat(alg3d.blades.e1,x,y), *planeat(alg3d.blades.e3,x,y)]

def points_gp_graph_func():
    R1 = np.cos(0.25*np.pi*p1_slider.value) + axis1*np.sin(0.25*np.pi*p1_slider.value)
    R2 = np.cos(0.25*np.pi*p2_slider.value) + axis2*np.sin(0.25*np.pi*p2_slider.value)
    _p1l1 = R1 >> p1l1
    _p1l2 = R1 >> p1l2
    _p2l1 = R2 >> p2l1
    _p2l2 = R2 >> p2l2
    _p1plane1 = R1 >> p1plane1
    _p2plane1 = R2 >> p2plane1
    
    # _p1 = _p1l1.cp(_p1l2) ^ PLANE
    # _p2 = _p2l1.cp(_p2l2) ^ PLANE
    _p1 = p1
    _p2 = p2
    if abs((_p1plane1 ^ _p2).dual().e) < 1e-3 and abs((_p2plane1 ^ _p1).dual().e) < 1e-3:
        return [
            clrs[0],
            _p1l2, _p1, 'a',
            '<G stroke-opacity="0.1">',
            _p1l1,
            '</G>',
            clrs[2],
            _p2l2, _p2, "b",
            '<G stroke-dasharray="0.1 0.1" stroke-opacity="0.1">',
            _p2l1,
            '</G>',
        ]
    return [
        clrs[0],
        _p1l1, _p1l2, _p1, 'a',
        clrs[2],
        _p2l1, _p2l2, _p2, "b",
    ]

def points_gp_graph_func_3d():
    R1 = np.cos(0.25*np.pi*p1_slider.value) + axis1*np.sin(0.25*np.pi*p1_slider.value)
    R2 = np.cos(0.25*np.pi*p2_slider.value) + axis2*np.sin(0.25*np.pi*p2_slider.value)
    _p1plane1, _p1plane2, _p1plane3 = _p1planes = R1 >> [p1plane1, p1plane2, p1plane3]
    _p2plane1, _p2plane2, _p2plane3 = _p2planes = R2 >> [p2plane1, p2plane2, p2plane3]

    c1 = R1 >> cross(p1)
    c2 = R2 >> cross(p2)
    if abs((_p1plane1 ^ p2).dual().e) < 1e-3 and abs((_p2plane1 ^ p1).dual().e) < 1e-3:
        return [
            '<G fill-opacity="0.1">',
            clrs[0],
            *c1[2:], 
            '</G>',
            *c1[:2], p1, 'a',
            '<G fill-opacity="0.1">',
            clrs[2],
            *c2[2:],
            '</G>',
            *c2[:2], p2, "b",
        ]
    return [
        '<G fill-opacity="0.6">',
        clrs[0],
        *c1, 
        '</G>',
        p1, 'a',
        '<G fill-opacity="0.6">',
        clrs[2],
        *c2,
        '</G>',
        p2, "b",
    ]
    
