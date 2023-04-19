import pygame

def inicializa():
    tela = pygame.display.set_mode((1520, 800))
    pygame.display.set_caption('Jogo do Caião e do Benizão')

    return tela

def atualiza_estado():
    #Caso o jogador clique no "quit" o jogo fecha:
    jogo = True
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False

    return jogo
    

def desenha(tela):
    #Desenha as telas de fundo:
    tela.fill((0, 0, 0))

    pygame.display.update()
  

def loop_jogo(tela):

    while atualiza_estado():
        desenha(tela)


