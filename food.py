import pygame
import random


class Food:
    def __init__(self, window, win_x, win_y, block_size=10, color=(0, 255, 0)):
        self._x = win_x
        self._y = win_y
        self._x_pos = 0
        self._y_pos = 0
        self._window = window
        self._color = color
        self._block_size = block_size
        self.has_food = False

    def create_food(self):
        if not self.has_food:
            self._x_pos = random.randint(0, self._x)
            self._y_pos = random.randint(0, self._y)
        pygame.draw.rect(self._window, self._color, (self._x_pos,
                                                    self._y_pos,
                                                    self._block_size,
                                                    self._block_size))
        self.has_food = True

    def empty_food(self):
        self.has_food = False

    def get_food_position(self):
        return [self._x_pos, self._y_pos]
