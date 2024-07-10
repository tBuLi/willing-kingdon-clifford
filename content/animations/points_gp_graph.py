import timeit
import numpy as np
import ipywidgets as ipy

from .config import alg3d, clrs, PLANE, ORIGIN

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
