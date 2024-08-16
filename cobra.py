import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo Snake Python")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# Parâmetros da cobrinha
tamanho_quadrado = 20
velocidade_jogo = 10

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * tamanho_quadrado
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * tamanho_quadrado
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def selecionar_velocidade(tecla, velocidade_atual_x, velocidade_atual_y):
    if tecla == pygame.K_DOWN and velocidade_atual_y == 0:
        return 0, tamanho_quadrado
    elif tecla == pygame.K_UP and velocidade_atual_y == 0:
        return 0, -tamanho_quadrado
    elif tecla == pygame.K_RIGHT and velocidade_atual_x == 0:
        return tamanho_quadrado, 0
    elif tecla == pygame.K_LEFT and velocidade_atual_x == 0:
        return -tamanho_quadrado, 0
    return velocidade_atual_x, velocidade_atual_y

def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0 
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)

        x += velocidade_x
        y += velocidade_y

        # Verificar colisão com as bordas
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        # Verificar se a cobra comeu a comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        # Atualizar a posição da cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # Verificar colisão com o próprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        desenhar_cobra(tamanho_quadrado, pixels)

        pygame.display.update()
        relogio.tick(velocidade_jogo)

    pygame.quit()

rodar_jogo()