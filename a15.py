import random
import os
import time
import sys

# função para limpar tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dicionário de personagens e seus golpes únicos com cooldowns
personagens = {
    'Adaga': [
        {"nome": "Facada Rápida", "dano_min": 8, "dano_max": 15, "cooldown": 0},
        {"nome": "Estocada Mortal", "dano_min": 15, "dano_max": 20, "cooldown": 1},
        {"nome": "Arremesso de Adaga", "dano_min": 15, "dano_max": 35, "cooldown": 2}
    ],
    'Ghost': [
        {"nome": "Soco Fantasma", "dano_min": 10, "dano_max": 18, "cooldown": 0},
        {"nome": "Garras Sombras", "dano_min": 12, "dano_max": 22, "cooldown": 1},
        {"nome": "Sombra Ilusória", "dano_min": 0, "dano_max": 0, "efeito": "esquiva", "cooldown": 2}
    ],
    'Crawler': [
        {"nome": "Garras Selvagens", "dano_min": 9, "dano_max": 16, "cooldown": 0},
        {"nome": "Investida Violenta", "dano_min": 14, "dano_max": 24, "cooldown": 1},
        {"nome": "Rugido Aterrorizante", "dano_min": 0, "dano_max": 0, "efeito": "enfraquecer", "cooldown": 2}
    ],
}

def ataque(golpe):
    return random.randint(golpe['dano_min'], golpe['dano_max'])

cooldowns = {1: {}, 2: {}}
status = {1: {}, 2: {}}

while True:
    limpar_tela()
    print("\tJogo de luta!")
    print("(1) Jogar")
    print("(0) Sair")
    opcao = input("Digite a opção: ")

    if opcao == '0':
        print("Saindo do jogo.")
        break
    elif opcao == '1':
        vida_um = 100
        vida_dois = 100
        cooldowns = {1: {}, 2: {}}
        status = {1: {}, 2: {}}

        print("Jogador 1 escolha seu personagem:")
        print("(1) Adaga\n(2) Ghost\n(3) Crawler")
        escolha_um = input("Digite a opção: ")
        personagens_lista = ['Adaga', 'Ghost', 'Crawler']
        if escolha_um not in ['1', '2', '3']:
            print("Escolha inválida.")
            time.sleep(2)
            continue
        escolha_personagem_um = personagens_lista[int(escolha_um) - 1]

        print(f"Jogador 1 escolheu {escolha_personagem_um}.\n")

        print("Jogador 2 escolha seu personagem:")
        print("(1) Adaga\n(2) Ghost\n(3) Crawler")
        escolha_dois = input("Digite a opção: ")
        if escolha_dois not in ['1', '2', '3']:
            print("Escolha inválida.")
            time.sleep(2)
            continue
        escolha_personagem_dois = personagens_lista[int(escolha_dois) - 1]

        print(f"Jogador 2 escolheu {escolha_personagem_dois}.")
        time.sleep(2)
        limpar_tela()

        print("Decidindo quem joga primeiro...")
        time.sleep(2)
        jogador_vez = random.choice([1, 2])
        print(f"\nJogador {jogador_vez} começa!")

        while vida_um > 0 and vida_dois > 0:
            print("\n---------------------------")
            if jogador_vez == 1:
                jogador, oponente = 1, 2
                personagem, inimigo = escolha_personagem_um, escolha_personagem_dois
                vida_jogador, vida_oponente = vida_um, vida_dois
            else:
                jogador, oponente = 2, 1
                personagem, inimigo = escolha_personagem_dois, escolha_personagem_um
                vida_jogador, vida_oponente = vida_dois, vida_um

            print(f"{personagem} (JOGADOR {jogador})\nHP: {vida_jogador}")
            print("Escolha seu golpe:")
            golpes = personagens[personagem]

            for idx, g in enumerate(golpes, start=1):
                cd_restante = cooldowns[jogador].get(idx, 0)
                cd_texto = f" (CD: {cd_restante} turno(s))" if cd_restante > 0 else ""
                print(f"({idx}) {g['nome']} (Dano {g['dano_min']}-{g['dano_max']}){cd_texto}")

            escolha = input("Digite a opção: ")
            if not escolha.isdigit() or int(escolha) not in range(1, len(golpes)+1):
                print("Golpe inválido, perdeu a vez!")
            else:
                escolha = int(escolha)
                golpe_escolhido = golpes[escolha - 1]
                if cooldowns[jogador].get(escolha, 0) > 0:
                    print(f"{golpe_escolhido['nome']} está em cooldown. Perdeu a vez!")
                else:
                    if 'efeito' in golpe_escolhido:
                        if golpe_escolhido['efeito'] == 'esquiva':
                            status[jogador]['esquiva'] = True
                            print(f"{personagem} ativou esquiva e evitará o próximo ataque!")
                        elif golpe_escolhido['efeito'] == 'enfraquecer':
                            status[oponente]['enfraquecido'] = 1
                            print(f"{personagem} usou {golpe_escolhido['nome']} e enfraqueceu {inimigo}!")
                    else:
                        dano = ataque(golpe_escolhido)
                        if status[oponente].get('esquiva'):
                            print(f"{inimigo} esquivou do ataque!")
                            status[oponente].pop('esquiva')
                        else:
                            if status[oponente].get('enfraquecido'):
                                dano = dano // 2
                                status[oponente]['enfraquecido'] -= 1
                            vida_oponente -= dano
                            print(f"{personagem} usou {golpe_escolhido['nome']} e causou {dano} de dano em {inimigo}!")
                    if golpe_escolhido['cooldown'] > 0:
                        cooldowns[jogador][escolha] = golpe_escolhido['cooldown'] + 1

            for i in cooldowns[jogador]:
                if cooldowns[jogador][i] > 0:
                    cooldowns[jogador][i] -= 1

            if jogador == 1:
                vida_um, vida_dois = vida_jogador, vida_oponente
            else:
                vida_dois, vida_um = vida_jogador, vida_oponente

            jogador_vez = 2 if jogador_vez == 1 else 1
            time.sleep(2)
            limpar_tela()

        print("\n--- FIM DE JOGO ---")
        if vida_um <= 0:
            print(f"{escolha_personagem_dois} venceu!")
        else:
            print(f"{escolha_personagem_um} venceu!")

        sair_do_jogo = input("Deseja jogar novamente? [S/N] ").strip().upper()
        if sair_do_jogo != 'S':
            print("Saindo do jogo.")
            break
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(2)
