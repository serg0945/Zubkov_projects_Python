from barrier import Cactus
from assets import track
import global_vars
import random
import sys
import pygame
from person import Person

barrier = Cactus()
person = Person()
class Other:

    def print_text(self, message, x, y, font_color=(0, 0, 0), font_size=40):  # Вывод текста на экран
        font_type = pygame.font.Font('assets/Samson.ttf', font_size)
        text = font_type.render(message, True, font_color)
        global_vars.screen.blit(text, (x, y))

    def pause(self):  # Пауза
        pause = True
        global_vars.score = 0
        music_pause = False
        while pause:
            keys = pygame.key.get_pressed()  # Обязательно здесь должно быть, июо не будет работать
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:  # Функция отключения музыки во время паузы
                        music_pause = not music_pause
                        if music_pause:
                            pygame.mixer.music.pause()
                        else:  # Функция включения музыки во время паузы
                            pygame.mixer.music.unpause()

                if keys[pygame.K_RETURN]:  # if global_vars.keys[pygame.K_RETURN] не прокатит
                    pause = False

            self.print_text('Press enter to continue', 380, 275)
            self.print_text('Press DOWN for attraction to earth', 700, 15, font_size=30)
            self.print_text('Press x to slow down time', 840, 50, font_size=30)
            self.print_text('Press UP or Space to jump', 850, 85, font_size=30)
            self.print_text('Press 1,2 or 3 for rengen', 865, 120, font_size=30)
            self.print_text('Press c to kill bird', 920, 155, font_size=30)
            self.print_text('Press + to increase the sound', 25, 50, font_size=30)
            self.print_text('Press - to reduce the sound', 25, 85, font_size=30)
            self.print_text('Press backspace to turn off the sound', 25, 15, font_size=30)
            pygame.display.update()

    def track(self):  # Дорога
        image_width = track.get_width()
        global_vars.screen.blit(track, (global_vars.x_pos_bg, global_vars.y_pos_bg))
        global_vars.screen.blit(track, (image_width + global_vars.x_pos_bg, global_vars.y_pos_bg))  # Два blit, чтобы дорога не разрывалась
        if global_vars.x_pos_bg <= -image_width:
            global_vars.x_pos_bg = 0
        global_vars.x_pos_bg -= global_vars.game_speed

    def score(self):  # Очки
        barrier.rect.x -= global_vars.game_speed
        if barrier.rect.x < -global_vars.screen_width:  # Когда появляется Кактус, добавляется 2 очка
            barrier.rect.x = global_vars.screen_width + random.randint(0, 600)
            barrier.rect.x -= barrier.rect.width
            global_vars.score += 2
        self.print_text('Score: ' + str(global_vars.score), 1040, 15)