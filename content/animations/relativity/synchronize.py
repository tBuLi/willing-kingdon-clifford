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

clock_labels_1 = ["⌛", "⌛", "⌛", "⌛", "🕛", "⌛", "⌛", "⌛", "⌛"]
clock_labels_2 = ["⌛", "⌛", "⌛", "⌛", "🕐", "⌛", "⌛", "⌛", "⌛"]
clock_labels_3 = ["⌛", "⌛", "⌛", "🕐", "🕐", "🕐", "⌛", "⌛", "⌛"]
clock_labels_4 = ["⌛", "⌛", "⌛", "🕑", "🕑", "🕑", "⌛", "⌛", "⌛"]
clock_labels_5 = ["⌛", "⌛", "🕑", "🕑", "🕑", "🕑", "🕑", "⌛", "⌛"]
N_clocks = len(clock_labels_1)
T_x = alg.evenmv(e=np.ones(N_clocks), e01=0.5*np.linspace(-2, 2, N_clocks))
T_t = alg.evenmv(e=np.ones(N_clocks), e02=0.5*np.linspace(-2, 2, N_clocks))
clocks = T_x >> master_clock

wl1 = normalized(-alg.blades.e1)
wl2 = normalized(-alg.vector(e1=1, e2=-0.4))
wl1_label = alg.vector(e0=1, e1=-0.2, e2=1.4).dual()
wl2_label = alg.vector(e0=1, e1=0.7, e2=1.4).dual()
bisector = normalized(wl1+wl2)
boost = bisector * wl2
lorentz_factor = -wl1|wl2

# firework1 = alg.vector(e0=1, e1=1.38, e2=-0.16).dual()
# firework2 = alg.vector(e0=1, e1=-1.62, e2=-0.16).dual()
firework1 = alg.vector(e0=1, e1=-1.5).dual()
firework2 = alg.vector(e0=1, e1=1.5).dual()

def synchronize_base():
    return [
        '<G fill-opacity="0.0">', t_label, '</G>', clrs[-3], 'ct',
        '<G fill-opacity="0.0">', x_label, '</G>', clrs[-3], 'x',
        '<G stroke-width="0.003">',
        -alg.blades.e1, alg.blades.e2, 
        '</G>',
    ]
def synchronize_0():
    return [
        *synchronize_base(),
        '<G fill-opacity="0.0">', master_clock, '</G>', clrs[-3], "🕛",
    ]

def synchronize_1(clock_labels=clock_labels_1, translation=1):
    return [
        *synchronize_base(),
        *itertools.chain(*(('<G fill-opacity="0.0">', c, '</G>', clrs[-3], label) for c, label in zip(translation >> clocks, clock_labels))),
    ]

def synchronize_2(clock_labels=clock_labels_2, translation=alg.evenmv(e=1, e02=-0.25)):
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
        *synchronize_2(clock_labels=clock_labels_3)
    ]

def synchronize_4():
    ray1 = [alg.blades.e0.dual(), alg.vector(e0=1, e1=1, e2=1).dual()]
    ray2 = [alg.blades.e0.dual(), alg.vector(e0=1, e1=-1, e2=1).dual()]
    return [
        *synchronize_2(clock_labels=clock_labels_4, translation=alg.evenmv(e=1, e02=-0.5)),
        '<G stroke-dasharray="0.03 0.03">',
        clrs[2], ray1, ray2,
        '</G>',
    ]

