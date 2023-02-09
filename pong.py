import pygame, sys

class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.dx = 0
        self.dy = 0
        self.show()

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

    def start_moving(self):
        self.dx = 15  #adjust ball speed
        self.dy = 5

    def move(self):
        self.posX += self.dx
        self.posY += self.dy

class Paddle:
    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.state = 'stopped'
        self.show()

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))

    def move(self):
        if self.state == 'up':
            self.posY -= 10 #adjust paddle speed when given movement command

        elif self.state == 'down':
            self.posY += 10



pygame.init()
clock = pygame.time.Clock()

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


# VARIABLES
playing = False

#main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                ball.start_moving()
                playing = True

            if event.key == pygame.K_w:
                paddle1.state = 'up'

            if event.key == pygame.K_s:
                paddle1.state = 'down'

            if event.key == pygame.K_UP:
                paddle2.state = 'up'

            if event.key == pygame.K_DOWN:
                paddle2.state = 'down'

        if event.type == pygame.KEYUP:
            paddle1.state = 'stopped'
            paddle2.state = 'stopped'

    #ball movement intialized
    if playing:
        paint_back()
        ball.move()
        ball.show()

        #paddle1
        paddle1.move()
        paddle1.show()

        #paddle2
        paddle2.move()
        paddle2.show()


    pygame.display.update()
    clock.tick(22.5) #FPS of game