from location.Location import Location
from diection.Direction import *
from bullet.Bullet import Bullet


class Tank(object):
    COLOR = ""
    WIDTH = 3
    HEIGHT = 3

    def __init__(self, x, y):
        self._location = Location(x, y)
        self._direction = None
        self._bullet = None

    def move_up(self):
        if not self._direction.turn_up():
            self._location.move_up()

    def move_down(self):
        if not self._direction.turn_down():
            self._location.move_down()

    def move_left(self):
        if not self._direction.turn_left():
            self._location.move_left()

    def move_right(self):
        if not self._direction.turn_right():
            self._location.move_right()

    def _get_bullect_begin_location(self):
        if Direction(UP) == self._direction:
            return 1, -1
        elif Direction(DOWN) == self._direction:
            return 1, 3
        elif Direction(LEFT) == self._direction:
            return -1, 1
        elif Direction(RIGHT) == self._direction:
            return 3, 1
        else:
            return None

    def get_blank_locations(self):
        if Direction(UP) == self._direction:
            return [(0, 0), (2, 0)]
        elif Direction(DOWN) == self._direction:
            return [(0, 2), (2, 2)]
        elif Direction(LEFT) == self._direction:
            return [(0, 0), (0, 2)]
        elif Direction(RIGHT) == self._direction:
            return [(2, 0), (2, 2)]
        else:
            return []

    def send_bullet(self):
        if self._bullet:
            return
        location = self._get_bullect_begin_location()
        bullet = Bullet(self.x + location[0], self.y + location[1], self._direction.direction)
        self._bullet = bullet

    def disappear_bullet(self):
        if not self._bullet:
            return
        del self._bullet
        self._bullet = None

    @property
    def bullect(self):
        return self._bullet

    @property
    def x(self):
        return self._location.x

    @property
    def y(self):
        return self._location.y
