import pygame

class Barreiras(pygame.sprite.Sprite):
    def init(self, pos_x, pos_y = 650):
        super().__init__()
        self.posx = pos_x
        self.posy = pos_y
        self.largura = 120
        self.altura = 10
        self.image = pygame.Surface([self.largura, self.altura])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()