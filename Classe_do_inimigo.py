import pygame

class Inimigo(pygame.sprite.Sprite):

    def __init__(self, posicao_inimigo, imagem_redimensionada, delta_t):
        super().__init__()
        self.image = imagem_redimensionada
        self.rect = self.image.get_rect()
        self.rect.x = posicao_inimigo[0]
        self.rect.y = posicao_inimigo[1]
        self.delta_t = delta_t
        self.max_x = posicao_inimigo[0] + 260
        self.min_x = posicao_inimigo[0] - 260
        self.velocidade = 10


    def update(self):

        if self.rect.x < self.min_x or self.rect.x > self.max_x:
            self.velocidade *= -1
            self.rect.y += self.image.get_height()
        self.rect.x += self.delta_t * self.velocidade