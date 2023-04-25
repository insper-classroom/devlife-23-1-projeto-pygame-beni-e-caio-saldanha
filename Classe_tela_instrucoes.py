import pygame


class TelaInstrucao:
    def __init__(self, window):
        self.window = window

    def desenha_tela(self):
        self.window.fill((0, 0, 0))
        # self.window.blit('Como Jogar:', (780,200))
        # self.window.blit('* O objetivo do jogo é destruir as naves inimigas.', (720,300))
        # self.window.blit('* O jogo é multiplayer', (720,350))
        # self.window.blit('* Existem 4 tipos de naves inimigas', (720,400))
        # self.window.blit('* Cada tipo de nave inimiga tem uma pontuação e alguma funcionalidade diferente', (720,450))
        # self.window.blit('* O jogaador 1 se move no A e no D e atira no W, já o jogador 2 se move no J e no L e atira no I', (720,500))
        # self.window.blit('* O jogador que mais fizer mais pontos é o grande campeão', (720,550))
        # self.window.blit('* Cada jogador tem 3 vidas', (720,600))
        # self.window.blit('Clique espaço para jogar', (780,650))

    def atualiza_estado(self):
        indice_tela = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                indice_tela = -1
                return indice_tela
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                indice_tela = 0
                return indice_tela
        return 2