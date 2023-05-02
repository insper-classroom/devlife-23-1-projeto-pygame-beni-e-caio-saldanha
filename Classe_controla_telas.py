import pygame
from Classe_tela_jogo import *
from Classe_tela_inicio import *
from Classe_tela_instrucoes import *
from Classe_tela_vitoria_P1 import *
from Classe_tela_vitoria_P2 import *
from Classe_tela_derrota import *

class ControlaTelas:
    """
    Classe responsável por controlar as telas do jogo.

    Atributos:
    - largura (int): a largura da tela do jogo.
    - altura (int): a altura da tela do jogo.
    - window (Surface): a janela pygame em que o jogo é mostrado.
    - TelaJogo (TelaJogo): a tela de jogo do jogo.
    - TelaInicio (TelaInicio): a tela inicial do jogo.
    - TelaInstrucoes (TelaInstrucao): a tela de instruções do jogo.
    - TelaVitoria (TelaVitoria): a tela de vitória do jogo.
    - TelaDerrota (TelaDerrota): a tela de derrota do jogo.
    - lista_telas (list): lista com as indices de todas as telas do jogo.
    - tela (Tela): a tela atual do jogo.

    Métodos:
    - __init__(): inicializa a classe ControlaTelas.
    - atualiza_telas(): atualiza o estado das telas e retorna True se a tela deve ser atualizada e False caso contrário.
    - desenha(): desenha a tela atual.
    - game_loop(): loop principal do jogo que atualiza e desenha as telas.

    """

    def __init__(self):
        """
        Inicializa a classe ControlaTelas.

        Cria a janela pygame com a largura e altura especificadas. Define o título da janela como 'Galactic Warfare'.
        Cria as instâncias das telas de jogo, inicial, instruções, vitória e derrota.
        """

        self.largura = 1520
        self.altura = 760
        self.window = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Galactic Warfare')

        self.TelaJogo = TelaJogo(self.window)
        self.TelaInicio = TelaInicio(self.window)
        self.TelaInstrucoes = TelaInstrucao(self.window)
        self.TelaVitoriaP1 = TelaVitoriaP1(self.window)
        self.TelaVitoriaP2 = TelaVitoriaP2(self.window)
        self.TelaDerrota = TelaDerrota(self.window)

        self.lista_telas = [self.TelaInicio, self.TelaJogo, self.TelaInstrucoes, self.TelaVitoriaP1, self.TelaVitoriaP2, self.TelaDerrota]
        indice_tela = 0
        self.tela = self.lista_telas[indice_tela]
    
    def atualiza_telas(self):
        """
        Atualiza o estado das telas e retorna True se a tela deve ser atualizada e False caso contrário.

        Verifica se a tela atual deve ser atualizada chamando o método atualiza_estado() da instância de tela atual.
        Se o índice retornado for -1, retorna False para indicar que o jogo deve ser encerrado.
        Caso contrário, atualiza a tela atual para a próxima tela da lista de telas e retorna True.

        Retorna:
        - bool: True se a tela deve ser atualizada e False caso contrário.
        """

        indice_tela = self.tela.atualiza_estado()
        if indice_tela == -1:
            return False
        else:
            self.tela = self.lista_telas[indice_tela]
            return True

    def desenha(self):
        """
        Desenha a tela atual
        """

        self.tela.desenha_tela()
        pygame.display.update()

    def game_loop(self):
        while self.atualiza_telas():
            self.desenha()