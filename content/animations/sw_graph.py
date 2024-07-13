import timeit
import numpy as np
import ipywidgets as ipy

from .config import alg3d, clrs, PLANE, ORIGIN

L1 = alg3d.vector(e1=1).normalized() ^ PLANE
L2 = alg3d.vector(e1=1, e2=0.5).normalized() ^ PLANE
intersection = L1.cp(L2)

sw_slider = ipy.FloatSlider(
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

def sw_graph_func():
    if sw_slider.value == 0.0:
        return [
            clrs[0],
            L1, 'a',
            clrs[2],
            L2, "b'",
            '<G stroke-dasharray="0.1 0.1">', clrs[1],
            L1, "a'",
            '</G>',
        ]
    elif sw_slider.value < 1.0:
        t = np.arccos((L1 | L2).e) * sw_slider.value
        R = np.cos(t / 2) + intersection*np.sin(t / 2)
        L2p = R >> L2
        L1p = R >> L1
        
        return [
            clrs[0],
            L1, 'a',
            clrs[2],
            L2p, "b'",
            clrs[1],
            L1p, "a'",
        ]
    else:
        R = (L1 * L2).sqrt()
        L2p = R >> L2
        L1p = R >> L1
        
        return [
            '<G fill-opacity="0.3" stroke-opacity="0.1">', 
            clrs[0],
            L1, 'a',
            '</G>',
            '<G stroke-opacity="0.3" fill-opacity="0.3" stroke-dasharray="0.1 0.1">', 
            clrs[2],
            L2p, "b'",
            '</G>',
            clrs[0],
            L1p, "a'",
        ]