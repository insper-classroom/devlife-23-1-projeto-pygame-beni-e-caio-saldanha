import pygame

class Inimigo(pygame.sprite.Sprite):
    """
    Classe que representa um inimigo no jogo.

    Argumentoss:
        posicao_inimigo (tuple): Tupla contendo as coordenadas (x,y) da posição inicial do inimigo.
        imagem_redimensionada (pygame.Surface): Superfície contendo a imagem redimensionada do inimigo.
        delta_t (float): Intervalo de tempo desde a última atualização.

    Atributos:
        image (Surface): Superfície contendo a imagem do inimigo.
        rect (Rect): Objeto rect que define a posição e as dimensões da imagem do inimigo.
        delta_t (float): Intervalo de tempo desde a última atualização.
        max_x (int): Coordenada x máxima que o inimigo pode atingir antes de mudar de direção.
        min_x (int): Coordenada x mínima que o inimigo pode atingir antes de mudar de direção.
        velocidade (int): Velocidade do inimigo.

    Métodos:
        update(): Atualiza a posição do inimigo.
    """

    def __init__(self, posicao_inimigo, imagem_redimensionada, delta_t):
        """
        Atualiza a posição do inimigo de acordo com a velocidade e o intervalo de tempo delta_t.

        Se a posição do inimigo atingir a coordenada máxima ou mínima definida, inverte a direção da velocidade
        e movimenta o inimigo para baixo.
        """
        
        super().__init__()
        self.image = imagem_redimensionada
        self.rect = self.image.get_rect()
        self.rect.x = posicao_inimigo[0]
        self.rect.y = posicao_inimigo[1]
        self.delta_t = delta_t
        self.max_x = posicao_inimigo[0] + 260
        self.min_x = posicao_inimigo[0] - 260
        self.velocidade = 30

    def update(self):
        if self.rect.x < self.min_x: 
            self.velocidade = abs(self.velocidade)
            self.rect.y += self.image.get_height()
            self.rect.x = self.min_x
        if self.rect.x > self.max_x:
            self.velocidade = -abs(self.velocidade)
            self.rect.y += self.image.get_height()
            self.rect.x = self.max_x
        self.rect.x += self.delta_t * self.velocidade