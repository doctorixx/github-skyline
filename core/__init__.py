import math
import os
import sys

import numpy as np
from stl import mesh

from .github_api import get_contributions
from .objects_gen import generate_username_letters, generate_github_logo, generate_year_text, generate_pedestal, \
    generate_main_body
from .text_gen import process_text_raw
from .letters_modifiers import FIXED_OFFSETS, FIXED_POSITION_MODIFIER
from .utils import *


def get_current_executable_directory():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(os.path.realpath(sys.executable))

    return os.getcwd()


def process_github_stats(username, year, filename):
    contributions = get_contributions(username, year)
    contribution_array = generate_contribution_array(contributions)

    body = generate_main_body(contribution_array)
    letters = generate_username_letters(username)
    year_obj = generate_year_text(year)
    github_logo = generate_github_logo()

    to_export = mesh.Mesh(numpy.concatenate([body.data, letters.data, year_obj.data, github_logo.data]))
    to_export.rotate([0, 0, 1], math.radians(180))

    path = os.path.join(
        get_current_executable_directory(), filename
    )

    to_export.save(path)


def process_text(text, filename):
    process_text_raw(text).save(filename)
