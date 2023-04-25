import pygame

class Inimigo(pygame.sprite.Sprite):

    def __init__(self, posicao_inimigo, imagem_redimensionada, delta_t):
        super().__init__()
        self.image = imagem_redimensionada
        self.rect = self.image.get_rect()
        self.rect.x = posicao_inimigo[0]
        self.rect.y = posicao_inimigo[1]
        self.delta_t = delta_t

    def update(self):
        velocidade = 10
        if self.rect.x < 1520:
            self.rect.x += self.delta_t * velocidade
        elif self.rect.x > 1520:
            self.rect.x -= self.delta_t * velocidade
        elif self.rect.x < 0:
            self.rect.x += self.delta_t * velocidade