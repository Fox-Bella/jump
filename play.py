import pygame
import time
import setup
from random import randint

# Делегировать - передавать, заставлять, просить кого-то сделать что-то

class Hero:

    def __init__(self, x=0, y=0, image_left="", image_right="", sx=0):
        self.x = x
        self.y = y
        self.image_left = pygame.image.load(image_left)
        self.image_right = pygame.image.load(image_right)

        self.sx = sx

    def draw(self, scene):
        if self.sx < 0:
            # Рисовать скин влево
            pass
        else:
            # Рисовать скин вправо
            pass

    def change_coordinates(self):
        if self.moving:
            self.x += self.sx
class Manager:

    def __init__(self):
        self.hero = Hero(x=200, y=800, image_left="image/hero-to-left.png", image_right="hero-to-right.png", sx=10)
        self.zlyden = Hero(x=50, y=800, image_left="image/hero-to-left.png", image_right="hero-to-right.png", sx=10)


    def draw(self, scene):
        self.hero.draw(scene)
        self.zlyden.draw(scene)


    def jump(self):
        pass


    def move(self):
        pass

    def rasst(self):
        for i in range(self.n - 1):
            for j in range(i + 1, self.n):
                a = abs(self.cir[i].x - self.cir[j].x)
                b = abs(self.cir[i].y - self.cir[j].y)
                c = abs(a * a + b * b) ** 0.5



                if c <= self.cir[i].radius + self.cir[j].radius:
                    # self.cir[i].moving = False
                    # self.cir[j].moving = False
                    self.cir[i].sx, self.cir[j].sx = self.cir[j].sx, self.cir[i].sx
                    self.cir[i].sy, self.cir[j].sy = self.cir[j].sy, self.cir[i].sy
                    self.cir[i].change_coordinates()
                    self.cir[j].change_coordinates()

    def shutting(self, x, y):
        # print(f"shutting: {x}, {y}")
        for i in range(self.n):
            a = abs(self.cir[i].x - x)
            b = abs(self.cir[i].y - y)
            c = abs(a * a + b * b) ** 0.5
            if c <= self.cir[i].radius:
                self.cir[i].set_start_time()

    def get_count_moving(self):
        summ = 0
        for i in range(self.n):
            summ += self.cir[i].moving

        return summ



pygame.init()
pygame.display.set_caption("Заставка :))))")
size = [setup.WIDTH, setup.HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()
playGame = True
deltatime = 0

m = Manager()

while playGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # print(f"Левая {pygame.mouse.get_pos()[0]}, {pygame.mouse.get_pos()[1]}")
                m.shutting(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            elif event.button == 3:
                # print(f"Правая {pygame.mouse.get_pos()[0]}, {pygame.mouse.get_pos()[1]}")
                m.shutting(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playGame = False
            elif event.key == pygame.K_UP:
                setup.f += 1
                if setup.f > 4:
                    setup.f = 0
            elif event.key == pygame.K_DOWN:
                setup.f -= 1
                if setup.f < 0:
                    setup.f = 4

    scene.fill(setup.c[setup.f])
    m.draw(scene)
    pygame.display.flip()

    m.move()
    m.rasst()

    if m.get_count_moving() == 0:
        m = None
        count_circle += 1
        m = Manager(count_circle)

    clock.tick(setup.FPS)