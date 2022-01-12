import pygame
import CONSTANTES
import os
import random
from NAVE import Nave
from ASTEROID import Asteroid
from SHOT import Shot

# diretorio principal, arquivos de imagens, sprites, audios
dir_principal = os.path.join(os.getcwd(), 'data')

# display principal
tela_principal = pygame.display.set_mode([CONSTANTES.w_tela, CONSTANTES.h_tela])
pygame.display.set_caption("DIF V1.00")
# Controle de FPS
frame = pygame.time.Clock()

# Pontos

Pontos = 0000000
timer = 0

# Controle do loop
IN_GAME = True
GAME__OVER = False

# função condicional de sair do jogo

# Classe correspondente a tela de inicio do jogo

pygame.init()
pygame.mixer.init()
pygame.font.init()

# Todas as sprites
todas_as_sprites = pygame.sprite.Group()
todos_os_asteroids = pygame.sprite.Group()
laser_group = pygame.sprite.Group()

# Background1

bg = pygame.sprite.Sprite(todas_as_sprites)
bg.image = pygame.image.load(os.path.join(dir_principal, CONSTANTES.FUNDO_FASE1))
bg.image = pygame.transform.scale(bg.image, [CONSTANTES.w_tela, CONSTANTES.h_tela])
bg.rect = bg.image.get_rect()
bg.rect.topleft = (0, 0)

# Objetos

# Função correspondete aos asteroids e a logica de produção dos mesmos
newasteroid = Asteroid(random.randint(0, 4))
todos_os_asteroids.add(newasteroid)


def novos_asteriods():
    global timer, Pontos
    timer += 2
    if timer > 30:
        timer = 0
        if random.random() > 0.8:
            newasteroid = Asteroid(random.randint(0,4))
            todas_as_sprites.add(newasteroid)
            todos_os_asteroids.add(newasteroid)
            if random.random() > 0.5 and newasteroid.rect.right <= 0:
                newasteroid.kill()

nave1 = Nave()
laser = Shot()
todas_as_sprites.add(laser)
todas_as_sprites.add(nave1)
laser_group.add(laser)

# Classe correspondente ao objeto da tela principal

class Inicio:

    def __init__(self):  # Os atributos correspondem as imagens e fonte e som
        self.dif = pygame.image.load(os.path.join(dir_principal, CONSTANTES.DIF))
        self.dif = pygame.transform.scale(self.dif, (250, 250))
        self.caveira = pygame.image.load(os.path.join(dir_principal, CONSTANTES.CAV))
        self.caveira = pygame.transform.scale(self.caveira, (700, 350))
        self.fonte = pygame.font.match_font(CONSTANTES.FONTE1)
        self.musica_inicial = (os.path.join(dir_principal, CONSTANTES.MUSICA_TELA_INICIAL))

    def posicao_dif(self):
        logo_dif = self.dif.get_rect()
        logo_dif.center = (CONSTANTES.w_tela/2, CONSTANTES.h_tela - 280)
        tela_principal.blit(self.dif, logo_dif)

    def posicao_caveira(self):
        LOGO_CAVEIRA = self.caveira.get_rect()
        LOGO_CAVEIRA.center = (CONSTANTES.w_tela/2, CONSTANTES.h_tela - 550)
        tela_principal.blit(self.caveira, LOGO_CAVEIRA)

    def posicao_texto1(self, texto, tamanho, cor, x, y):
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto1 = fonte.render(texto, False, cor)
        texto1_rect = texto1.get_rect()
        texto1_rect.midtop = (x, y)
        tela_principal.blit(texto1, texto1_rect)

    def posicao_nome_do_vagabundo_que_fez(self, texto, tamanho, cor, x, y):
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto1 = fonte.render(texto, False, cor)
        texto1_rect = texto1.get_rect()
        texto1_rect.midtop = (x, y)
        tela_principal.blit(texto1, texto1_rect)

    def todos_os_objetos(self):

        pygame.mixer.music.load(self.musica_inicial)
        pygame.mixer.music.play(-1)
        tela_principal.fill(CONSTANTES.CINZA1)
        self.posicao_caveira()
        self.posicao_dif()
        self.posicao_texto1(")>Aperte uma tecla para começar<(", 30, CONSTANTES.PRETO1, CONSTANTES.w_tela/2, CONSTANTES.h_tela - 150)
        self.posicao_nome_do_vagabundo_que_fez("Will 2022", 15, CONSTANTES.BRANCO1, CONSTANTES.w_tela/2, CONSTANTES.h_tela - 50)

        pygame.display.update()
        self.sair_tela()

    def sair_tela(self):

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    pygame.mixer.music.pause()
                    pygame.mixer.Sound(os.path.join(dir_principal, CONSTANTES.START)).play()

