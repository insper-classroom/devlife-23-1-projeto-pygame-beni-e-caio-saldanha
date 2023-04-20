import pygame

class Jogo:
    def __init__(self):
        pygame.init()
        largura = 1520
        altura = 760
        self.window = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption('Jogo do Caião e do Benizão')
        imagem_nave = pygame.image.load('nave do joguinho.png')
        imagem_nave_redimensionada = pygame.transform.scale(imagem_nave, (100,100))
        self.nave = Nave(self.window, 380, 670, imagem_nave_redimensionada, 500, 500)
        self.nave2 = Nave(self.window, 1140, 670, imagem_nave_redimensionada, 500, 500)

    def atualiza_estado(self):
        #Caso o jogador clique no "quit" o jogo fecha:
        jogo = True
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo = False
        self.nave.movimenta_nave()
        self.nave2.movimenta_nave()

        return jogo
        
    def desenha(self):
        #Desenha as telas de fundo:
        self.window.fill((0, 0, 0))
        self.nave.desenha_nave()
        self.nave2.desenha_nave()

        pygame.display.update()
    
    def loop_jogo(self):

        while self.atualiza_estado():
            self.desenha()

class Nave:
    
    def __init__(self,window,posx,posy,imagem_redimensionada,vel_navex, vel_navey):
        self.posicao_nave_x = posx
        self.posicao_nave_y = posy
        self.vel_navex = vel_navex
        self.vel_navey = vel_navey
        self.window = window
        imagem = pygame.image.load('nave do joguinho.png')
        imagem_redimensionada = pygame.transform.scale(imagem, (100,100))
        self.imagem_redimensionada = imagem_redimensionada

    def desenha_nave(self):
        self.window.blit(self.imagem_redimensionada, (self.posicao_nave_x, self.posicao_nave_y))

    def movimenta_nave(self):
        
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_d:
                    self.vel_navex += 500
                elif evento.key == pygame.K_a:
                    self.vel_navex -= 500
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_d:
                    self.vel_navex -= 500
                elif evento.key == pygame.K_a:
                    self.vel_navex += 500



