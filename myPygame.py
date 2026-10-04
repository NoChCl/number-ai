from math import sqrt
import pygame, sys

class myPygame:
    def __init__(self, sampleX, scale):
        self.xSize=int(sqrt(len(sampleX)))
        self.ySize=int(sqrt(len(sampleX)))
        self.scale=scale
        self.pygame = pygame
        self.pygame.init()
        self.screen = self.pygame.display.set_mode((self.xSize*self.scale, self.ySize*self.scale))
        self.pygame.display.set_caption('number ai')
        self.FPSCLOCK = self.pygame.time.Clock()



    def update(self, grid):
        self.screen
        self.screen.fill((255, 255, 255))
        index=0
        for y in range(self.ySize):
            for x in range(self.xSize):
                pixel=pygame.Surface((self.scale, self.scale))
                color=(grid[index], grid[index], grid[index])
                pixel.fill(color)
                self.screen.blit(pixel, (x*self.scale, y*self.scale))
                index+=1
        pygame.display.update()
    def buttonPressed(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.pygame.quit()
                sys.exit()
            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_SPACE:
                    return True

        return False