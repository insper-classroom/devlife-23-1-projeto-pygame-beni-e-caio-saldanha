import pygame

class TelaVitoriaP1:
    """
    Classe responsável por exibir a tela de vitória do jogo.
    """

    def __init__(self, window):
        """
        Inicializa a classe TelaVitoria.

        Argumentos:
            window (pygame.Surface): janela do pygame.

        Atributos:
            window (pygame.Surface): janela do pygame.
            width_window (int): largura da janela do pygame.
            imagem_fundo_redimensionada (pygame.Surface): imagem de fundo da tela de vitória redimensionada.
        """

        self.window = window
        self.width_window= window.get_width()
        imagem_fundo = pygame.image.load('Imagens\SpaceBackground.png')
        self.imagem_fundo_redimensionada = pygame.transform.scale(imagem_fundo, (1520, 760))

    def desenha_tela(self):
        """
        Desenha a tela de vitória.
        """

        pygame.init()
        cor_p = (115,215,255)
        cor = (255,255,255)
        self.window.fill((255, 255, 255))
        self.window.blit(self.imagem_fundo_redimensionada, (0,0))

        fonte_titulo = pygame.font.Font('Imagens\Sigmar-Regular.ttf', 80)
        fonte_titulo_desenha = fonte_titulo.render('GALACTIC WARFARE', fonte_titulo, cor)
        self.widht_texto_titulo = fonte_titulo_desenha.get_width()
        self.window.blit(fonte_titulo_desenha, ((self.width_window//2)-(self.widht_texto_titulo//2),180))   

        fonte_win = pygame.font.Font('Imagens\Sigmar-Regular.ttf', 50)
        fonte_win_desenha = fonte_win.render('Parabéns, o Player 1 venceu!', fonte_win, cor_p)
        self.widht_texto_win = fonte_win_desenha.get_width()
        self.window.blit(fonte_win_desenha, ((self.width_window//2)-(self.widht_texto_win//2),480))

        fonte_winners = fonte_win.render('WINNER!', fonte_win, cor)
        self.widht_texto_winner_desenha = fonte_winners.get_width()
        self.window.blit(fonte_winners, ((self.width_window//2)-(self.widht_texto_winner_desenha//2),330))

    def atualiza_estado(self):
        """
        Atualiza o estado da tela de acordo com os comandos do usuário.
        """
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return -1
        return 3