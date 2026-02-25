from .synchronize import synchronize_6
from ..config import ltap, clrs
import numpy as np
import timeit
np.random.seed(43)

alg = ltap
N_events = 5
events = alg.vector(e0=np.ones(N_events), e1=np.random.uniform(-2, 2, N_events), e2=np.random.uniform(-2, 2, N_events)).dual()
wl1 = events[0] & events[1]
wl2 = events[3] & events[4]
wl3 = ((1.3*alg.blades.e01).exp() >> wl2)
wl4 = ((1.4*alg.blades.e01).exp() >> wl2)
wl5 = alg.vector(e0=1.5, e1=1.0, e2=0.3)
wl6 = alg.vector(e0=1.5, e1=0.8, e2=0.5)

def elements_events():
    return [
        *synchronize_6(),
        clrs[0],
        events,
    ]

def elements_world_lines():
    return [
        *elements_events(),
        wl1,
        wl2,
    ]

def elements_world_planes():
    return [
        *elements_world_lines(),
        '<G fill-opacity=0.5>',
        [events[2], events[1], events[4]],
        '</G>'
    ]

def elements_bireflections():
    t = 0.1*np.sin(0.5*timeit.default_timer())
    
    T = (0.5*t*wl3^wl4).exp()
    R = (2.5*t*wl5^wl6).exp()
    return [
        *elements_world_planes(),
        clrs[2],
        T >> wl3,
        T >> wl4,
        R >> wl5,
        R >> wl6,
    ]