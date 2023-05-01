import pygame

class TiroPersonagem(pygame.sprite.Sprite):
    def __init__(self, posicao_tiro, delta_t, imagem_tiro = pygame.image.load('Imagens/tiro_personagem.png')):
        pygame.sprite.Sprite.__init__(self)
        self.posicao = posicao_tiro
        self.delta_t = delta_t
        self.velocidade = 100
        self.image = imagem_tiro
        self.rect = self.image.get_rect()
        self.rect.x = self.posicao[0]
        self.rect.y = self.posicao[1]


    def update (self):
        self.rect.y -= self.velocidade * self.delta_t