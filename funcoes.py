import pygame

class Tela_do_jogo:
    def __init__(self, tela):
        self.tela = tela

def inicializa(self):
    pygame.init()
    self.tela = pygame.display.set_mode((1520, 800))
    pygame.display.set_caption('Jogo do Caião e do Benizão')

    return self.tela

def atualiza_estado():
    #Caso o jogador clique no "quit" o jogo fecha:
    jogo = True
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False

    return jogo
    
def desenha(self):
    #Desenha as telas de fundo:
    self.tela.fill((0, 0, 0))

    pygame.display.update()
  
def loop_jogo(self):

    while atualiza_estado():
        desenha(self)


