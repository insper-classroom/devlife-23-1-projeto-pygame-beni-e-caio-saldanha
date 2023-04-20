import pygame
from Classe_da_nave import Nave
class Jogo:
    def __init__(self):
        pygame.init()
        largura = 1520
        altura = 760
        self.ultimo_updated = -1
        self.delta_t = self.calcula_deltaT()
        self.window = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption('Jogo do Caião e do Benizão')
        imagem_nave = pygame.image.load('nave do joguinho.png')
        imagem_nave_redimensionada = pygame.transform.scale(imagem_nave, (100,100))
        self.nave = Nave(self.window, [380, 670], imagem_nave_redimensionada, 0, self.delta_t)
        self.nave2 = Nave(self.window, [1140, 670], imagem_nave_redimensionada, 0, self.delta_t)


    def calcula_deltaT(self):
        tempo_atual = pygame.time.get_ticks()
        delta_t = (tempo_atual - self.ultimo_updated) / 1000
        self.ultimo_updated = tempo_atual
        return delta_t

    def atualiza_estado(self):
        
        jogo = True
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo = False
            self.nave.movimenta_nave(evento)
            self.nave2.movimenta_nave2(evento)

        return jogo
        
    def desenha(self):

        self.window.fill((0, 0, 0))
        self.nave.desenha_nave()
        self.nave2.desenha_nave()

        pygame.display.update()
    
    def loop_jogo(self):
        self.atualiza_estado()
        while self.atualiza_estado():
            self.desenha()




