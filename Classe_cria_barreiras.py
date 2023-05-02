import pygame

class Barreiras(pygame.sprite.Sprite):
    """
    Classe que representa as barreiras que protegem o jogador dos ataques inimigos.

    Atributos:
    - posx (int): posição x da barreira.
    - posy (int): posição y da barreira.
    - largura (int): largura da barreira.
    - altura (int): altura da barreira.
    - image (Surface): superfície que representa a imagem da barreira.
    - rect (Rect): retângulo que representa o posicionamento e o tamanho da barreira.

    Métodos:
    - __init__(self, pos_x, pos_y=650): inicializa a classe Barreiras.
    """

    def init(self, pos_x, pos_y = 650):
        """
        Inicializa a classe Barreiras.

        Cria a barreira na posição (pos_x, pos_y) com a largura e altura especificadas.
        Define a cor da barreira como branco e cria uma superfície para a imagem da barreira.
        Define o retângulo que representa o posicionamento e tamanho da barreira.

        Parâmetros:
        - pos_x (int): posição x da barreira.
        - pos_y (int): posição y da barreira. 
        """

        super().__init__()
        self.posx = pos_x
        self.posy = pos_y
        self.largura = 120
        self.altura = 10
        self.image = pygame.Surface([self.largura, self.altura])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()