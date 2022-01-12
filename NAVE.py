import pygame
import os
import CONSTANTES

frame = pygame.time.Clock()

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        dir_principal = os.path.join(os.getcwd(), "data")
        self.sprite_nave = pygame.image.load(os.path.join(dir_principal, CONSTANTES.NAVE_RED)).convert_alpha()
        nave_inteira = self.sprite_nave  # Sprite inteira
        self.lista_para_corte_sprite = []  # Lista comportará os cortes da sprite(nave_red_inteira)
        for i in range(13):
            img = nave_inteira.subsurface((i*32, 0), (CONSTANTES.ASTEROID_DIMENSAO, CONSTANTES.ASTEROID_DIMENSAO))
            naves_partes = pygame.transform.scale(img, (CONSTANTES.ASTEROID_DIMENSAO * 3, CONSTANTES.ASTEROID_DIMENSAO * 3))
            self.lista_para_corte_sprite.append(naves_partes)
        self.index_lista = 0
        self.image = self.lista_para_corte_sprite[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.topright = (100, 100)
        self.mask = pygame.mask.from_surface(self.image)


    def update(self):

        if self.index_lista > 12:
            self.index_lista = 0
        self.index_lista += 0.5
        self.image = self.lista_para_corte_sprite[int(self.index_lista)]

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.rect.y -= 10
                if self.rect.top < 0:
                    self.rect.y = 0
            elif keys[pygame.K_s]:
                self.rect.y += 10
                if self.rect.bottom > CONSTANTES.h_tela:
                    self.rect.y = CONSTANTES.h_tela - 64
            elif keys[pygame.K_d]:
                self.rect.x += 10
                if self.rect.right > CONSTANTES.w_tela:
                    self.rect.right = CONSTANTES.w_tela
            elif keys[pygame.K_a]:
                self.rect.x -= 10
                if self.rect.left < 0:
                    self.rect.x = 0