import timeit
import itertools
import warnings

import numpy as np
from kingdon import Algebra
import ipywidgets as ipy
from lapygaga import diamond, diamond_mechanism, fivebar, fivebar_mechanism, arm, arm_mechanism, jsonreader
from lapygaga.mechanisms.mechanisms import LineType, PointType
from lapygaga.objectives import MechanismFitness

from .config import clrs, alg2d

# Algebras
dualalg = Algebra(0, 0, 1)

# Make widgets
tangent_widget = ipy.Checkbox(
    value=False,
    description='Derivative',
    disabled=False,
    indent=False
)

mechanism_widget = ipy.Dropdown(
    options=[('Diamond', 0), ('Fivebar', 1),],
    value=0,
    # description='Mechanism:',
)

recompute_widget = ipy.Button(
    description=f'Fit',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Execute fitting',
    icon='arrows-rotate' # (FontAwesome names without the `fa-` prefix)
)

def perform_fit(button):
    global obj_value, params, points, pairs, mechanism_fitness, mechanism, coordinates, objective
    mechanism = diamond_mechanism if mechanism_widget.value == 0 else fivebar_mechanism 
    mechanism_fitness = MechanismFitness(
        topology=mechanism.topology,
        target_coordinates=target_coords,
        algebra=alg2d,
        dual_numbers=dualalg
    )
    coordinates = np.array([[(q := p.undual()).e1, q.e2] for p in points]).T
    with warnings.catch_warnings():  
        # Ignore RuntimeWarning: invalid value encountered in sqrt, because I do not work with complex numbers here.
        warnings.simplefilter("ignore")
        obj_value = mechanism_fitness(coordinates=coordinates)
    params = tuple(float(v) for v in mechanism_fitness.fit_results.params.values())
    objective = mechanism_fitness.objective
    for p, q in zip(points, objective.points):
        for i, v in enumerate(q.values()):
            p._values[i] = v
    # points = [p.map(float) for p in objective.points]  # Cast back to python float so the graph is interactive.
    pairs = [key for key, idx in mechanism.connection_indices.items() if mechanism.topology[idx] and len(key) == 2]
    recompute_widget.description=f'Fit ({obj_value:.2f})'

mechanism_widget.observe(perform_fit, names='value')
recompute_widget.on_click(perform_fit)

# Function to form lines from given points on the basis of the pairs extracted from the mechanism.
def lines(points, pairs):
    return [[points[i], points[j]] for i, j in pairs]



# GLOBALS
mechanism = diamond_mechanism
target_coords = np.array([[0.15, 0.5,  0.85], [0.3,  0.5,  0.2 ]])
coordinates = np.array([
        0.476018975165776,
        0.6260100093482048,
        0.8753453209080457,
        0.5839114813135214,
        0.5038412869978799,
        0.22729782583687924,
        0.3014745071957209,
        0.45242577563985825,
        0.452673007868295,
        0.27690001725029845
    ]).reshape((2, mechanism.n_points))
mechanism_fitness = MechanismFitness(
    topology=mechanism.topology,
    target_coordinates=target_coords,
    algebra=alg2d,
    dual_numbers=dualalg
)
obj_value = mechanism_fitness(coordinates=coordinates)
# Extract the best fit parameters, these are the polynomial values which determine the angle(s). Convert to float again.
params = tuple(float(v) for v in mechanism_fitness.fit_results.params.values())
objective = mechanism_fitness.objective
points = [p.map(float) for p in objective.points]  # Cast back to python float so the graph is interactive.
target_points = objective.target_points
pairs = [key for key, idx in mechanism.connection_indices.items() if mechanism.topology[idx] and len(key) == 2]



def graph_mechanism_func():
    global obj_value, params, points, pairs, mechanism_fitness, mechanism, coordinates, objective
    # Work over dual numbers for automatic differentiation.
    if tangent_widget.value:
        t = dualalg.multivector(e=0.5*np.sin(0.2*timeit.default_timer()) + 0.5, e0=1)
        dangles = objective.params_to_angles(params, t)
        changes = mechanism(points, dangles, [])
        # Extract the new points and the directions.
        changed_points     = [change.map(lambda v: v if isinstance(v, float) else v.e)  for change in changes]
        changed_directions = [change.map(lambda v: v.e0) for change in changes if len(change.shape) > 1]
        # Add these changed directions to the points to display tangent lines
        tangents = [[p, p + d] for p, d in zip(changed_points[1:-1], changed_directions)]
    else:
        t = 0.5*np.sin(0.2*timeit.default_timer()) + 0.5
        angles = objective.params_to_angles(params, t)
        changed_points = mechanism(points, angles, [])
        tangents = []

    return [
        clrs[2], *itertools.chain(*zip(target_points, ['X', 'Y', 'Z'])),
        '<G  stroke-width=0.02 stroke-dasharray="0.1" stroke-opacity="0.2" fill-opacity="0.2">',
        0x000000, #*itertools.chain(*zip(points, ['A', 'B', 'C', 'D', 'E'])),
        *lines(points, pairs),
        '</G>',
        # *itertools.chain(*zip(changed_points, ['A', 'B', 'C', 'D', 'E'])),
        *[p for j, p in enumerate(changed_points) if j not in mechanism.motor_indices],
        clrs[6], *[changed_points[i] for i in mechanism.end_indices],
        0x000000,
        '<G  stroke-width=0.02>',
        *lines(changed_points, pairs),
        '</G>',
        '<G  stroke-width=0.02>',
        clrs[0], *tangents,
        '</G>',
        0x000000, 
        *itertools.chain(*zip(points, ['A', 'B', 'C', 'D', 'E'])),
        clrs[8], *[points[i] for i in mechanism.motor_indices],
        clrs[7], *[points[i] for i in mechanism.end_indices],
    ]


def graph_usecase_func():
    return [
        clrs[2], *itertools.chain(*zip(target_points, ['X', 'Y', 'Z'])),
    ]

def graph_guess_func():
    return [
        clrs[2], *itertools.chain(*zip(target_points, ['X', 'Y', 'Z'])),
        '<G  stroke-width=0.02 stroke-dasharray="0.1" stroke-opacity="0.2" fill-opacity="0.2">',
        0x000000,
        *lines(points, pairs),
        '</G>',
        0x000000, 
        *itertools.chain(*zip(points, ['A', 'B', 'C', 'D', 'E'])),
        clrs[8], *[points[i] for i in mechanism.motor_indices],
        clrs[7], *[points[i] for i in mechanism.end_indices],
    ]