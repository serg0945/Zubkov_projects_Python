from assets import *
import global_vars

pygame.init()

keys = pygame.key.get_pressed()

class Person:

    def __init__(self):
        self.attraction_img = person_attraction  #Изображение притягивания
        self.run_img = [person_running_1, person_running_2]  #Изображения бега
        self.jump_img = person_jump  #Изображение прыжка
        self.shoot_img = [person_shoot_1, person_shoot_2]  # Изображения стрельбы
        self.jump_vel = global_vars.person_jump_vel
        self.image = self.run_img[0]  # get_rect не принимает list, поэтому беру первый индекс
        self.person_rect = self.image.get_rect()  # Определение координат
        self.person_rect.x = global_vars.person_x  # Координаты по x
        self.person_rect.y = global_vars.person_y  # Координаты по y
        self.img_count = 0
        self.person_run = True
        self.person_jump = False
        self.person_attraction = False

    def update(self, keys):  # Главная функция взаимодействия пользователя с горячими клавишами

        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:  # Прыжок
            self.person_attraction = False
            self.person_run = False
            self.person_jump = True

        if self.person_jump:
            self.jump()

        if keys[pygame.K_DOWN]:  # Притягивание
            self.person_attraction = True
            self.person_run = False
            self.person_jump = False

        if self.person_attraction:
            self.attraction()

        if not (self.person_jump or keys[pygame.K_DOWN]):   # Бег
            self.person_attraction = False
            self.person_run = True
            self.person_jump = False

        if self.person_run:
            self.run()

        # Чтобы персонаж после прыжка не проваливался под землю и для реализации притяжения
        if (self.jump_vel < -global_vars.person_jump_vel) or keys[pygame.K_DOWN]:
            self.person_jump = False  # Чтобы после прыжка он не прыгал сам по себе
            self.jump_vel = global_vars.person_jump_vel


    def attraction(self):
        self.image = self.attraction_img
        self.person_rect = self.image.get_rect()
        self.person_rect.x = global_vars.person_x
        self.person_rect.y = global_vars.person_y

    def run(self):
        self.image = self.run_img[self.img_count // 4]
        self.person_rect = self.image.get_rect()
        self.person_rect.x = global_vars.person_x
        self.person_rect.y = global_vars.person_y
        self.img_count += 1

        if self.img_count == 8:  # Анимация бега
            self.img_count = 0

    def jump(self):
        self.image = self.jump_img

        if self.person_jump:
            self.person_rect.y -= self.jump_vel * 3  # Высота прыжка
            self.jump_vel -= 1  # Для падения персонажа. Если поставить плюс, то персонаж улетит за экран

    def shoot(self):
        self.image = self.shoot_img[self.img_count // 4]
        self.img_count += 1

        if self.img_count == 8:  # Анимация бега
            self.img_count = 0

    def output(self, screen):
        # screen.blit(self.image[self.img_count], (self.person_rect.x, self.person_rect.y)) : # 'pygame.surface.Surface' object is not subscriptable
        screen.blit(self.image, (self.person_rect.x, self.person_rect.y))  # Вывод изображения (персонаж) с его координатами

    def output_min_person(self):
        pygame.draw.rect(global_vars.screen, (247, 240, 22), self.person_rect)  # Жёлтый квадрат
