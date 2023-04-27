import pygame


class TelaInstrucao:
    def __init__(self, window):
        self.window = window
        self.width_window= window.get_width()
        imagem_fundo = pygame.image.load('Imagens\SpaceBackground.png')
        self.imagem_fundo_redimensionada = pygame.transform.scale(imagem_fundo, (1520, 760))

    def desenha_tela(self):
        pygame.init()
        cor = (255,255,255)
        self.window.fill((255, 255, 255))
        self.window.blit(self.imagem_fundo_redimensionada, (0,0))   

        fonte_titulo = pygame.font.Font('Imagens\Sigmar-Regular.ttf', 80)
        fonte_titulo_desenha = fonte_titulo.render('GALACTIC WARFARE', fonte_titulo, cor)
        self.widht_texto_titulo = fonte_titulo_desenha.get_width()
        self.window.blit(fonte_titulo_desenha, ((self.width_window//2)-(self.widht_texto_titulo//2),80))

        fonte_texto = pygame.font.Font('Imagens\Rubik-Italic-VariableFont_wght.ttf', 30)
        fonte_como_jogar = pygame.font.Font('Imagens\Sigmar-Regular.ttf', 50)
        fonte_voltar = pygame.font.Font('Imagens\Sigmar-Regular.ttf', 20)


        fonte_i0 = fonte_como_jogar.render('COMO JOGAR:', fonte_texto, cor)
        self.widht_texto_i0 = fonte_i0.get_width()
        self.window.blit(fonte_i0, ((self.width_window//2)-(self.widht_texto_i0//2),230))

        fonte_i1 = fonte_texto.render('O jogo é multiplayer local no estilo PVP', fonte_texto, cor)
        self.widht_texto_i1 = fonte_i1.get_width()
        self.window.blit(fonte_i1, ((self.width_window//2)-(self.widht_texto_i1//2),350))

        fonte_i2 = fonte_texto.render('O player 1 se movimenta no (A) e no (D) e atira no (W)', fonte_texto, cor)
        self.widht_texto_i2 = fonte_i2.get_width()
        self.window.blit(fonte_i2, ((self.width_window//2)-(self.widht_texto_i2//2),400))

        fonte_i3 = fonte_texto.render('O player 2 se movimenta no (J) e no (L) e atira no (I)', fonte_texto, cor)
        self.widht_texto_i3 = fonte_i3.get_width()
        self.window.blit(fonte_i3, ((self.width_window//2)-(self.widht_texto_i3//2),450))

        fonte_i4 = fonte_texto.render('Existem 3 tipos de naves inimigas', fonte_texto, cor)
        self.widht_texto_i4 = fonte_i4.get_width()
        self.window.blit(fonte_i4, ((self.width_window//2)-(self.widht_texto_i4//2),500))

        fonte_i5 = fonte_texto.render('O objetivo do jogo é eliminar todas as naves inimigas e salvar a mundo', fonte_texto, cor)
        self.widht_texto_i5 = fonte_i5.get_width()
        self.window.blit(fonte_i5, ((self.width_window//2)-(self.widht_texto_i5//2),550))

        fonte_i6 = fonte_texto.render('Cada tipo de nave inimiga vale uma quantidade de pontos, ganha quem fizer mais pontos', fonte_texto, cor)
        self.widht_texto_i6 = fonte_i6.get_width()
        self.window.blit(fonte_i6, ((self.width_window//2)-(self.widht_texto_i6//2),600))

        fonte_i7 = fonte_voltar.render('Clique (V) para voltar', fonte_texto, cor)
        self.widht_texto_i7 = fonte_i7.get_width()
        self.window.blit(fonte_i7, ((self.width_window//2)-(self.widht_texto_i7//2),680))
 

    def atualiza_estado(self):
        2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                return 0
        return 2