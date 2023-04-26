import pygame

class TelaInicio:
    def __init__(self, window):
        self.window = window
        self.width_window= window.get_width()
        imagem_fundo = pygame.image.load('Imagens\Space Background.png')
        self.imagem_fundo_redimensionada = pygame.transform.scale(imagem_fundo, (1520, 760))

    def desenha_tela(self):
        pygame.init()
        cor = (255,255,255)
        self.window.fill((255, 255, 255))
        self.window.blit(self.imagem_fundo_redimensionada, (0,0))    

        fonte_titulo = pygame.font.Font('Imagens\Sigmar-Regular.ttf', 120)
        fonte_titulo_desenha = fonte_titulo.render('GALACTIC WARFARE', fonte_titulo, cor)
        self.widht_texto_titulo = fonte_titulo_desenha.get_width()
        self.window.blit(fonte_titulo_desenha, ((self.width_window//2)-(self.widht_texto_titulo//2),150))

        fonte_texto = pygame.font.Font('Imagens\Rubik-Italic-VariableFont_wght.ttf', 50)
        fonte_espaco_desenha = fonte_texto.render('Clique espaço para jogar', fonte_texto, cor)
        self.widht_texto_espaco = fonte_espaco_desenha.get_width()
        self.window.blit(fonte_espaco_desenha, ((self.width_window//2)-(self.widht_texto_espaco//2),650))

        fonte_instrucoes_desenha = fonte_texto.render('Clique i para ler as instruções', fonte_texto, cor)
        self.widht_texto_instrucoes = fonte_instrucoes_desenha.get_width()
        self.window.blit(fonte_instrucoes_desenha, ((self.width_window//2)-(self.widht_texto_instrucoes//2),450))

        fonte_OU_desenha = fonte_texto.render('OU', fonte_texto, cor)
        self.widht_texto_OU = fonte_OU_desenha.get_width()
        self.window.blit(fonte_OU_desenha, ((self.width_window//2)-(self.widht_texto_OU//2),550))

        

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                print(12)
                return 2
        return 0















































                                                                                                                                         