def generate_rect(a, b, c, d):
    return [a, b, c], [a, c, d]


def generate_stat(x, y, level):
    a = [0, 0, 0]
    b = [0, 1, 0]
    c = [1, 1, 0]
    d = [1, 0, 0]

    e = [0, 0, level]
    f = [0, 1, level]
    g = [1, 1, level]
    h = [1, 0, level]

    polygons = [

    ]
