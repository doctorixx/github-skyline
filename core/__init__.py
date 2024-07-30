import math

import numpy as np
from stl import mesh

from .github_api import get_contributions
from .utils import *


def process_github_stats(username, year, filename):
    polygons = []
    contributions = get_contributions(username, year)
    contribution_array = generate_contribution_array(contributions)

    # Generation of stats
    for y, x_values in enumerate(contribution_array):
        for x, level in enumerate(x_values):
            polygons += generate_stat(math.sqrt(level) * 2.5, -x, y, 3)

    polygons += generate_pedestal()

    cube = mesh.Mesh(np.zeros(len(polygons), dtype=mesh.Mesh.dtype))
    for i, f in enumerate(polygons):
        cube.vectors[i] = f

    cube.save(filename)


def process_text(text, filename):
    objs = []
    x_pos = 0
    for letter in text.upper():
        obj = mesh.Mesh.from_file(f'assets/{letter}.stl')
        obj.vectors *= (1 / 2)

        move(obj, x_pos, 0, 0)
        x_pos += get_w(obj, 1)
        objs.append(obj)

    combined = mesh.Mesh(numpy.concatenate([to_render.data for to_render in objs]))

    combined.save(filename)
