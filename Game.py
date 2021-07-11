import time
import random
import tkinter as tk
from map.Map import Map
from tank.MyTank import MyTank
from tank.EnemyTank import EnemyTank


cell_size = 20
map_height = 30
map_width = 30
height = map_height * cell_size
width = map_width * cell_size


class Game(object):

    def __init__(self, canvas):
        self._tank_map = Map(map_width, map_height)
        self._my_tank = MyTank(int(self._tank_map.width / 2), self._tank_map.height - 3)
        self._enemy_tanks = [EnemyTank(int(self._tank_map.width / 2), 0), EnemyTank(0, 0)]
        self._canvas = canvas

    def draw_cell_by_cr(self, width, height, color="#CCCCCC"):
        x0 = width * cell_size
        y0 = height * cell_size
        x1 = width * cell_size + cell_size
        y1 = height * cell_size + cell_size
        self._canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black", width=1)

    # 绘制空白面板
    def draw_blank_board(self):
        for w in range(self._tank_map.width):
            for h in range(self._tank_map.height):
                self.draw_cell_by_cr(w, h)

    def draw_tank(self, tank, color='#CCCCCC'):
        for w in range(tank.x, tank.x + tank.WIDTH):
            for h in range(tank.y, tank.y + tank.HEIGHT):
                blank_locations = tank.get_blank_locations()
                if (w - tank.x, h - tank.y) in blank_locations:
                    continue
                self.draw_cell_by_cr(w, h, color=color)

    def draw_bullet(self, tank, color='#CCCCCC'):
        if not tank.bullect:
            return
        self.draw_cell_by_cr(tank.bullect.x, tank.bullect.y, color=color)

    def tank_bullet_run(self, tank):
        if self._can_tank_bullet_run(tank):
            self.draw_bullet(tank)
            tank.bullect.run()
            self.draw_bullet(tank, color=tank.COLOR)
            return
        tank.disappear_bullet()

    def _can_tank_bullet_run(self, tank):
        return 0 <= tank.bullect.x <= self._tank_map.width and \
               0 <= tank.bullect.y <= self._tank_map.height

    def draw_my_tank(self):
        self.draw_tank(self._my_tank, color=self._my_tank.COLOR)

    def draw_enemy_tanks(self):
        for tank in self._enemy_tanks:
            self.draw_tank(tank, color=tank.COLOR)

    def tank_move_up(self, tank):
        if not self._can_tank_move_up(tank):
            return
        self.draw_tank(tank)
        tank.move_up()
        self.draw_tank(tank, color=tank.COLOR)

    def _can_tank_move_up(self, tank):
        return self._tank_map.height - 3 >= tank.y > 0

    def tank_move_down(self, tank):
        if not self._can_tank_move_down(tank):
            return
        self.draw_tank(tank)
        tank.move_down()
        self.draw_tank(tank, color=tank.COLOR)

    def _can_tank_move_down(self, tank):
        return self._tank_map.height - 3 > tank.y >= 0

    def tank_move_left(self, tank):
        if not self._can_tank_move_left(tank):
            return
        self.draw_tank(tank)
        tank.move_left()
        self.draw_tank(tank, color=tank.COLOR)

    def _can_tank_move_left(self, tank):
        return self._tank_map.width - 3 >= tank.x > 0

    def tank_move_right(self, tank):
        if not self._can_tank_move_right(tank):
            return
        self.draw_tank(tank)
        tank.move_right()
        self.draw_tank(tank, color=tank.COLOR)

    def _can_tank_move_right(self, tank):
        return self._tank_map.width - 3 > tank.x >= 0

    def loop(self):
        self.loop_enemy_tanks()
        self.loop_bullets()

    def loop_bullets(self):
        if self._my_tank.bullect:
            self.tank_bullet_run(self._my_tank)
        for tank in self._enemy_tanks:
            if tank.bullect:
                self.tank_bullet_run(tank)

    def loop_enemy_tanks(self):
        actions = [self.tank_move_up] * 1 + [self.tank_move_down] * 3 + \
                  [self.tank_move_left] * 2 + [self.tank_move_right] * 2 + [self.tank_send_bullet] * 2
        for tank in self._enemy_tanks:
            action = random.choice(actions)
            action(tank)

    def tank_send_bullet(self, tank):
        tank.send_bullet()
        self.draw_bullet(tank, tank.COLOR)

    def loop_my_tank(self, event):
        cases = {
            'Up': self.tank_move_up,
            'Down': self.tank_move_down,
            'Left': self.tank_move_left,
            'Right': self.tank_move_right,
            'space': self.tank_send_bullet
        }
        action = cases.get(event.keysym)
        if action:
            action(self._my_tank)


def main():
    win = tk.Tk()
    canvas = tk.Canvas(win, width=width, height=height, )
    canvas.pack()

    FPS = 200  # 刷新页面的毫秒间隔

    game = Game(canvas)
    game.draw_blank_board()
    game.draw_my_tank()
    game.draw_enemy_tanks()
    canvas.focus_set()
    canvas.bind("<Key>", game.loop_my_tank)

    def game_loop():
        win.update()
        game.loop()

        # print(time.ctime())
        win.after(FPS, game_loop)

    win.after(FPS, game_loop)
    win.mainloop()

