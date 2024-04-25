#####################################################################
# author:   
# date:    
# description: 
#####################################################################
import pygame
from random import randint, choice
from Item import *
from Constants import *


class Person(pygame.sprite.Sprite, Item):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Item.__init__(self,name="player 1", x=0, y=0)
        
        self.color = (0, 0 ,0)
        self.surf = pygame.Surface(self.size)
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()

    def setColor(self):
        self.color = [random.randint(0,255) for i in range(3)]
        self.surf.fill(self.color)

    def setSize(self):
        self.size = random.randint(10, 100), random.randint(10,100)
        self.surf = pygame.Surface(self.size)
        self.surf.fill(self.color)

    def update(self,pressedKeys):
        if pressedKeys[pygame.K_UP]:
            self.goUp()
        if pressedKeys[pygame.K_DOWN]:
            self.goDown()
        if pressedKeys[pygame.K_LEFT]:
            self.goLeft()
        if pressedKeys[pygame.K_RIGHT]:
            self.goRight()
        if pressedKeys[pygame.K_SPACE]:
            self.setSize()
            self.setColor()
            self.setRandomPosition()
    
    def goUp(self):
        self.rect.y -= 10

    def goDown(self):
        self.rect.y += 10

    def goLeft(self):
        self.rect.x -= 10

    def goRight(self):
        self.rect.x +=10

    def setRandomPosition(self):
        self.rect.x = randint(0, WIDTH-self.rect.width)
        self.rect.y = randint(0, HEIGHT - self.rect.height)

    def getPosition(self):
        return self.rect.topleft()

        
    def __str__(self):
        return f"Person color: {self.color}"


########################### main game################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()



