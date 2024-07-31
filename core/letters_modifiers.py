from .utils import move

FIXED_OFFSETS = {
    "I": 10,
    "J": 10,
    "K": 25,
    "M": 25,
    "N": 23,
    "R": 23,
    "W": 32,
    "X": 25,
    "-": 15,
}

FIXED_POSITION_MODIFIER = {
    "-": lambda obj: move(obj, 0, -15, 0),
    "default": lambda _: None
}
