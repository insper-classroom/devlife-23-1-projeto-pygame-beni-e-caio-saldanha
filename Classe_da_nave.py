import pygame


class Nave:
    
    def __init__(self,window,pos,imagem_redimensionada,vel_nave,delta_t,n_nave):
        self.posicao_nave = pos
        self.vel_nave = vel_nave
        self.delta_t = delta_t
        self.window = window
        self.n_nave = n_nave
        imagem = pygame.image.load('nave do joguinho.png')
        imagem_redimensionada = pygame.transform.scale(imagem, (100,100))
        self.imagem_redimensionada = imagem_redimensionada

    def desenha_nave(self):
        self.window.blit(self.imagem_redimensionada, self.posicao_nave)


    def movimenta_nave(self, evento):
        
        if self.n_nave == 1:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_d:
                    self.vel_nave += 30
                elif evento.key == pygame.K_a:
                    self.vel_nave -= 30
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_d:
                    self.vel_nave -= 30
                elif evento.key == pygame.K_a:
                    self.vel_nave += 30

        else:        
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    self.vel_nave += 30
                elif evento.key == pygame.K_LEFT:
                    self.vel_nave -= 30
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT:
                    self.vel_nave -= 30
                elif evento.key == pygame.K_LEFT:
                    self.vel_nave += 30

        self.posicao_nave[0] += self.vel_nave * self.delta_t
