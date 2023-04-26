import pygame

class TelaInicio:
    def __init__(self, window):
        self.window = window
        self.width_window= window.get_width()
        imagem_fundo = pygame.image.load('Imagens\Space Background.png')
        self.imagem_fundo_redimensionada = pygame.transform.scale(imagem_fundo, (1520, 760))

    def desenha_tela(self):
        pygame.init()
        fonte = pygame.font.Font('Imagens\Rubik-Italic-VariableFont_wght.ttf', 50)
        cor = (255,255,255)
        self.window.fill((255, 255, 255))
        self.window.blit(self.imagem_fundo_redimensionada, (0,0))
        # self.window.draw(''' 
        # _______  _______  _        _______  _______ __________________ _______             _______  _______  _______  _______  _______  _______ 
        # (  ____ \(  ___  )( \      (  ___  )(  ____ |\__   __/\__   __/(  ____ \  |\     /|(  ___  )(  ____ )(  ____ \(  ___  )(  ____ )(  ____|
        # | (    \/| (   ) || (      | (   ) || (    \/   ) (      ) (   | (    \/  | )   ( || (   ) || (    )|| (    \/| (   ) || (    )|| (    
        # | |      | (___) || |      | (___) || |         | |      | |   | |        | | _ | || (___) || (____)|| (__    | (___) || (____)|| (__    
        # | | ____ |  ___  || |      |  ___  || |         | |      | |   | |        | |( )| ||  ___  ||     __)|  __)   |  ___  ||     __)|  __)   
        # | | \_  )| (   ) || |      | (   ) || |         | |      | |   | |        | || || || (   ) || (\ (   | (      | (   ) || (\ (   | (      
        # | (___) || )   ( || (____/\| )   ( || (____/\   | |   ___) (___| (____/\  | () () || )   ( || ) \ \__| )      | )   ( || ) \ \__| (____/|
        # (_______)|/     \|(_______/|/     \|(_______/   )_(   \_______/(_______/  (_______)|/     \||/   \__/|/       |/     \||/   \__/(_______/
        # ''', (780,300))
            
        fonte_espaco = fonte.render('Clique espaço para jogar', fonte, cor)
        self.widht_texto_inicio = fonte_espaco.get_width()
        self.window.blit(fonte_espaco, ((self.width_window//2)-(self.widht_texto_inicio//2),650))
        # self.window.blit('Clique I para ler as instruções', (780,600))

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















































                                                                                                                                         