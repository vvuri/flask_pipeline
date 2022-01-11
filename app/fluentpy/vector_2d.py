#  pytest .\vector_2d.py

from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __hash__(self):
        # vector length
        return hash(abs(self))


def test_add_two_vectors():
    assert hash(Vector(2, 3) + Vector(4, 1)) == hash(Vector(6, 4))
    assert hash(Vector(2, 3) + Vector(4, 1)) == hash(Vector(4, 6))


def test_as_string():
    assert repr(Vector(2, 3) + Vector(4, 1)) == repr(Vector(6, 4))
    assert repr(Vector(2, 3) + Vector(4, 1)) != repr(Vector(4, 6))


def test_zero_is_false():
    assert bool(Vector(0, 0)) is False


def test_not_zero_is_true():
    assert bool(Vector(1, 2)) is True


def test_scaling():
    assert hash(Vector(2, 3)*5) == hash(Vector(10, 15))
    assert hash(Vector(2, 4)*.5) == hash(Vector(1, 2))


def test_hash():
    assert hash(Vector(1, 2)) == hash(Vector(2, 1))