def synchronize_5():
    ray1 = [alg.blades.e0.dual(), alg.vector(e0=1, e1=1, e2=1).dual()]
    ray2 = [alg.blades.e0.dual(), alg.vector(e0=1, e1=-1, e2=1).dual()]
    return [
        *synchronize_2(clock_labels=clock_labels_5, translation=alg.evenmv(e=1, e02=-0.5)),
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

axes_x, axes_t = make_grid((-1.5, 1.5), (-1.5, 1.5), 7)
axes_xp, axes_tp = (~boost >> axes_x), (~boost >> axes_t) 

def synchronize_6():
    """ Show the resulting grid """
    return [
        '<G stroke-opacity="0.3">',
        clrs[1],
        *axes_x,
        *axes_t,
        '</G>',
        '<G stroke-dasharray="0.03 0.03">',
        clrs[7], ep, em,
        '</G>',
        *synchronize_base(),
    ]

def synchronize_7():
    return [
        *synchronize_6(),
        '<G stroke-width="0.03" fill-opacity="0.001">',
        clrs[1], wl1, wl1_label,
        '</G>',	
         "ℓ",
    ]

def synchronize_8():
    return [
        *synchronize_7(),
        '<G stroke-width="0.03" fill-opacity="0.001">',
        clrs[5], wl2, wl2_label,
        '</G>',
        "ℓ'",
    ]

def synchronize_9():
    return [
        *synchronize_8(),
        clrs[6],
        '<G stroke-width="0.03" fill-opacity="1.0">',
        firework1,
        '</G>',
        "1", 
        '<G stroke-width="0.03" fill-opacity="1.0">',
        firework2,
        '</G>',
        "2",
    ]

def synchronize_10():
    return [
        *synchronize_9(),
        clrs[5],
        '<G stroke-width="0.03" stroke-dasharray="0.03 0.03">',
        bisector, 
        # "ℓ₁ + ℓ₂",
        '</G>',	
    ]

def synchronize_11():
    return [
        *synchronize_9(),
        '<G stroke-opacity="0.3">',
        clrs[5],
        *axes_xp, 
        *axes_tp, 
        # "ℓ₁ + ℓ₂",
        '</G>',	
    ]

def synchronize_12(t):
    t = min(t, 1.0)
    L = (-t*boost.grade(2)).exp()
    return [x if isinstance(x, (int, float, str)) else L >> x for x in synchronize_11()]


# TIME DILATION
scene_time_dilation_prime = [
    '',
    clrs[-3],
    f'γ={lorentz_factor}',
    *synchronize_8(),
    '<G stroke-opacity="0.3">',
    clrs[5],
    *axes_xp,
    *axes_tp,
    '</G>',	
]
scene_time_dilation_prime = [x if isinstance(x, (int, float, str)) else boost >> x for x in scene_time_dilation_prime]
tick1p, tick2p = alg.vector(e0=1, e1=0, e2=1).dual(), alg.vector(e0=1, e1=0, e2=0).dual()
def time_dilation_0():
    return [
        *scene_time_dilation_prime,
        clrs[4], [tick1p, tick2p], "T'",
        clrs[4], tick1p, f' {2*tick1p.e01:.2f}', tick2p,
    ]

def time_dilation_1(t):
    t = min(t, 1.0)
    L = (t*boost.grade(2)).exp()
    return [x if isinstance(x, (int, float, str)) else L >> x for x in time_dilation_0()]

scene_time_dilation = [x if isinstance(x, (int, float, str)) else ~boost >> x for x in time_dilation_0()]
tick1, tick2 = ~boost >> [tick1p, tick2p]
mark1 = tick1 @ wl1
mark2 = tick2 @ wl1
def time_dilation_2():
    return [
        *scene_time_dilation,
        clrs[3], [mark2, mark1], "T",
        clrs[3],
        mark1, f'{-2*mark1.e01:.2f}',
    ]

def time_dilation_3():
    p = tick1p@normalized(boost >> wl1)
    l = (p & tick2p)
    return [
        *time_dilation_0(),
        clrs[3], p, f'{2*(-l.normsq().e)**0.5:.2f}', l,
    ]


# Length Contraction
backp1 = normalized(alg.evenmv(e=1, e01=0.25) * boost >> wl2)
backp2 = normalized(alg.evenmv(e=1, e01=0.5) * boost >> wl2)
back1 = ~boost >> backp1
back2 = ~boost >> backp2
wlp1 = boost >> wl1
wlp2 = boost >> wl2
p1 = alg.evenmv(e=1, e01=0.25) * boost >> tick2
p2 = alg.evenmv(e=1, e01=0.5) * boost >> tick2
length_prime = (p1 & p2).norm().e

def length_contraction_0():
    return [
        *scene_time_dilation_prime,
        '<G stroke-dasharray="0.05 0.05">',
        clrs[4], -backp1, "b'", -backp2, "f'",
        '</G>',
        p1, p2, [p1, p2],
    ]

scene_length_contraction_prime = [x if isinstance(x, (int, float, str)) else ~boost >> x for x in length_contraction_0()]
xtick1, xtick2 = normalized(alg.blades.e2^back1), normalized(alg.blades.e2^back2)
length = (xtick1 & xtick2).norm().e
def length_contraction_1(t):
    t = min(t, 1.0)
    L = (t*boost.grade(2)).exp()
    return [x if isinstance(x, (int, float, str)) else L >> x for x in length_contraction_0()]

def length_contraction_2():
    return [
        *scene_length_contraction_prime,
    ]

def length_contraction_3():
    return [
        *scene_length_contraction_prime,
        clrs[3], xtick1, f'{2*length:.2f}', xtick2, [xtick1, xtick2],
    ]

def length_contraction_4(t):
    t = min(t, 1.0)
    L = (t*~boost.grade(2)).exp()
    return [x if isinstance(x, (int, float, str)) else L >> x for x in length_contraction_3()]