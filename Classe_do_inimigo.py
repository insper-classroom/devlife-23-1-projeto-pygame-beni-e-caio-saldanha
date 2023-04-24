import pygame

class Inimigo:

    def __init__(self, window, pos, n_inimigos, imagem_redimensionada, largura_inimigo):
        self.window = window
        self.pos = pos
        self.n_inimigos = n_inimigos
        self.imagem = imagem_redimensionada
        self.largura_inimigo = largura_inimigo

    def desenha_inimigo (self):
        inimigo = self.imagem
        for i in range (4):
            self.window.blit(inimigo, self.pos)
            self.pos[0] += self.largura_inimigo
            i += 1
            