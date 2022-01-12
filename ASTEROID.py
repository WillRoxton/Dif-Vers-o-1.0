import pygame
import os
import CONSTANTES
import random



class Asteroid(pygame.sprite.Sprite):
    def __init__(self, index_lista):
        if index_lista >= 3:
            index_lista = 0
        pygame.sprite.Sprite.__init__(self)
        dir_principal = os.path.join(os.getcwd(), "data")
        self.sprite_asteroid = pygame.image.load(os.path.join(dir_principal, CONSTANTES.AST)).convert_alpha()
        asteroid_inteiro = self.sprite_asteroid  # Sprite inteira
        self.lista_para_corte_sprite = []  # Lista comportará os cortes da sprite(asteroid_inteiro)
        for i in range(3):
            img = asteroid_inteiro.subsurface((0, i*32), (CONSTANTES.NAVE_DIMENSAO, CONSTANTES.NAVE_DIMENSAO))
            naves_partes = pygame.transform.scale(img, (CONSTANTES.NAVE_DIMENSAO * 3, CONSTANTES.NAVE_DIMENSAO * 3))
            self.lista_para_corte_sprite.append(naves_partes)
        self.index_lista = index_lista
        self.image = self.lista_para_corte_sprite[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topleft = (1350, random.randint(100, 600))
        self.mask = pygame.mask.from_surface(self.image)


    def update(self):

        if self.rect.topright[0] < 0:
            self.rect.x = 1650 - random.randrange(30, 200, 50)
            self.rect.y = random.randrange(50, 650, 50)
        self.rect.x -= 5