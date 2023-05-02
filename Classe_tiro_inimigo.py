import pygame

class TiroInimigo(pygame.sprite.Sprite):
    """
    Classe para representar um tiro disparado por um inimigo no jogo.
    """

    def __init__(self, posicao_tiro, delta_t, imagem_tiro = pygame.image.load('Imagens/tiro_personagem.png')):
        """
        Construtor da classe.

        Argumentos:
        - posicao_tiro: uma tupla (x,y) que representa a posição inicial do tiro.
        - delta_t: um float que representa a variação de tempo desde a última atualização do tiro.
        - imagem_tiro: um objeto de imagem do pygame que representa o sprite do tiro.
        """

        pygame.sprite.Sprite.__init__(self)
        self.posicao = posicao_tiro
        self.delta_t = delta_t
        self.velocidade = 120
        self.image = imagem_tiro
        self.rect = self.image.get_rect()
        self.rect.x = self.posicao[0]
        self.rect.y = self.posicao[1]


    def update (self):
        """
        Método que atualiza a posição do tiro de acordo com a variação de tempo e sua velocidade.
        """
        self.rect.y += self.velocidade * self.delta_t