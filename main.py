import pygame
import sys

class Game():

    corredores = []
    __startLine = 20
    __finishLine = 620

    def __init__(self):

        self.__screen = pygame.display.set_mode((640, 480))
        self.background = pygame.image.load("assets/background.png")
        pygame.display.set_caption("Carrera de bichos")

        self.runner = pygame.image.load("assests/smallball.png")

    def competir(self):

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True

            self.__screen.blit(self.background(0,0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()

        pygame.quit()
        sys.exit()

      '''  x = 0
        hayGanador = False

        while True:
            #Comprobacion de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Refrescar / renderizar la pantalla
            self.__screen.blit(self.background(0,0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()

            x += 3
            if x >= 250:
                hayGanador = True
                pygame.quit()
                sys.exit() '''

if __name__ == '__main__':
    
    game = Game()
    pygame.init()
    
    game.competir()