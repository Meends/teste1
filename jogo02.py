import pygame
import sys
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Combate em Turnos")
clock = pygame.time.Clock()

# Fontes
font_titulo = pygame.font.SysFont(None, 50)
font_botao = pygame.font.SysFont(None, 40)
font_normal = pygame.font.SysFont(None, 36)
font_grande = pygame.font.SysFont(None, 48)

# Estados de tela: "menu" ou "combate"
tela_atual = "menu"

# --- Menu ---
menu_titulo = font_titulo.render("Combate Escuro", True, (255, 255, 255))
menu_titulo_rect = menu_titulo.get_rect(center=(400, 50))
botao_jogar_rect = pygame.Rect(0, 0, 120, 50)
botao_jogar_rect.center = (400, 300)

# --- Combate ---
player_hp = 100
enemy_hp = 100
turn = "player"
mensagem = "Sua vez! Escolha um ataque:"
player_defendendo = False

opcoes = ["Golpe Fraco", "Golpe Forte", "Defender"]
botao_rects = []
start_y = 350
for i in range(len(opcoes)):
    rect = pygame.Rect(300, start_y + i*60, 200, 50)
    botao_rects.append(rect)

botao_clicado = None

def desenha_botao_menu(mouse_pos):
    centro_padrao = (400, 300)
    if botao_jogar_rect.collidepoint(mouse_pos):
        blink = pygame.time.get_ticks() % 1000 < 500
        cor = (255, 255, 0) if blink else (255, 255, 255)
        fonte_hover = pygame.font.SysFont(None, 48)
        texto = fonte_hover.render("Jogar", True, cor)
        tempo = pygame.time.get_ticks()
        deslocamento_x = 3 * math.sin(tempo * 0.01)
        angulo = 5 * math.sin(tempo * 0.005)
        texto_rot = pygame.transform.rotate(texto, angulo)
        rect = texto_rot.get_rect(center=(centro_padrao[0] + deslocamento_x, centro_padrao[1]))
        screen.blit(texto_rot, rect)
    else:
        texto = font_botao.render("Jogar", True, (255, 255, 255))
        screen.blit(texto, botao_jogar_rect)

def desenha_tela_menu(mouse_pos):
    screen.fill((0, 0, 0))
    screen.blit(menu_titulo, menu_titulo_rect)
    desenha_botao_menu(mouse_pos)

def desenha_tela_combate():
    screen.fill((0, 0, 0))

    # HP
    player_text = font_normal.render(f"Jogador HP: {max(player_hp, 0)}", True, (255, 255, 255))
    enemy_text = font_normal.render(f"Inimigo HP: {max(enemy_hp, 0)}", True, (255, 255, 255))
    screen.blit(player_text, (50, 50))
    screen.blit(enemy_text, (500, 50))

    # Mensagem
    mensagem_text = font_grande.render(mensagem, True, (255, 255, 0))
    screen.blit(mensagem_text, (50, 150))

    # Opções do jogador
    if turn == "player":
        for i, rect in enumerate(botao_rects):
            cor = (100, 100, 250) if botao_clicado == i else (50, 50, 200)
            pygame.draw.rect(screen, cor, rect)
            opc_text = font_normal.render(opcoes[i], True, (255, 255, 255))
            opc_text_rect = opc_text.get_rect(center=rect.center)
            screen.blit(opc_text, opc_text_rect)

# Loop principal
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if tela_atual == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if botao_jogar_rect.collidepoint(mouse_pos):
                    # Começa o combate
                    tela_atual = "combate"
                    # Reseta o combate
                    player_hp = 100
                    enemy_hp = 100
                    turn = "player"
                    mensagem = "Sua vez! Escolha um ataque:"
                    player_defendendo = False
                    botao_clicado = None

        elif tela_atual == "combate":
            if turn == "player" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, rect in enumerate(botao_rects):
                    if rect.collidepoint(mouse_pos):
                        botao_clicado = i
                        # Ações
                        if opcoes[i] == "Golpe Fraco":
                            dano = 10
                            mensagem = f"Você causou {dano} de dano!"
                            enemy_hp -= dano
                            player_defendendo = False
                        elif opcoes[i] == "Golpe Forte":
                            dano = 20
                            mensagem = f"Você causou {dano} de dano!"
                            enemy_hp -= dano
                            player_defendendo = False
                        elif opcoes[i] == "Defender":
                            mensagem = "Você se defendeu! Menos dano no próximo ataque inimigo."
                            player_defendendo = True

                        turn = "enemy"

    if tela_atual == "combate" and turn == "enemy":
        dano = random.choice([5, 15])
        if player_defendendo:
            dano //= 2
            mensagem = f"Inimigo atacou, mas você defendeu! Dano reduzido para {dano}."
        else:
            mensagem = f"Inimigo causou {dano} de dano!"
        player_hp -= dano
        player_defendendo = False
        turn = "player"
        botao_clicado = None

    # Fim de jogo
    if tela_atual == "combate":
        if player_hp <= 0:
            mensagem = "Você perdeu! Feche o jogo para tentar de novo."
            turn = None
        elif enemy_hp <= 0:
            mensagem = "Você venceu! Feche o jogo para jogar novamente."
            turn = None

    # Desenho
    if tela_atual == "menu":
        desenha_tela_menu(mouse_pos)
    elif tela_atual == "combate":
        desenha_tela_combate()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
