import pygame

class TiroPersonagem(pygame.sprite.Sprite):
    def __init__(self, posicao_tiro, imagem_tiro, delta_t):
        self.posicao = posicao_tiro
        self.delta_t = delta_t
        self.velocidade = 40
        rect_tiro = imagem_tiro.get_rect()

    def update (self):
        self.posicao.x += self.velocidade * self.delta_t