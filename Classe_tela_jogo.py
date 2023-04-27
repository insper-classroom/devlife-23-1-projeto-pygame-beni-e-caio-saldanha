import pygame
from Classe_da_nave import Nave
from Classe_do_inimigo import Inimigo
from Classe_cria_barreiras import Barreiras
from Classe_tiro_personagem import TiroPersonagem

class TelaJogo:
    def __init__(self, window):
        pygame.init()

        # TELA E WINDOW
        self.largura = 1520
        self.altura = 760
        self.window = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Galactic Warfare')

        imagem_nave_p1 = pygame.image.load('Imagens\Imagem_p1.png')
        imagem_nave_redimensionada1 = pygame.transform.scale(imagem_nave_p1, (95,95))
        imagem_nave_p2 = pygame.image.load('Imagens\Imagem_p2.png')
        imagem_nave_redimensionada2 = pygame.transform.scale(imagem_nave_p2, (95,95))
        self.imagem_fundo = pygame.image.load('Imagens\SpaceBackground.png')
        imagem_inimigo = pygame.image.load('Imagens\Imagem_inimigo1.png')
        imagem_inimigo_redimensionada = pygame.transform.scale(imagem_inimigo, (50,50))
        largura_inimigo = imagem_inimigo_redimensionada.get_width()
        imagem_tiro_personagem = pygame.image.load('Imagens/tiro_personagem.png')

        self.ultimo_updated = -1
        self.delta_t = self.calcula_deltaT()
        self.nave_pos = [380, 670]
        self.nave = Nave(self.window, self.nave_pos, imagem_nave_redimensionada1, 0, self.delta_t,1)
        self.nave2 = Nave(self.window, [1140, 670], imagem_nave_redimensionada2, 0, self.delta_t,2)
        self.largura_personagem = imagem_nave_redimensionada1.get_width()


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

        self.postiro = [380,670]
        self.sprites_tiro = pygame.sprite.Group()
        # self.tiro = TiroPersonagem([self.postiro[0] + (largura_personagem/2), self.postiro[1]], imagem_tiro_personagem, self.delta_t)


        pygame.mixer.music.load('sons\Trilha Sonora do Game.mp3')
        # pygame.mixer.music.play()
           

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
                    return -1
                elif evento.type == pygame.KEYDOWN or pygame.KEYUP:
                    self.nave.movimenta_nave(evento)
                    self.nave2.movimenta_nave(evento)
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                tiro_pos = [self.nave_pos[0] + (self.largura_personagem/2), self.nave_pos[1]]
                tiro = TiroPersonagem(tiro_pos, self.delta_t)
                self.sprites_tiro.add(tiro)

        self.sprites_tiro.update()
        self.sprites_inimigo.update()

        for i in self.sprites_tiro:
            if tiro_pos[1] > 1400:
                self.sprites_tiro.remove(i)

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
        return 1
    
    def desenha_tela(self):
        
        self.window.fill((255, 255, 255))
        self.window.blit(self.imagem_fundo, (0,0))
        self.nave.desenha_nave()
        self.nave2.desenha_nave()
        self.sprites_inimigo.draw(self.window)
        self.sprites_tiro.draw(self.window)
        fonte = pygame.font.Font('Imagens\Sigmar-Regular.ttf', 24)
        score_p1 = 0
        score_p2 = 0
        pontuacao_p1 = fonte.render(f'score:  {score_p1}', True, (115,215,255))
        vidas_p1 = fonte.render('vidas:', True, (115,215,255))
        pontuacao_p2 = fonte.render(f'score:  {score_p2}', True, (255,0,0))
        vidas_p2 = fonte.render('vidas:', True, (255,0,0))
        self.window.blit(pontuacao_p1, (10, 30))
        self.window.blit(vidas_p1, (10, 5))
        self.window.blit(pontuacao_p2, (1300, 30))
        self.window.blit(vidas_p2, (1300, 5))
        
        for tupla in range(3):
            barreira = pygame.Rect(Barreiras.gera_barreiras(self)[tupla][0], Barreiras.gera_barreiras(self)[tupla][1], 120, 10)
            pygame.draw.rect(self.window, (255,255,255), barreira)


        pygame.display.update()
    
    