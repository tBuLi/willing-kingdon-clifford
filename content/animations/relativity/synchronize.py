import timeit
import numpy as np
import itertools

from ..config import clrs, ptap, ltap

alg = ltap

t_label = alg.vector(e0=1, e1=0.1, e2=1.5).dual()
x_label = alg.vector(e0=1, e1=1.5, e2=-0.3).dual()
master_clock = alg.vector(e0=1, e1=-0.12, e2=-0.16).dual()
ep, em = alg.vector(e1=1, e2=1), alg.vector(e1=1, e2=-1)

N_clocks = 5
T = alg.evenmv(e=np.ones(N_clocks), e01=0.5*np.linspace(-1, 1, N_clocks))
clocks = T >> master_clock
clock_labels_1 = ["⏳", "⏳", "🕛", "⏳", "⏳"]
clock_labels_2 = ["⏳", "🕐", "🕐", "🕐", "⏳"]
clock_labels_3 = ["🕑", "🕑", "🕑", "🕑", "🕑"]

def synchronize_base():
    return [
        -alg.blades.e1, alg.blades.e2, 
        0xffffff, t_label,  0, 'ct',
        0xffffff, x_label, 0, 'x',
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