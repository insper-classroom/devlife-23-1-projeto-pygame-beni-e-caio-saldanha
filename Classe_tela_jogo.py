import pygame
from Classe_da_nave import Nave
from Classe_do_inimigo import Inimigo

class TelaJogo:
    def __init__(self, window):
        clock = pygame.time.Clock()

        # TELA E WINDOW
        self.largura = 1520
        self.altura = 760
        self.window = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Galactic Warfare')

        imagem_nave_p1 = pygame.image.load('Imagens\Imagem_p1.png')
        imagem_nave_redimensionada1 = pygame.transform.scale(imagem_nave_p1, (95,95))
        imagem_nave_p2 = pygame.image.load('Imagens\Imagem_p2.png')
        imagem_nave_redimensionada2 = pygame.transform.scale(imagem_nave_p2, (95,95))
        self.imagem_fundo = pygame.image.load('Imagens\Space Background.png')
        imagem_inimigo = pygame.image.load('Imagens\Imagem_inimigo1.png')
        imagem_inimigo_redimensionada = pygame.transform.scale(imagem_inimigo, (50,50))
        largura_inimigo = imagem_inimigo_redimensionada.get_width()

        self.ultimo_updated = -1
        self.delta_t = self.calcula_deltaT()
        # 
        self.nave = Nave(self.window, [380, 670], imagem_nave_redimensionada1, 0, self.delta_t,1)
        self.nave2 = Nave(self.window, [1140, 670], imagem_nave_redimensionada2, 0, self.delta_t,2)

        largura_inimigo = imagem_inimigo_redimensionada.get_width()
        altura_inimigo = imagem_inimigo_redimensionada.get_height()

        self.sprites_inimigo = pygame.sprite.Group()
        x = 260
        y = 65

        for _ in range (3):
            for _ in range (20):
                self.inimigo = Inimigo([x,y], imagem_inimigo_redimensionada, self.delta_t)
                self.sprites_inimigo.add(self.inimigo)
                x += largura_inimigo
            y += altura_inimigo
            x = 260

        self.sprites_tiro = pygame.sprite.Group()


    def calcula_deltaT(self):
        tempo_atual = pygame.time.get_ticks()
        delta_t = (tempo_atual - self.ultimo_updated) / 1000
        self.ultimo_updated = tempo_atual

        return delta_t

    def atualiza_estado(self):
        
        clock = pygame.time.Clock()
        clock.tick(120)
        for evento in pygame.event.get():
            if evento.type != pygame.MOUSEMOTION:
                if evento.type == pygame.QUIT:
                    return False
                elif evento.type == pygame.KEYDOWN or pygame.KEYUP:
                    self.nave.movimenta_nave(evento)
                    self.nave2.movimenta_nave(evento)
        self.sprites_inimigo.update()
        self.sprites_tiro.update()

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return 0
        return 1
    
    def desenha_tela(self):
        
        self.window.fill((255, 255, 255))
        self.window.blit(self.imagem_fundo, (0,0))
        self.nave.desenha_nave()
        self.nave2.desenha_nave()
        self.sprites_inimigo.draw(self.window)
        fonte = pygame.font.Font('Imagens\Rubik-Italic-VariableFont_wght.ttf', 24)
        pontuacao_p1 = fonte.render('pontuação:', True, (115,215,255))
        vidas_p1 = fonte.render('vidas:', True, (115,215,255))
        pontuacao_p2 = fonte.render('pontuação:', True, (255,0,0))
        vidas_p2 = fonte.render('vidas:', True, (255,0,0))
        pontuacao_p1 = self.window.blit(pontuacao_p1, (10, 30))
        vida_p1 = self.window.blit(vidas_p1, (10, 5))
        self.window.blit(pontuacao_p2, (1300, 30))
        self.window.blit(vidas_p2, (1300, 5))


        pygame.display.update()
    
    