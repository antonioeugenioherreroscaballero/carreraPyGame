import pygame, sys, random

from pygame.locals import *

class Runner():
    __customes = ('turtle', 'fish','prawn', 'moray', 'octopus')

    def __init__(self, x = 0, y = 0): 

       ixCustom = random.randint(0,4)

       self.custome = pygame.image.load("assets/{}.png".format(self__customes[ixCustome]))
       self.position = [x,y]
       self.name =""

class Game():

    def __init__(self):

        ixCustom = random.randint(0,4)
        self.__screen = pygame.display.set_mode((640, 480))
        self.background = pygame.image.load("assets/background.png")
        pygame.display.set_caption("Carrera de bichos")

        self.runners = Runner(320,240)

    def start(self):
        gameOver= False
       
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.type == K_UP:
                        self.runner.position[1] -= 5 
                        # Mover hacia arriba Runner
                    elif event.type == K_DOWN:
                        self.runner.position[1] += 5 
                         # Mover hacia abajo Runner
                    elif event.type == K_LEFT:
                        self.runner.position[0] -= 5 
                        # Mover hacia izquierda Runner
                    elif event.type == K_RIGHT:
                        self.runner.position[0] += 5 
                        # Mover hacia derecha Runner
                    elif:
                        pass
  

            self.__screen.blit(self.background(0,0))
            self.__screen.blit(self.runner.custome, self.runner.position)

            pygame.display.flip() 
            

if __name__ == '__main__':
    
    game = Game()
    pygame.init()
    
      