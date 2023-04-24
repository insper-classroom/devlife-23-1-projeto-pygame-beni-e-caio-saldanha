import pygame

class Inimigo(pygame.sprite.Sprite):

    def __init__(self, posicao_inimigo, imagem_redimensionada):
        super().__init__()
        self.image = imagem_redimensionada
        self.rect = self.image.get_rect()
        self.rect.x = posicao_inimigo[0]
        self.rect.y = posicao_inimigo[1]