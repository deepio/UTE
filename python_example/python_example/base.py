import attr

@attr.s
class Rectangle:
  width = attr.ib(type=int,)
  height = attr.ib(type=int,)
  area = attr.ib(type=int,)
  @area.default
  def area_default(self):
    return self.width * self.height

class Square(Rectangle):
  def __init__(self, side):
    Rectangle.__init__(self, side, side)
    self.side = side

# @attr.s
# class Square:
#   side = attr.ib(type=int,)
#   area = attr.ib(type=int,)
#   @area.default
#   def area_default(self):
#     return Rectangle(self.side, self.side).area
