from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    prev: list[Point]

@dataclass(init=False)
class Circle:
    x: float
    y: float
    radius: float
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('x')
parser.add_argument('y')
parser.add_argument('radius')
circle = Circle(**vars(parser.parse_args("0.1 0.5 42".split())))
print(circle)