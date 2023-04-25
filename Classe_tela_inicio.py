import pygame

class TelaInicio:
    def __init__(self, window):
        self.window = window

    def desenha_tela(self):
        self.window.fill((255, 255, 255))
        # self.window.blit(''' 
        # _______  _______  _        _______  _______ __________________ _______             _______  _______  _______  _______  _______  _______ 
        # (  ____ \(  ___  )( \      (  ___  )(  ____ |\__   __/\__   __/(  ____ \  |\     /|(  ___  )(  ____ )(  ____ \(  ___  )(  ____ )(  ____|
        # | (    \/| (   ) || (      | (   ) || (    \/   ) (      ) (   | (    \/  | )   ( || (   ) || (    )|| (    \/| (   ) || (    )|| (    
        # | |      | (___) || |      | (___) || |         | |      | |   | |        | | _ | || (___) || (____)|| (__    | (___) || (____)|| (__    
        # | | ____ |  ___  || |      |  ___  || |         | |      | |   | |        | |( )| ||  ___  ||     __)|  __)   |  ___  ||     __)|  __)   
        # | | \_  )| (   ) || |      | (   ) || |         | |      | |   | |        | || || || (   ) || (\ (   | (      | (   ) || (\ (   | (      
        # | (___) || )   ( || (____/\| )   ( || (____/\   | |   ___) (___| (____/\  | () () || )   ( || ) \ \__| )      | )   ( || ) \ \__| (____/|
        # (_______)|/     \|(_______/|/     \|(_______/   )_(   \_______/(_______/  (_______)|/     \||/   \__/|/       |/     \||/   \__/(_______/
        # ''', (780,300))
            
        # self.window.blit('Clique espaço para jogar', (780,500))
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















































                                                                                                                                         