import pygame

class TelaDerrota:
    def __init__(self, window):
        self.window = window

    def desenha_tela(self):
        self.window.fill((0,0,255))

    def atualiza_estado(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return -1
            if evento == pygame.KEYDOWN and evento.key == pygame.K_v:
                return 0
        return 4