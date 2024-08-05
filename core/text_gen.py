import os

import numpy
from stl import mesh

from .letters_modifiers import FIXED_POSITION_MODIFIER, FIXED_OFFSETS
from .utils import move, get_w


def process_text_raw(text):
    objs = []
    x_pos = 0
    for letter in text.upper():
        try:
            path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "assets", f"{letter}.stl"
            )

            obj = mesh.Mesh.from_file(path)
        except:
            path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "assets", "question_mark.stl"
            )

            obj = mesh.Mesh.from_file(path)
        # print(path)
        modifier = FIXED_POSITION_MODIFIER.get(letter, FIXED_POSITION_MODIFIER['default'])
        modifier(obj)

        obj.vectors *= (1 / 2)

        move(obj, x_pos, 0, 0)

        x_pos += FIXED_OFFSETS.get(
            letter,
            get_w(obj, 1)
        )
        objs.append(obj)

    combined = mesh.Mesh(numpy.concatenate([to_render.data for to_render in objs]))

    return combined
