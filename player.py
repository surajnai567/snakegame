import pygame


class Player:
    def __init__(self):
        self.vel = 5
        self.x = 0
        self.y = 0
        self.x_change = 0
        self.y_change = 0

    def move_left(self):
        self.x_change = -self.vel
        self.y_change = 0
        self.x += self.x_change
        self.y +=self.y_change
        return self.x, self.y

    def move_right(self):
        self.x_change = +self.vel
        self.y_change = 0
        self.x += self.x_change
        self.y +=self.y_change
        return self.x, self.y

    def move_up(self):
        self.x_change = 0
        self.y_change = -self.vel
        self.x += self.x_change
        self.y += self.y_change
        return self.x, self.y

    def move_down(self):
        self.x_change = 0
        self.y_change = self.vel
        self.x += self.x_change
        self.y += self.y_change
        return self.x, self.y

