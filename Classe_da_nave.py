import pygame


class Nave:
    
    def __init__(self,window,pos,imagem_redimensionada,vel_nave,delta_t,n_nave):
        self.posicao_nave = pos
        self.vel_nave = vel_nave
        self.delta_t = delta_t
        self.window = window
        self.n_nave = n_nave
        self.imagem_redimensionada = imagem_redimensionada

    def desenha_nave(self):
        self.window.blit(self.imagem_redimensionada, self.posicao_nave)


    def movimenta_nave(self, evento):

        v = 30
        
        if self.n_nave == 1:

            if self.posicao_nave[0] < 0:
                self.posicao_nave[0] = 0
            elif self.posicao_nave[0] > 670:
                self.posicao_nave[0] = 670

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_d:
                    self.vel_nave += v
                elif evento.key == pygame.K_a:
                    self.vel_nave -= v
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_d:
                    self.vel_nave -= v
                elif evento.key == pygame.K_a:
                    self.vel_nave += v

            self.posicao_nave[0] += self.vel_nave * self.delta_t
        
        else: 

            if self.posicao_nave[0] < 760:
                self.posicao_nave[0] = 760
            elif self.posicao_nave[0] > 1420:
                self.posicao_nave[0] = 1420

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_l:
                    self.vel_nave += v
                elif evento.key == pygame.K_j:
                    self.vel_nave -= v
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_l:
                    self.vel_nave -= v
                elif evento.key == pygame.K_j:
                    self.vel_nave += v


            self.posicao_nave[0] += self.vel_nave * self.delta_t
