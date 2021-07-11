class Location(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move_up(self):
        self._y -= 1

    def move_down(self):
        self._y += 1

    def move_left(self):
        self._x -= 1

    def move_right(self):
        self._x += 1

    def move_direction(self, direction):
        self._x += direction[0]
        self._y += direction[1]

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
