import math

import numpy as np
from stl import mesh

from .text_gen import process_text_raw
from .utils import move, scale, generate_parallepiped


def generate_stat(level, offset_x=0, offset_y=0, offset_z=0):
    a = [offset_x + 0, offset_y + 0, 0 + offset_z]
    b = [offset_x + 0, offset_y + 1, 0 + offset_z]
    c = [offset_x + 1, offset_y + 1, 0 + offset_z]
    d = [offset_x + 1, offset_y + 0, 0 + offset_z]

    e = [offset_x + 0, offset_y + 0, level + offset_z]
    f = [offset_x + 0, offset_y + 1, level + offset_z]
    g = [offset_x + 1, offset_y + 1, level + offset_z]
    h = [offset_x + 1, offset_y + 0, level + offset_z]

    return generate_parallepiped(a, b, c, d, e, f, g, h)


def generate_pedestal():
    return generate_parallepiped(
        [3, -2, 0],
        [3, 9, 0],
        [-55, 9, 0],
        [-55, -2, 0],
        [2, -1, 3],
        [2, 8, 3],
        [-54, 8, 3],
        [-54, -1, 3],
    )


def generate_username_letters(username):
    letters = process_text_raw(username)
    # letters = process_text_raw("a" * 28)
    letters.rotate([1, 0, 0], math.radians(-90))
    letters.rotate([0, 0, 1], math.radians(180))
    letters.rotate([1, 0, 0], math.radians(-20))

    letters.vectors *= 0.20
    move(letters, -5, 21, 6)

    return letters


def generate_github_logo():
    github_logo = mesh.Mesh.from_file(f'assets/github.stl')
    scale(github_logo, 1, 1, 2)
    github_logo.rotate([1, 0, 0], math.radians(-90))
    github_logo.rotate([0, 0, 1], math.radians(180))
    github_logo.rotate([1, 0, 0], math.radians(-20))
    move(github_logo, -110, 30.5, 95)
    github_logo.vectors *= 0.35

    return github_logo


def generate_year_text(year):
    year_obj = process_text_raw(year)
    year_obj.rotate([1, 0, 0], math.radians(-90))
    year_obj.rotate([0, 0, 1], math.radians(180))
    year_obj.rotate([1, 0, 0], math.radians(-20))

    year_obj.vectors *= 0.20
    move(year_obj, -120, 21, 6)

    return year_obj


def generate_main_body(contribution_array):
    polygons = []

    # Generation of stats
    for y, x_values in enumerate(contribution_array):
        for x, level in enumerate(x_values):
            if level == 0:
                # If level is 0, all polygons are unnecessary (The height of generated mesh is also 0)
                continue
            polygons += generate_stat(math.sqrt(level) * 2.5, -x, y, 3)

    polygons += generate_pedestal()

    cube = mesh.Mesh(np.zeros(len(polygons), dtype=mesh.Mesh.dtype))
    for i, f in enumerate(polygons):
        cube.vectors[i] = f

    cube.vectors *= 2.58

    return cube
