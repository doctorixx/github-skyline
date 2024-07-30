import math

import numpy as np
from stl import mesh

from utils import *

from raw import DATA

# Define the 8 vertices of the cube


polygons = [
    # *generate_stat(0, 0, 2),
    # *generate_stat(1, 1, 1),
]

for y, x_values in enumerate(DATA):
    for x, level in enumerate(x_values):
        polygons += generate_stat(math.ceil(level * 0.75), -x, y, 4)

polygons += generate_parallepiped(
    [3, -2, 0],
    [3, 9, 0],
    [-55, 9, 0],
    [-55, -2, 0],
    [2, -1, 4],
    [2, 8, 4],
    [-54, 8, 4],
    [-54, -1, 4],
)

# Create the mesh
cube = mesh.Mesh(np.zeros(len(polygons), dtype=mesh.Mesh.dtype))
for i, f in enumerate(polygons):
    cube.vectors[i] = f

# Write the mesh to file "cube.stl"
cube.save('result.stl')
