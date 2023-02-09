import pygame, sys

class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.show()

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

class Paddle:
    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.show()

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))




pygame.init()

WIDTH = 900
HEIGHT = 500

BLACK = (0,0,0) #RGB notation
WHITE = (255,255,255)

screen = pygame.display.set_mode(( WIDTH, HEIGHT))
pygame.display.set_caption('Pong')


def paint_back():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH//2,0), (WIDTH//2, HEIGHT), 5)

paint_back()

# OBJECTS

ball = Ball(screen, WHITE, WIDTH//2, HEIGHT//2, 15)
paddle1 = Paddle(screen, WHITE, 15, HEIGHT//2-60, 20, 120 )
paddle2 = Paddle(screen, WHITE, WIDTH - 20 - 15, HEIGHT//2-60, 20, 120)

#main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()