from location.Location import Location
from diection.Direction import *


class Bullet(object):

    _speed = 1

    def __init__(self, x, y, direction=UP):
        self._location = Location(x, y)
        self._direction = Direction(direction)

    def run(self):
        for _ in range(self._speed):
            self._location.move_direction(self._direction.direction)

    @property
    def x(self):
        return self._location.x

    @property
    def y(self):
        return self._location.y

