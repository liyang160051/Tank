UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Direction(object):

    def __init__(self, direction=UP):
        self._direction = direction

    def turn_up(self):
        return self._turn_direction(UP)

    def turn_down(self):
        return self._turn_direction(DOWN)

    def turn_left(self):
        return self._turn_direction(LEFT)

    def turn_right(self):
        return self._turn_direction(RIGHT)

    def _turn_direction(self, direction):
        if direction == self._direction:
            return False
        self._direction = direction
        return True

    @property
    def direction(self):
        return self._direction

    def __eq__(self, other):
        return self._direction == other.direction
