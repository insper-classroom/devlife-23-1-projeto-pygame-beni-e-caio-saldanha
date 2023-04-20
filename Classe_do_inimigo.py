import pygame

class Inimigo:

    def __init__(self, window, pos, n_inimigos, imagem_redimensionada):
        self.window = window
        self.pos = pos
        self.n_inimigos = n_inimigos
        self.imagem = imagem_redimensionada

    def desenha_inimigo (self):
        vida = self.imagem
        self.window.blit(vida, self.pos)