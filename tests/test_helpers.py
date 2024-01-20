from src.helpers import Point, haversine
from src.model import NorthPole
import pytest
from pytest import approx


def test_neutral():
    distance = haversine(NorthPole, NorthPole)
    assert distance == approx(0)


@pytest.mark.parametrize("a, b, distance", (
        (NorthPole, (38.8976, -77.0366), 5682.3),
        (NorthPole, (69.9496, -17.0366), 2229.5),
        (NorthPole, (-45.1354, 54.6312), 15026.3),
        ((69.9496, -17.0366), (-45.1354, 54.6312), 14026.0)
))
def test_to_north_pole(a: Point, b: Point, distance: float):
    assert haversine(a, b) == approx(distance, abs=0.1)
