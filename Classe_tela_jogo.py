import pygame
import random
from Classe_da_nave import Nave
from Classe_do_inimigo import Inimigo
from Classe_tiro_personagem import TiroPersonagem
from Classe_tiro_inimigo import TiroInimigo

class TelaJogo:
    """
    A classe TelaJogo define a tela e os objetos do jogo.
    
    Atributos:
    - window (Surface): superfície onde o jogo é renderizado.
    - largura (int): largura da janela.
    - altura (int): altura da janela.
    - imagem_fundo (Surface): imagem do fundo do jogo.
    - nave (Nave): nave do jogador 1.
    - nave2 (Nave): nave do jogador 2.
    - grupo_personagem (Group): grupo que contém as naves dos jogadores.
    - largura_personagem (int): largura da imagem das naves dos jogadores.
    - sprites_inimigo (Group): grupo que contém os inimigos do jogo.
    - sprites_tiro (Group): grupo que contém os tiros das naves dos jogadores.
    - sprites_tiro_inimigo (Group): grupo que contém os tiros dos inimigos.
    - som_tiro (Sound): som do tiro das naves dos jogadores.
    - ultimo_updated (int): momento da última atualização.
    - delta_t (float): tempo desde a última atualização.
    - nave1_pos (list): lista com a posição inicial da nave do jogador 1.
    - nave2_pos (list): lista com a posição inicial da nave do jogador 2.
    
    Métodos:
    - __init__(self, window): inicializa a janela e os objetos do jogo.
    - calcula_deltaT(self): calcula o tempo desde a última atualização.
    - atualiza_estado(self): atualiza o estado do jogo.
    """

    def __init__(self, window):
        """
        Inicializa a janela e os objetos do jogo.

        Argumentos:
        - window (Surface): superfície onde o jogo é renderizado.
        """
        pygame.init()

        self.largura = 1520
        self.altura = 760
        self.window = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Galactic Warfare')

        TIRO = pygame.image.load('Imagens/tiro_personagem.png')
        TIRO_REDIMENSIONADO = pygame.transform.scale_by(TIRO, 2)
        TIRO_INIMIGO = pygame.image.load('Imagens/tiro_inimigo.png')

        imagem_nave_p1 = pygame.image.load('Imagens\Imagem_p1.png')
        imagem_nave_redimensionada1 = pygame.transform.scale(imagem_nave_p1, (95,95))
        self.img_vidas = pygame.transform.scale(imagem_nave_p1, (40,40))
        self.lista_de_vidas_1 = [(90,5),(120,5),(150,5)]
        self.contador_vidas_1 = 3
        imagem_nave_p2 = pygame.image.load('Imagens\Imagem_p2.png')
        imagem_nave_redimensionada2 = pygame.transform.scale(imagem_nave_p2, (95,95))
        self.img_vidas_2 = pygame.transform.scale(imagem_nave_p2, (40,40))
        self.lista_de_vidas_2 = [(1380,5),(1410,5),(1440,5)]
        self.contador_vidas_2 = 3
        self.imagem_fundo = pygame.image.load('Imagens\SpaceBackground.png')
        imagem_inimigo = pygame.image.load('Imagens\Imagem_inimigo1.png')
        imagem_inimigo_redimensionada = pygame.transform.scale(imagem_inimigo, (50,50))
        largura_inimigo = imagem_inimigo_redimensionada.get_width()

        self.lista_sprites_tiro_personagem = []
        for i in range (3):
            imagem_tiro_personagem = TIRO_REDIMENSIONADO.subsurface((i * 10, 0), (10, 40))
            self.lista_sprites_tiro_personagem.append(imagem_tiro_personagem)
        index_tiro_personagem = 0
        self.img_tiro_personagem = self.lista_sprites_tiro_personagem[index_tiro_personagem]

        self.lista_sprites_tiro_inimigo = []
        for i2 in range (4):
            imagem_tiro_inimigo = TIRO_INIMIGO.subsurface((i2 * 18, 0), (18, 38))
            self.lista_sprites_tiro_inimigo.append(imagem_tiro_inimigo)
        index_tiro_inimigo = 0
        self.img_tiro_inimigo = self.lista_sprites_tiro_inimigo[index_tiro_inimigo]

        self.ultimo_updated = -1
        self.delta_t = self.calcula_deltaT()
        self.nave1_pos = [380, 670]
        self.nave2_pos = [1140, 670]
        self.grupo_personagem = pygame.sprite.Group()
        self.nave = Nave(self.nave1_pos, imagem_nave_redimensionada1, self.delta_t,1)
        self.nave2 = Nave(self.nave2_pos, imagem_nave_redimensionada2, self.delta_t,2)
        self.grupo_personagem.add(self.nave)
        self.grupo_personagem.add(self.nave2)
        self.largura_personagem = imagem_nave_redimensionada1.get_width()
        self.score_p1 = 0
        self.score_p2 = 0

        self.som_tiro = pygame.mixer.Sound('sons\Som-do-tiro-dos-Players.wav')
        self.som_tiro_inimigo = pygame.mixer.Sound('sons\Som-tiro-do-inimigo.wav')
        self.explosao_inimiga = pygame.mixer.Sound('sons\explosão_inimiga.wav')
        self.explosao_player = pygame.mixer.Sound('sons\explosão_player.wav')

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
        self.sprites_tiro_inimigo = pygame.sprite.Group()

        pygame.mixer.music.load('sons\Trilha Sonora do Game.mp3')
        pygame.mixer.music.play(loops=-1)

    def calcula_deltaT(self):
        """
        calcula o tempo desde a ultima atualização
        """

        tempo_atual = pygame.time.get_ticks()
        delta_t = (tempo_atual - self.ultimo_updated) / 1000
        self.ultimo_updated = tempo_atual

        return delta_t

    def atualiza_estado(self):
        """
        Atualiza a tela de gameplay
        """
        
        clock = pygame.time.Clock()
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type != pygame.MOUSEMOTION:
                if evento.type == pygame.QUIT:
                    return -1
                elif evento.type == pygame.KEYDOWN or pygame.KEYUP:
                    self.nave.movimenta_nave(evento)
                    self.nave2.movimenta_nave(evento)
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_w:
                    tiro = TiroPersonagem([self.nave.rect.x + (self.largura_personagem/2), self.nave1_pos[1]], self.delta_t,'p1', self.lista_sprites_tiro_personagem)
                    self.sprites_tiro.add(tiro)
                    self.som_tiro.play()

                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_i:
                    tiro = TiroPersonagem([self.nave2.rect.x + (self.largura_personagem/2), self.nave2_pos[1]], self.delta_t, 'p2', self.lista_sprites_tiro_personagem)
                    self.sprites_tiro.add(tiro)
                    self.som_tiro.play() 
            

        self.sprites_tiro.update()
        self.sprites_inimigo.update()


        numero_sorteado = random.randint(1, 25)

        for inimigo in self.sprites_inimigo:
            for tiro_i in self.sprites_tiro:
                if pygame.sprite.collide_rect(inimigo, tiro_i):
                    self.sprites_inimigo.remove(inimigo)
                    self.sprites_tiro.remove(tiro_i)
                    self.explosao_inimiga.play()
                    if tiro_i.quem_atirou == 'p1':
                        self.score_p1 += 30
                    elif tiro_i.quem_atirou == 'p2':
                        self.score_p2 += 30
                elif tiro_i.rect.y < 0:
                    self.sprites_tiro.remove(tiro_i)

        if numero_sorteado == 3:
            if len(self.sprites_inimigo) > 1:
                inimigo_aleatorio = random.choice(self.sprites_inimigo.sprites())
                tiro_inimigo = TiroInimigo((inimigo_aleatorio.rect.x, inimigo_aleatorio.rect.y), self.delta_t, self.lista_sprites_tiro_inimigo)
                self.sprites_tiro_inimigo.add(tiro_inimigo)
                self.som_tiro_inimigo.play()
            else:
                for inimigo in self.sprites_inimigo:
                    tiro_inimigo = TiroInimigo((inimigo.rect.x, inimigo.rect.y), self.delta_t, self.lista_sprites_tiro_inimigo)
                    self.sprites_tiro_inimigo.add(tiro_inimigo)
                    self.som_tiro_inimigo.play()
        for tiro_i2 in self.sprites_tiro_inimigo:
            if tiro_i2.rect.y > 760:
                self.sprites_tiro_inimigo.remove(tiro_i2)
        if pygame.sprite.spritecollide(self.nave, self.sprites_tiro_inimigo, True):
            self.lista_de_vidas_1.pop()
            self.contador_vidas_1 -= 1
            self.explosao_player.play()
        if pygame.sprite.spritecollide(self.nave2, self.sprites_tiro_inimigo, True):
            self.lista_de_vidas_2.pop()
            self.contador_vidas_2 -= 1
            self.explosao_player.play()

        self.sprites_tiro_inimigo.update()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
        if len(self.sprites_inimigo) == 0:
            if self.score_p1 > self.score_p2:
                return 3
            else:
                return 4
        if self.inimigo.rect.y > 640:
            return 5
        if self.contador_vidas_1 == 0:
            return 4
        if self.contador_vidas_2 == 0:
            return 3
        return 1
    
    def desenha_tela(self):
        """
        Desenha na tela do jogo
        """
        
        self.window.fill((255, 255, 255))
        self.window.blit(self.imagem_fundo, (0,0))
        self.sprites_inimigo.draw(self.window)
        self.sprites_tiro.draw(self.window)
        self.sprites_tiro_inimigo.draw(self.window)
        self.grupo_personagem.draw(self.window)
        fonte = pygame.font.Font('Imagens\Sigmar-Regular.ttf', 24)
        pontuacao_p1 = fonte.render(f'score:  {self.score_p1}', True, (115,215,255))
        vidas_p1 = fonte.render('vidas:', True, (115,215,255))
        pontuacao_p2 = fonte.render(f'score:  {self.score_p2}', True, (255,0,0))
        vidas_p2 = fonte.render('vidas:', True, (255,0,0))
        self.window.blit(pontuacao_p1, (10, 30))
        self.window.blit(vidas_p1, (10, 5))
        for self.posicao in self.lista_de_vidas_1:
            self.window.blit(self.img_vidas, self.posicao)
        self.window.blit(pontuacao_p2, (1300, 30))
        self.window.blit(vidas_p2, (1300, 5))
        for posicao in self.lista_de_vidas_2:
            self.window.blit(self.img_vidas_2,posicao)   


        pygame.display.update()   