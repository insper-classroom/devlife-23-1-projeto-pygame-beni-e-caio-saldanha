import pygame

class TelaDerrota:
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
        self.window.blit(fonte_titulo_desenha, ((self.width_window//2)-(self.widht_texto_titulo//2),180))   

        fonte_win = pygame.font.Font('Imagens\Sigmar-Regular.ttf', 50)
        fonte_win_desenha = fonte_win.render('AH não, os aliens invadiram a terra!', fonte_win, cor)
        self.widht_texto_win = fonte_win_desenha.get_width()
        self.window.blit(fonte_win_desenha, ((self.width_window//2)-(self.widht_texto_win//2),480))

        fonte_game_over = fonte_win.render('GAME OVER!', fonte_win, cor)
        self.widht_texto_game_over = fonte_game_over.get_width()
        self.window.blit(fonte_game_over, ((self.width_window//2)-(self.widht_texto_game_over//2),330))

    def atualiza_estado(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return -1
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_v:
                return 0
        return 4