def Game_Over():
    global IN_GAME

    for event in pygame.key.get_pressed():
        if event.type == pygame.K_ESCAPE:
            pygame.quit()
        elif event.type == pygame.K_r:
            sair_jogo()
            while IN_GAME:
                frame.tick(CONSTANTES.FPS)
                sair_jogo()
                tela_principal.fill(CONSTANTES.BRANCO1)
                tela_principal.blit(bg.image, (0, 0))
                colissoes()
                novos_asteriods()
                todas_as_sprites.draw(tela_principal)
                pontuacao(50, f"SCORE:{Pontos}", [255, 255, 0], 1000, 100)
                todas_as_sprites.update()
                todos_os_asteroids.update()
                pygame.display.update()


# funçoes (colissoes e perdeu) incluem a logica de game over caso a nave colida com o asteroid

def colissoes():
    global Pontos,GAME__OVER
    if pygame.sprite.spritecollide(nave1, todos_os_asteroids, True, pygame.sprite.collide_mask):
        pygame.mixer.music.load(os.path.join(dir_principal, CONSTANTES.GAME_DOWN))
        pygame.mixer.music.play(-1)
        GAME__OVER = True
        perdeu()

def perdeu():
    global Pontos, GAME__OVER
    while GAME__OVER:

        frame.tick(0)
        tela_principal.fill(CONSTANTES.PRETO1)
        Fonte = pygame.font.match_font(CONSTANTES.FONTE1)
        fonte = pygame.font.Font(Fonte, 40)
        txt1 = fonte.render("GAME OVER", False, [255, 255, 255])
        txt2 = fonte.render("Aperte r para recomeçar", False, [255, 255, 255])
        score = fonte.render( f"SEU SCORE:{Pontos}", False, [255, 255, 255])
        score_rect = score.get_rect()
        txt2_rect = txt2.get_rect()
        txt1_rect = txt1.get_rect()
        txt2_rect.center = [CONSTANTES.w_tela / 2, (CONSTANTES.h_tela / 2) + 100]
        txt1_rect.center = [CONSTANTES.w_tela / 2, CONSTANTES.h_tela / 2]
        score_rect.center = [CONSTANTES.w_tela/2,(CONSTANTES.h_tela / 2) + 200]
        tela_principal.blit(txt1, txt1_rect)
        tela_principal.blit(txt2, txt2_rect)
        tela_principal.blit(score, score_rect)
        todos_os_asteroids.remove()
        pygame.display.flip()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
            elif keys[pygame.K_ESCAPE]:
                pygame.quit()
            elif keys[pygame.K_r]:
                GAME__OVER = False
                pygame.mixer.music.pause()
                Pontos = 00000000

    else:
        pass

# função correspondente a colisao do projectil e o asteroid
def laser_asteroid():
    global Pontos
    colidiu = pygame.sprite.groupcollide(laser_group, todos_os_asteroids, True, True)
    if colidiu:
        Pontos += 100


# função do desenho da pontuação
def pontuacao(tamanho, texto, cor, x, y):
    Fonte = pygame.font.match_font(CONSTANTES.FONTE1)
    fonte = pygame.font.Font(Fonte, tamanho)
    txt1 = fonte.render(texto, False, cor)
    txt1_rect = txt1.get_rect()
    txt1_rect.center = [x, y]
    tela_principal.blit(txt1, bg)


def sair_jogo():
    frame.tick(CONSTANTES.FPS)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
        elif keys[pygame.K_SPACE]:
            pygame.mixer.Sound(os.path.join(dir_principal, CONSTANTES.TIRO)).play()
            laser = Shot()
            todas_as_sprites.add(laser)
            laser_group.add(laser)
            laser.rect.center = nave1.rect.center





if __name__ == "__main__":

    New_Game = Inicio()
    New_Game.todos_os_objetos()
    sair_jogo()
    while IN_GAME:

        sair_jogo()
        tela_principal.fill(CONSTANTES.BRANCO1)
        tela_principal.blit(bg.image, (0, 0))
        novos_asteriods()
        laser_asteroid()
        todas_as_sprites.draw(tela_principal)
        pontuacao(50, f"SCORE:{Pontos}", [255, 255, 0], 1000, 100)
        colissoes()
        todas_as_sprites.update()
        todos_os_asteroids.update()
        pygame.display.flip()



