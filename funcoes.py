import pygame

class Tela_do_jogo:
    def __init__(self):
        pygame.init()
        largura = 1520
        altura = 800
        self.window = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption('Jogo do Caião e do Benizão')

    def atualiza_estado(self):
        #Caso o jogador clique no "quit" o jogo fecha:
        jogo = True
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo = False

        return jogo
        
    def desenha(self):
        #Desenha as telas de fundo:
        self.window.fill((0, 0, 0))

        pygame.display.update()
    
    def loop_jogo(self):

        while self.atualiza_estado():
            self.desenha()


