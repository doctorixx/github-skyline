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
