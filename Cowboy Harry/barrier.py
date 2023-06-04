from person import *
import random

pygame.init()

class Cactus:
    def __init__(self):
        self.img_list = [small_cactus_1, small_cactus_1_2, small_cactus_2, small_cactus_2_2,  small_cactus_3, small_cactus_3_2]
        self.img = self.img_list[0]
        self.rect = self.img.get_rect()  # Определение координат
        self.rect.x = global_vars.screen_width  # Координаты по x
        self.rect.y = global_vars.cactus_y  # Координаты по y

    def update(self):
        self.rect.x -= global_vars.game_speed  # Появление кактуса и его движение
        if self.rect.x < -global_vars.screen_width:  # Бесконечное появление кактусов
            global_vars.type_skin = random.randint(0, 2)  # Смена скинов
            self.rect.x = global_vars.screen_width + random.randint(0, 600)


    def output(self, screen):
        screen.blit(self.img_list[global_vars.type_skin], self.rect)  # Вывод изображения (кактусы) с его координатами

    def output_min_cactus(self):
        pygame.draw.rect(global_vars.screen, (247, 240, 22), (self.rect))  # Жёлтый квадрат


class Bird(Cactus):
    def __init__(self):
        super().__init__()
        self.img_list = [bird_1, bird_2]
        self.rect.y = global_vars.bird_y
        self.index = 0
        self.rect.x = global_vars.screen_width + random.randint(600, 1000)


    def output(self, screen):
        if self.index >= 9:  # Анимация птицы
            self.index = 0
        screen.blit(self.img_list[self.index // 5], self.rect)  # Вывод изображения (птица) с его координатами
        self.index += 1

    def output_min_bird(self):
        pygame.draw.rect(global_vars.screen, (247, 240, 22), (self.rect))  # Жёлтый квадрат
