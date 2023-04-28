import pygame

class TelaVitoria:
    def __init__(self, window):
        self.window = window

    def desenha_tela(self):
        self.window.fill((255,0,0))