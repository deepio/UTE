from random import randint

from python_example import __version__
from python_example.base import Rectangle, Square


def test_version():
  assert __version__ == '0.1.0'

################################################################################
# Integration Tests
def test_rectangle():
  w, h = randint(-9223372036854775807,9223372036854775807), randint(-9223372036854775807,9223372036854775807)
  a = Rectangle(w, h)
  assert a.area == w * h

def test_square():
  s = randint(-9223372036854775807,9223372036854775807)
  a = Square(s)
  assert a.area == s * s
