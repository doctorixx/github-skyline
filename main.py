import numpy as np
from stl import mesh

from utils import *

# Define the 8 vertices of the cube
vertices = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [1, 0, 0],

    [0, 0, 1],
    [0, 1, 1],
    [1, 1, 1],
    [1, 0, 1],

    [0 + 1, 0, 0],
    [0 + 1, 1, 0],
    [1 + 1, 1, 0],
    [1 + 1, 0, 0],

    [0 + 1, 0, 1],
    [0 + 1, 1, 1],
    [1 + 1, 1, 1],
    [1 + 1, 0, 1],

])
# Define the 12 triangles composing the cube

# a, b = generate_rect(0, 1, 2, 3)

faces = np.array([
    *generate_rect(0, 1, 2, 3),
    *generate_rect(4, 5, 6, 7),

    *generate_rect(0, 4, 7, 3),
    *generate_rect(0, 4, 5, 1),
    *generate_rect(2, 3, 7, 6),
    *generate_rect(1, 5, 6, 2),




    *generate_rect(0 + 8, 1 + 8, 2 + 8, 3 + 8),
    *generate_rect(4 + 8, 5 + 8, 6 + 8, 7 + 8),

    *generate_rect(0 + 8, 4 + 8, 7 + 8, 3 + 8),
    *generate_rect(0 + 8, 4 + 8, 5 + 8, 1 + 8),
    *generate_rect(2 + 8, 3 + 8, 7 + 8, 6 + 8),
    *generate_rect(1 + 8, 5 + 8, 6 + 8, 2 + 8),
])

# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[f[j], :]

# Write the mesh to file "cube.stl"
cube.save('cube.stl')
