import pygame
from Classe_tela_jogo import *
from Classe_tela_inicio import *
from Classe_tela_instrucoes import *
from Classe_tela_vitoria import *

class ControlaTelas:
    def __init__(self):
        self.largura = 1520
        self.altura = 760
        self.window = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Galactic Warfare')

        self.TelaJogo = TelaJogo(self.window)
        self.TelaInicio = TelaInicio(self.window)
        self.TelaInstrucoes = TelaInstrucao(self.window)
        self.TelaVitoria = TelaVitoria(self.window)

        self.lista_telas = [self.TelaInicio, self.TelaJogo, self.TelaInstrucoes, self.TelaVitoria]
        indice_tela = 0
        self.tela = self.lista_telas[indice_tela]
    
    def atualiza_telas(self):
        indice_tela = self.tela.atualiza_estado()
        print(indice_tela)
        if indice_tela == -1:
            return False
        else:
            self.tela = self.lista_telas[indice_tela]
            return True

    def desenha(self):
        self.tela.desenha_tela()
        pygame.display.update()

    def game_loop(self):
        while self.atualiza_telas():
            self.desenha()