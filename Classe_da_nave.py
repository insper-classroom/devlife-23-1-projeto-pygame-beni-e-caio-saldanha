import pygame


class Nave(pygame.sprite.Sprite):
    
    def __init__(self,pos,imagem_redimensionada,delta_t,n_nave):
        pygame.sprite.Sprite.__init__(self)
        self.vel_nave1 = 0
        self.vel_nave2 = 0
        self.delta_t = delta_t
        self.n_nave = n_nave
        self.image = imagem_redimensionada
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def movimenta_nave(self, evento):

        v = 30
        
        if self.n_nave == 1:

            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > 1440:
                self.rect.x = 1440

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_d:
                    self.vel_nave1 += v
                elif evento.key == pygame.K_a:
                    self.vel_nave1-= v
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_d:
                    self.vel_nave1 -= v
                elif evento.key == pygame.K_a:
                    self.vel_nave1 += v

            self.rect.x += self.vel_nave1 * self.delta_t
            
        
        else: 

            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > 1440:
                self.rect.x = 1440

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_l:
                    self.vel_nave2 += v
                elif evento.key == pygame.K_j:
                    self.vel_nave2 -= v
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_l:
                    self.vel_nave2 -= v
                elif evento.key == pygame.K_j:
                    self.vel_nave2 += v


            self.rect.x += self.vel_nave2 * self.delta_t

# class NaveVermelha(Nave):
    