import timeit
import numpy as np

from .config import alg2d, clrs

a = alg2d.vector(e1=2, e0=1).normalized()
b = alg2d.vector(e1=2, e2=1, e0=-0.4).normalized()
R = b/a
c = (a+b).normalized()

def sqrt_graph_func_0():
    return [
        '<G stroke-width="0.02">',
        clrs[0], b, 'b',
        a, 'a',
        '</G>',
    ]

def sqrt_graph_func_1():
    return [
        '<G stroke-width="0.02">',
        clrs[0], b, 'b',
        a, 'a',
        clrs[2], R >> a, 'R a R⁻¹',
        '</G>',
    ]

def sqrt_graph_func_2():
    return [
        '<G stroke-width="0.02">',
        clrs[0], b, 'b',
        a, 'a',
        '</G>',
        clrs[1], 
        '<G stroke-width="0.02" stroke-opacity="0.5">',
        c, 'a+b',
        '</G>',
    ]

def sqrt_graph_func_3():
    return [
        '<G stroke-width="0.02">',
        clrs[0], 
        b,
        a, 'a',
        '</G>',
        clrs[1], 
        '<G stroke-width="0.02" stroke-opacity="0.5">',
        c, 'a+b',
        '</G>',
        clrs[2],
        '<G stroke-dasharray="0.05 0.05">',
        R.sqrt() >> a, '(√R) a (√R)⁻¹',
        '</G>',
    ]