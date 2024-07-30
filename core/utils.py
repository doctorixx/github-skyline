import datetime

import numpy


def generate_rect(a, b, c, d):
    return [a, b, c], [a, c, d]


def generate_parallepiped(a, b, c, d, e, f, g, h):
    return [
        *generate_rect(a, b, c, d),
        *generate_rect(e, f, g, h),

        *generate_rect(e, h, d, a),
        *generate_rect(h, d, c, g),
        *generate_rect(c, g, f, b),
        *generate_rect(e, f, b, a),
    ]


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


def generate_contribution_array(github_data) -> list:
    contribution_array = [[0] * 54 for _ in range(7)]

    first_day = list(map(int, github_data[0]["date"].split("-")))
    first_day_of_year = datetime.date(first_day[0], first_day[1], first_day[2])

    offset = first_day_of_year.isoweekday()

    for i, value in enumerate(github_data):
        x = (i + offset) // 7
        y = (i + offset) % 7

        contribution_array[y][x] = value['count']

    return contribution_array


def move(your_mesh, tx, ty, tz):
    for i in range(0, len(your_mesh.vectors)):
        for j in range(0, len(your_mesh.vectors[i])):
            your_mesh.vectors[i][j] = your_mesh.vectors[i][j] + numpy.array([tx, ty, tz])


def get_w(your_mesh, axis):
    arr = []

    for i in range(0, len(your_mesh.vectors)):
        for j in range(0, len(your_mesh.vectors[i])):
            arr.append(your_mesh.vectors[i][j][axis])

    return max(arr) - min(arr)
