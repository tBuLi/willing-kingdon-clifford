import timeit
import numpy as np
import ipywidgets as ipy

from .config import alg3d, clrs, PLANE, ORIGIN

p = alg3d.vector(e0=1, e1=-1).dual()
l = alg3d.vector(e0=-1, e1=1, e2=1).normalized() ^ PLANE
l1, l2, axis = p | [alg3d.blades.e1, alg3d.blades.e2, alg3d.blades.e3]

proj_slider = ipy.FloatSlider(
    value=0.0,
    min=-1.0,
    max=1.0,
    step=0.1,
    description='',
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

proj_selector = ipy.Dropdown(
    options=[('a⋅b', 1), ('(a⋅b)b', 2), ('(a⋅b)a', 3)],
    value=1,
    description='Display:',
    disabled=False,
)

def proj_graph_func():
    if proj_selector.value != 1:
        proj_slider.value = 0.5
    R = np.cos(0.25*np.pi*proj_slider.value) + axis*np.sin(0.25*np.pi*proj_slider.value)
    l1p, l2p = R >> [l1, l2]

    if proj_selector.value == 1:
        if abs((l2p | l).e) < 1e-3:
            return [
                clrs[0],
                '<G stroke-opacity="0.2" fill-opacity="0.2">',
                l1p, p, 'a',
                '</G>',
                l2p, 'a⋅b',
                clrs[2],
                '<G stroke-opacity="0.2" fill-opacity="0.2">',
                l, 'b',
                '</G>',
            ]
        return [
            clrs[0],
            l1p, l2p,
            p, 'a',
            clrs[2],
            l,
            "b",
        ]
    elif proj_selector.value == 2:
        return [
            clrs[0],
            '<G stroke-opacity="0.2" fill-opacity="0.2">',
            l1p, p, 'a',
            '</G>',
            l2p,
            clrs[2],
            l,
            '<G stroke-opacity="0.2" fill-opacity="0.2">',
            'b',
            '</G>',
            (l2p.cp(l) ^ PLANE), '(a⋅b)b'
        ]
    else:
        return [
            clrs[0],
            l1p, '(a⋅b)a',
            '<G stroke-opacity="0.2" fill-opacity="0.2">',
            l2p, p, 'a',
            '</G>',
            clrs[2],
            '<G stroke-opacity="0.2" fill-opacity="0.2">',
            l, 'b',
            '</G>',
        ]
        