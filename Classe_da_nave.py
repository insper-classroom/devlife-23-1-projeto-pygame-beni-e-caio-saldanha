import pygame


class Nave(pygame.sprite.Sprite):
    """
    Classe que representa a nave do jogador.

    Atributos:
    pos (tuple): Posição inicial da nave na tela (x,y).
    imagem_redimensionada (pygame.Surface): Imagem da nave com as dimensões já redimensionadas.
    delta_t (float): Diferença de tempo entre cada iteração do loop de jogo.
    n_nave (int): Identificador da nave (1 ou 2).

    Métodos:
    movimenta_nave(evento): Move a nave de acordo com as teclas pressionadas pelo jogador.
    
    """
    
    def __init__(self,pos,imagem_redimensionada,delta_t,n_nave):
        """
        Construtor da classe Nave.
        
        """

        pygame.sprite.Sprite.__init__(self)
        self.vel_nave1 = 0
        self.vel_nave2 = 0
        self.delta_t = delta_t
        self.n_nave = n_nave
        self.image = imagem_redimensionada
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def movimenta_nave(self, evento):
        """
        Move a nave de acordo com as teclas pressionadas pelo jogador.
        
        Parametros:
        evento : pygame.event.Event
            Evento escolhido pelo teclado do jogador.
        """

        v = 30
        
        if self.n_nave == 1:

            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > 1440:
                self.rect.x = 1440

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_d:
                    self.vel_nave1 += v
                elif evento.key == pygame.K_a:
                    self.vel_nave1-= v
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_d:
                    self.vel_nave1 -= v
                elif evento.key == pygame.K_a:
                    self.vel_nave1 += v

            self.rect.x += self.vel_nave1 * self.delta_t
            
        
        else: 

            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > 1440:
                self.rect.x = 1440

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_l:
                    self.vel_nave2 += v
                elif evento.key == pygame.K_j:
                    self.vel_nave2 -= v
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_l:
                    self.vel_nave2 -= v
                elif evento.key == pygame.K_j:
                    self.vel_nave2 += v


            self.rect.x += self.vel_nave2 * self.delta_t
    