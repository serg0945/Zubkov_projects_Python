import pygame
import random
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))  # Главное графическое окно игры
person_x = 80
person_y = 360
person_pos_x = 340
person_jump_vel = 8.5
keys = pygame.key.get_pressed()
x_pos_bg = 0
y_pos_bg = 400
cactus_y = 350
bird_y = 220
type_skin = random.randint(0, 2)
game_speed = 50
score = 0