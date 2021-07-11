from tank.Tank import Tank
from diection.Direction import *


class MyTank(Tank):

    COLOR = 'red'

    def __init__(self, x, y):
        super().__init__(x, y)
        self._direction = Direction(UP)
