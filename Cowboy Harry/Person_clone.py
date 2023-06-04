import pygame
from assets import *
import global_vars

pygame.init()

keys = pygame.key.get_pressed()


class Person:

    def __init__(self):
        self.bend_img = person_bend_1
        self.run_img = [person_running_1, person_running_2]
        self.jump_img = person_jump
        self.jump_vel = global_vars.person_jump_vel
        self.image = self.run_img[0]  # get_rect не принимает list, поэтому беру первый индекс
        self.person_rect = self.image.get_rect()
        self.person_rect.x = global_vars.person_x
        self.person_rect.y = global_vars.person_y
        self.img_count = 0
        self.person_run = True
        self.person_jump = False
        self.person_bend = False

    def update(self, keys):

        if self.person_bend:
            self.bend()
        if self.person_run:
            self.run()
        if self.person_jump:
            self.jump()

        if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and not self.person_jump:
            self.person_bend = False
            self.person_run = False
            self.person_jump = True

        if keys[pygame.K_DOWN]:
            self.person_bend = True
            self.person_run = False
            self.person_jump = False

        if not (self.person_jump or keys[pygame.K_DOWN]):
            self.person_bend = False
            self.person_run = True
            self.person_jump = False

        # Чтобы персонаж после прыжка не проваливался под землю и для реализации крюка
        if (self.jump_vel < -global_vars.person_jump_vel) or keys[pygame.K_DOWN]:
            self.person_jump = False  # Чтобы после прыжка он не прыгал сам по себе
            self.jump_vel = global_vars.person_jump_vel

    def bend(self):
        self.image = self.bend_img  # Чем меньше число, тем больше скорость обновления анимации
        self.person_rect = self.image.get_rect()
        self.person_rect.x = global_vars.person_x
        self.person_rect.y = global_vars.person_y

    def run(self):
        self.image = self.run_img[self.img_count // 4]
        self.person_rect = self.image.get_rect()
        self.person_rect.x = global_vars.person_x
        self.person_rect.y = global_vars.person_y
        self.img_count += 1

        if self.img_count == 8:
            self.img_count = 0

    def jump(self):
        self.image = self.jump_img

        if self.person_jump:
            self.person_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8 # Если поставить плюс, то персонаж улетит за экран


    def output(self, screen):
        #screen.blit(self.image[self.img_count], (self.person_rect.x, self.person_rect.y)) : # 'pygame.surface.Surface' object is not subscriptable
        screen.blit(self.image, (self.person_rect.x + 20, self.person_rect.y - 30))

    def output_min_person(self):
        pygame.draw.rect(global_vars.screen, (247, 240, 22), self.person_rect)

