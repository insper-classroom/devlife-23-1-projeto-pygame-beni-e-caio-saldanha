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
        self.nave = Nave(self.window, [380, 670], imagem_nave_redimensionada, 0)
        self.nave2 = Nave(self.window, [1140, 670], imagem_nave_redimensionada, 0)

    def atualiza_estado(self):
        #Caso o jogador clique no "quit" o jogo fecha:
        jogo = True
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo = False
            else:
                self.nave.movimenta_nave(evento)
        # self.nave2.movimenta_nave()

        return jogo
        
    def desenha(self):
        #Desenha as telas de fundo:
        self.window.fill((0, 0, 0))
        self.nave.desenha_nave()
        self.nave2.desenha_nave()

        pygame.display.update()
    
    def loop_jogo(self):
        self.atualiza_estado()
        while self.atualiza_estado():
            self.desenha()

class Nave:
    
    def __init__(self,window,pos,imagem_redimensionada,vel_nave):
        self.posicao_nave = pos
        self.vel_nave = vel_nave
        self.window = window
        imagem = pygame.image.load('nave do joguinho.png')
        imagem_redimensionada = pygame.transform.scale(imagem, (100,100))
        self.imagem_redimensionada = imagem_redimensionada

    def desenha_nave(self):
        self.window.blit(self.imagem_redimensionada, (self.posicao_nave[0], 670))

    def movimenta_nave(self, evento):
        
        # for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d:
                self.vel_nave += 10
            elif evento.key == pygame.K_a:
                self.vel_nave -= 10

        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_d:
                self.vel_nave -= 10
            elif evento.key == pygame.K_a:
                self.vel_nave += 10

        self.posicao_nave[0] += self.vel_nave



