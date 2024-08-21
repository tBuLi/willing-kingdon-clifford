import numpy as np

from .config import alg3d, clrs, PLANE, ORIGIN

np.random.seed(42)
coords = np.ones((4, 15))
coords[1:] = np.random.uniform(-1.5, 1.5, size=(3, 15))
pc = alg3d.vector(coords).dual()
avg = pc.map(np.mean)

def graph_pc_func():
    return [
        pc, 
        clrs[0], avg
    ]