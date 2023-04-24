import pygame
from Classe_da_nave import Nave
from Classe_do_inimigo import Inimigo

class Jogo:
    def __init__(self):
        pygame.init()

        # TELA E WINDOW
        self.largura = 1520
        self.altura = 760
        self.window = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Jogo do Caião e do Benizão')

        # IMAGENS
        imagem_nave = pygame.image.load('nave do joguinho.png')
        imagem_nave_redimensionada = pygame.transform.scale(imagem_nave, (100,100))
        imagem_fundo = pygame.image.load('Imagens\Space Background.png')
        self.imagem_fundo_redimensionada = pygame.transform.scale_by(imagem_fundo, (1, 0.93))
        imagem_inimigo = pygame.image.load('Imagens\Klaed - Fighter - Base.png')
        imagem_inimigo_redimensionada = pygame.transform.scale(imagem_inimigo, (60,60))
        altura_imagem_fundo = self.imagem_fundo_redimensionada.get_height()
        largura_inimigo = imagem_inimigo_redimensionada.get_width()

        # 
        self.ultimo_updated = -1
        self.delta_t = self.calcula_deltaT()
        
        # 
        self.nave = Nave(self.window, [380, 610], imagem_nave_redimensionada, 0, self.delta_t,1)
        self.nave2 = Nave(self.window, [1140, 610], imagem_nave_redimensionada, 0, self.delta_t,2)

        # self.inimigo_p1 = pygame.sprite.Group()
        # x = 0
        # y = 0
        largura_inimigo = imagem_inimigo_redimensionada.get_width()
        altura_inimigo = imagem_inimigo_redimensionada.get_height()
        # contagem_inimigo_linha = 0
        # for i in range (18):
        #     contagem_inimigo_linha += 1
        #     self.inimigo = Inimigo([x,y], imagem_inimigo_redimensionada)
        #     self.inimigo_p1.add(self.inimigo)
        #     if contagem_inimigo_linha > 6:
        #         x = 0
        #         y += altura_inimigo
        #         contagem_inimigo_linha = 0
        #     else:
        #         x += largura_inimigo
        # x = 0

        self.inimigo_p2 = pygame.sprite.Group()
        x = 0
        y = 0

        for i_y in range (3):
            for i in range (20):
                self.inimigo = Inimigo([x,y], imagem_inimigo_redimensionada)
                self.inimigo_p2.add(self.inimigo)
                x += largura_inimigo
            y += altura_inimigo
            x = 0
        self.todos_inimigos = pygame.sprite.Group()
        self.todos_inimigos.add( self.inimigo_p2)


    def calcula_deltaT(self):
        tempo_atual = pygame.time.get_ticks()
        delta_t = (tempo_atual - self.ultimo_updated) / 1000
        self.ultimo_updated = tempo_atual
        return delta_t

    def atualiza_estado(self):
        
        jogo = True
        for evento in pygame.event.get():
            if evento.type != pygame.MOUSEMOTION:
                if evento.type == pygame.QUIT:
                    jogo = False
                elif evento.type == pygame.KEYDOWN or pygame.KEYUP:
                    self.nave.movimenta_nave(evento)
                    self.nave2.movimenta_nave(evento)

        return jogo
        
    def desenha(self):

        self.window.fill((255, 255, 255))
        self.window.blit(self.imagem_fundo_redimensionada, (0,0))
        self.nave.desenha_nave()
        self.nave2.desenha_nave()
        self.todos_inimigos.draw(self.window)
        

        pygame.display.update()
    
    def loop_jogo(self):
        while self.atualiza_estado():
            self.desenha()




