import timeit
import numpy as np
import itertools

from ..config import clrs, ptap, ltap, arrow
from . import normalized

alg = ltap

t_label = alg.vector(e0=1, e1=0.1, e2=1.7).dual()
x_label = alg.vector(e0=1, e1=1.8, e2=-0.3).dual()
master_clock = alg.vector(e0=1, e1=-0.12, e2=-0.16).dual()
ep, em = alg.vector(e1=1, e2=1), alg.vector(e1=1, e2=-1)

N_clocks = 5
T_x = alg.evenmv(e=np.ones(N_clocks), e01=0.5*np.linspace(-1, 1, N_clocks))
T_t = alg.evenmv(e=np.ones(N_clocks), e02=0.5*np.linspace(-1, 1, N_clocks))
clocks = T_x >> master_clock
clock_labels_1 = ["⏳", "⏳", "🕛", "⏳", "⏳"]
clock_labels_2 = ["⏳", "🕐", "🕐", "🕐", "⏳"]
clock_labels_3 = ["🕑", "🕑", "🕑", "🕑", "🕑"]

wl1 = -alg.blades.e1
wl2 = normalized(-alg.vector(e1=1, e2=-0.4))
wl1_label = alg.vector(e0=1, e1=-0.1, e2=1.4).dual()
wl2_label = alg.vector(e0=1, e1=1.8, e2=-0.3).dual()
bisector = normalized(wl1+wl2)
boost = bisector * wl2

def synchronize_base():
    return [
        0xffffff, t_label,  0, 'ct',
        0xffffff, x_label, 0, 'x',
        '<G stroke-width="0.003">',
        -alg.blades.e1, alg.blades.e2, 
        '</G>',
    ]
def synchronize_0():
    return [
        *synchronize_base(),
        0xffffff, master_clock, 0, "🕛",
    ]

def synchronize_1(clock_labels=clock_labels_1, translation=1):
    return [
        *synchronize_base(),
        0xffffff, *itertools.chain(*((c, label) for c, label in zip(translation >> clocks, clock_labels)))
    ]

def synchronize_2(clock_labels=clock_labels_1, translation=alg.evenmv(e=1, e02=-0.25)):
    ray1 = [alg.blades.e0.dual(), alg.vector(e0=1, e1=0.5, e2=0.5).dual()]
    ray2 = [alg.blades.e0.dual(), alg.vector(e0=1, e1=-0.5, e2=0.5).dual()]
    return [
        *synchronize_1(clock_labels=clock_labels, translation=translation),
        '<G stroke-dasharray="0.03 0.03">',
        clrs[2], ray1, ray2,
        '</G>',
    ]

def synchronize_3():
    return [
        *synchronize_2(clock_labels=clock_labels_2)
    ]

def synchronize_4():
    ray1 = [alg.blades.e0.dual(), alg.vector(e0=1, e1=1, e2=1).dual()]
    ray2 = [alg.blades.e0.dual(), alg.vector(e0=1, e1=-1, e2=1).dual()]
    return [
        *synchronize_2(clock_labels=clock_labels_2, translation=alg.evenmv(e=1, e02=-0.5)),
        '<G stroke-dasharray="0.03 0.03">',
        clrs[2], ray1, ray2,
        '</G>',
    ]

def synchronize_5():
    ray1 = [alg.blades.e0.dual(), alg.vector(e0=1, e1=1, e2=1).dual()]
    ray2 = [alg.blades.e0.dual(), alg.vector(e0=1, e1=-1, e2=1).dual()]
    return [
        *synchronize_2(clock_labels=clock_labels_3, translation=alg.evenmv(e=1, e02=-0.5)),
        '<G stroke-dasharray="0.03 0.03">',
        clrs[2], ray1, ray2,
        '</G>',
    ]

def make_grid(x_limits, t_limits, N_lines=5):
    T_x = alg.evenmv(e=np.ones(N_lines), e01=0.5*np.linspace(x_limits[0], x_limits[1], N_lines))
    T_t = alg.evenmv(e=np.ones(N_lines), e02=0.5*np.linspace(t_limits[0], t_limits[1], N_lines))
    ticks_x = alg.vector(e0=np.ones(2), e1=np.linspace(x_limits[0], x_limits[1], 2)).dual()
    ticks_t = alg.vector(e0=np.ones(2), e2=np.linspace(t_limits[0], t_limits[1], 2)).dual()
    axis_x = [ticks_x[0], ticks_x[-1]]
    axis_t = [ticks_t[0], ticks_t[-1]]
    axes_x = [T >> axis_x for T in T_t]
    axes_t = [T >> axis_t for T in T_x]
    return axes_x, axes_t

def synchronize_6():
    """ Show the resulting grid """
    axes_x, axes_t = make_grid((-1.5, 1.5), (-1.5, 1.5), 7)
    return [
        '<G stroke-opacity="0.3">',
        clrs[4],
        *axes_x,
        *axes_t,
        '</G>',
        '<G stroke-dasharray="0.03 0.03">',
        clrs[5], ep, em,
        '</G>',
        *synchronize_base(),
    ]

def synchronize_7():
    return [
        *synchronize_6(),
        '<G stroke-width="0.03" fill-opacity="0.003">',
        wl1, wl1_label,
        '</G>',	
         "ℓ₁",
    ]

def synchronize_8():
    return [
        *synchronize_6(),
        '<G stroke-width="0.03">',
        clrs[4], wl1, "ℓ",
        clrs[6], wl2, "ℓ'",
        '</G>',	
    ]

def synchronize_9():
    return [
        *synchronize_8(),
        0,
        '<G stroke-width="0.03" stroke-dasharray="0.03 0.03">',
        bisector, 
        # "ℓ₁ + ℓ₂",
        '</G>',	
    ]

def synchronize_10():
    axes_x, axes_t = make_grid((-1.5, 1.5), (-1.5, 1.5), 7)
    return [
        *synchronize_8(),
        '<G stroke-opacity="0.3">',
        clrs[6],
        *(~boost >> axes_x), 
        *(~boost >> axes_t), 
        # "ℓ₁ + ℓ₂",
        '</G>',	
    ]