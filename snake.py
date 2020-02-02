import pygame


class Snake:
    def __init__(self, win, x, y, color=(0, 0, 255)):
        self.x = x
        self.y = y
        self.color = color
        self.block = [[0, 0]]
        self.win = win
        self.snake_size = 1

    def draw_snake(self):
        if len(self.block) > self.snake_size:
            del self.block[0]
        for x, y in self.block:
            pygame.draw.rect(self.win, self.color, (x, y, 10, 10))
        print(self.block)

    def add_block(self, lis):
        self.block.append(lis)

    def increase_size(self):
        self.snake_size += 1

    def get_head_position(self):
        return self.block[-1:]

