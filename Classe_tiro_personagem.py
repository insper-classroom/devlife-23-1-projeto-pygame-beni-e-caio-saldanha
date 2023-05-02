import pygame

class TiroPersonagem(pygame.sprite.Sprite):
    """
    Classe que representa um tiro disparado pelo personagem controlado pelo jogador.

    Atributos:
    - posicao_tiro (tuple): posição inicial do tiro na tela, representada por uma tupla de duas coordenadas (x, y)
    - delta_t (float): tempo decorrido desde o último frame do jogo
    - imagem_tiro (pygame.Surface): imagem que representa o tiro na tela (padrão é 'Imagens/tiro_personagem.png')
    - velocidade (int): velocidade do tiro na tela

    Métodos:
    - __init__(self, posicao_tiro, delta_t, imagem_tiro = pygame.image.load('Imagens/tiro_personagem.png')): inicializa um novo tiro com a posição, tempo e imagem passados como argumentos.
    - update(self): atualiza a posição do tiro na tela de acordo com sua velocidade e o tempo decorrido desde o último frame.
    """

    def __init__(self, posicao_tiro, delta_t, quem_atirou, imagem_tiro = pygame.image.load('Imagens/tiro_personagem.png')):
        """
        Inicializa um novo tiro com a posição, tempo e imagem passados como argumentos.

        Argumentos:
        - posicao_tiro (tuple): posição inicial do tiro na tela, representada por uma tupla de duas coordenadas (x, y)
        - delta_t (float): tempo decorrido desde o último frame do jogo
        - imagem_tiro (pygame.Surface): imagem que representa o tiro na tela (padrão é 'Imagens/tiro_personagem.png')
        """

        pygame.sprite.Sprite.__init__(self)
        self.posicao = posicao_tiro
        self.delta_t = delta_t
        self.velocidade = 100
        self.image = imagem_tiro
        self.rect = self.image.get_rect()
        self.rect.x = self.posicao[0]
        self.rect.y = self.posicao[1]
        self.quem_atirou = quem_atirou


    def update (self):
        """
        Atualiza a posição do tiro na tela de acordo com sua velocidade e o tempo decorrido desde o último frame.
        """
        self.rect.y -= self.velocidade * self.delta_t