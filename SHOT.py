import pygame
import os
import CONSTANTES




class Shot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        dir_principal = os.path.join(os.getcwd(), "data")
        self.sprite_laser = pygame.image.load(os.path.join(dir_principal, CONSTANTES.LASER)).convert_alpha()
        self.image = self.sprite_laser
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def update(self):

        self.rect.x += 20
        if self.rect.left > CONSTANTES.w_tela:
            self.kill()

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


