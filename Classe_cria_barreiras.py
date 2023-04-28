import pygame

class Barreiras(pygame.sprite.Sprite):
    def init(self, pos_x, pos_y):
        super().__init__()
        self.posx = pos_x
        self.posy = pos_y
        self.largura = 120
        self.altura = 10
    
    def update(self):
        barreira = pygame.draw.rect(self.window, (255,255,255), (self.posx, self.posy, self.largura, self.altura))
        return barreira