import pygame

class Barreiras:
    def init(self,window,posx,posy,largura,altura):
        self.window = window
        self.posx = posx 
        self.posy = posy
        self.largura = largura
        self.altura = altura
    
    def gera_barreiras(self):
        lista_barreiras = []
        self.posx = 200
        self.posy = 650
        for _ in range(3):
            lista_barreiras.append((self.posx, self.posy))
            self.posx += 500
        
        return lista_barreiras

