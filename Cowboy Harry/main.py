import random
from assets import *
from person import Person
from barrier import Cactus, Bird
import sys
import global_vars
from other import Other

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("assets/music.mp3")
pygame.mixer.music.play(-1)
keys = pygame.key.get_pressed()


def run():
    pygame.display.set_caption("Cowboy Harry")
    person = Person()
    bird = Bird()
    cactus = Cactus()
    other = Other()
    run = True
    music_pause = False
    background = pygame.image.load('assets/Background.png').convert()
    background = pygame.transform.smoothscale(background, global_vars.screen.get_size())

    while run:
        clock = pygame.time.Clock()  # Объект, который отслеживает время
        keys = pygame.key.get_pressed()  # Возвращает информацию о состояниях клавиш в виде кортежа.
        # Если клавиша с определенным индексом нажата, то в этом кортеже ее значение будет 1, а если отжата, то 0.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Без этой строки будет ошибка pygame.error: display Surface quit

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:  # Функция отключения музыки
                    music_pause = not music_pause
                    if music_pause:
                        pygame.mixer.music.pause()
                    else:   # Функция включения музыки во время паузы
                        pygame.mixer.music.unpause()

            if event.type == pygame.KEYDOWN:  # Функция уменьшения и увеличения звука
                vol = 0.5
                if event.key == pygame.K_MINUS:  # Функция уменьшения звука
                    vol -= 0.3
                    pygame.mixer.music.set_volume(vol)
                if event.key == pygame.K_EQUALS:  # Функция уменьшения звука
                    vol += 0.2
                    pygame.mixer.music.set_volume(vol)

        clock.tick(25)  # Скорость игры

        if keys[pygame.K_ESCAPE]:  # Кнопка Esc для паузы
            other.pause()

        if keys[pygame.K_x]:  # Кнопка X для замедления игры
            clock.tick(20)

        if keys[pygame.K_c]:  # Кнопка C для убийства птицы
            bird.rect.x = global_vars.screen_width + random.randint(600, 1000)
            person.shoot()

        if keys[pygame.K_1]:  # Кнопка 1 для представления жёлтого квадрата на персонаже
            person.output_min_person()

        if keys[pygame.K_2]:  # Кнопка 2 для представления жёлтого квадрата на кактусе
            cactus.output_min_cactus()

        if keys[pygame.K_3]:  # Кнопка 3 для представления жёлтого квадрата на птице
            bird.output_min_bird()

        # Система столкновений
        if person.person_rect.colliderect(cactus.rect) or person.person_rect.colliderect(bird.rect):
            pygame.time.delay(1000)
            other.pause()
            cactus.rect.x = global_vars.screen_width + random.randint(0, 400)
            bird.rect.x = global_vars.screen_width + random.randint(400, 800)

        # Вызов функций
        other.track()
        other.score()
        person.output(global_vars.screen)  # Если убрать атрибут screen, то будет набор ошибок
        person.update(keys)
        cactus.update()
        cactus.output(global_vars.screen)
        bird.output(global_vars.screen)
        bird.update()
        pygame.display.update()
        global_vars.screen.blit(background, (0, 0))
        # screen.fill(bg_color)  # Если убрать это, то будет дублирование объектов на экране


run()
