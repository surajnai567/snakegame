import pygame
import snake
import player
import food


class App:
    def __init__(self, win_size=(500, 600)):
        self.win_size = win_size
        pygame.init()
        self.win = pygame.display.set_mode(win_size)

    def on_exe(self):
        my_snake = snake.Snake(self.win, 0, 0)
        play = player.Player()
        my_food = food.Food(self.win, self.win_size[0], self.win_size[1])
        run = True

        # main loop
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                my_snake.add_block(list(play.move_left()))
            elif keys[pygame.K_RIGHT]:
                my_snake.add_block(list(play.move_right()))
            elif keys[pygame.K_UP]:
                my_snake.add_block(list(play.move_up()))
            elif keys[pygame.K_DOWN]:
                my_snake.add_block(list(play.move_down()))

            # drawing objects
            self.win.fill((0, 0, 0))
            s_pos = my_snake.get_head_position()[0]
            f_pos = my_food.get_food_position()
            if s_pos[0] < 0 or s_pos[1] > self.win_size[1] or s_pos[0] > self.win_size[0] or s_pos[1] < 0:
                run = False
                print("game over")
            my_food.create_food()
            my_snake.draw_snake()
            if abs(s_pos[0] - f_pos[0]) < 6 and abs(s_pos[1] - f_pos[1]) < 6:
                my_food.empty_food()
                my_snake.increase_size()

            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    ap = App()
    ap.on_exe()
