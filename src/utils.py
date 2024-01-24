from math import sin, cos, asin, sqrt, radians
from typing import Tuple

Latitude = float
Longitude = float
Point = Tuple[Latitude, Longitude]

EARTH_RADIUS = 6371


def haversine(a: Point, b: Point) -> float:
    """
    Calculate haversine distance between two points

    :param a: First point
    :param b: Second point
    :return: Distance between points
    """
    a = tuple(map(radians, a))
    b = tuple(map(radians, b))
    delta_latitude: float = b[0] - a[0]
    delta_longitude: float = b[1] - a[1]
    d: float = sin(delta_latitude / 2) ** 2 + cos(a[0]) * cos(b[0]) * sin(
        delta_longitude / 2) ** 2
    e: float = 2 * asin(sqrt(d))

    return e * EARTH_RADIUS


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return func(*args, **kwargs)

    def clear_counter():
        wrapper.counter = 0

    wrapper.counter = 0
    wrapper.clear_counter = clear_counter

    return wrapper
