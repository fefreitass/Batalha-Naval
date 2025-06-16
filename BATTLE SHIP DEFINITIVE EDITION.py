import random
import time

# Cores solicitadas
AZUL = '\033[94m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
VERDE = '\033[92m'
CINZA = '\033[90m'
CIANO = '\033[96m'
RESET = '\033[0m'

# Tamanhos dos navios
tamanho_navios = [2, 2, 3, 3, 4, 5]

# Cria um dicionário que mapeia letras para números, dependendo do tamanho do tabuleiro
def escala_tabuleiro(tamanho):
    letras = {}
    if tamanho == 10:
        letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
    elif tamanho == 12:
        letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11}
    elif tamanho == 15:
        letras = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,"K": 10, "L": 11, "M": 12, "N": 13, "O": 14}
    return letras

# Imprime o tabuleiro
def print_tabuleiro(tabuleiro):
    # Faz que tenha os espacos corretos para o tamanho do tabuleiro
    print("  ", end="  ")
    for letra in letras_para_numero:
        print(f"{AMARELO}{letra}{RESET} ", end="  ")
    print()
    linha_num = 1
    # Altera o tabuleiro com os termos e as cores solicitadas
    for linha in tabuleiro:
        linha_texto = ""
        for posicao in linha:
            if posicao == "~":
                linha_texto += f"{AZUL}~{RESET} | "
            elif posicao == "X":
                linha_texto += f"{VERMELHO}X{RESET} | "
            elif posicao == "-":
                linha_texto += f"{CINZA}-{RESET} | "
            elif posicao == "N":
                linha_texto += f"{VERDE}N{RESET} | "
            else:
                linha_texto += f"{posicao} | "
        print(f"{linha_num:2}| {linha_texto}")
        linha_num += 1

# Função para entrada do usuário
def entrada_usuario():
    orientacao = ""
    tentativas_orientacao = 0
    # Aqui ele verifica se a orientação é válida, ou seja, se digitar X ele não aceita
    while orientacao not in ["H", "V"]:
        if tentativas_orientacao > 0:
            print(f"{VERMELHO}Orientação inválida{RESET}")
        orientacao = input("Digite a orientação do navio (H ou V): ").upper()
        tentativas_orientacao += 1
        
    linha = -1
    tentativas_linha = 0
    # Verifica se a linha solicitada pelo usuário é válida, ou seja, se está dentro do tamanho do tabuleiro
    while linha not in range(tamanho_tabuleiro):
        if tentativas_linha > 0:
            print(f"{VERMELHO}Número da linha inválido, digite um número entre 1 e {tamanho_tabuleiro}.{RESET}")
        entrada_linha = input(f"Digite o número da linha (1 a {tamanho_tabuleiro}): ")
        # Ele converte a entrada do usuário para inteiro e ele subtrai 1 para que a linha comece do 0
        if entrada_linha.isdigit():
            linha = int(entrada_linha) - 1
        tentativas_linha += 1

    coluna = -1
    tentativas_coluna = 0
    # Verifica se a coluna solicitada pelo usuário é válida, ou seja, se está dentro do tamanho do tabuleiro
    while coluna not in range(tamanho_tabuleiro):
        if tentativas_coluna > 0:
            print(f"{VERMELHO}Coluna inválida, digite uma letra entre A e {ultima_letra}.{RESET}")
        entrada_coluna = input(f"Digite a coluna (A a {ultima_letra}): ").upper()
        # Ele converte a entrada do usuário para inteiro e ele subtrai 1 para que a linha comece do 0
        if entrada_coluna in letras_para_numero:
            coluna = letras_para_numero[entrada_coluna]
        tentativas_coluna += 1

    return linha, coluna, orientacao

# Função para colocar navios no tabuleiro (Horizontal ou Vertical)
def colocar_navio(comprimento, linha, coluna, orientacao):
    if orientacao == "H":
        return coluna + comprimento <= tamanho_tabuleiro
    else:
        return linha + comprimento <= tamanho_tabuleiro


# Função para verificar se há sobreposição de navios
def sobreposicao(tabuleiro, linha, coluna, orientacao, comprimento):
    if orientacao == "H":
        for i in range(coluna, coluna + comprimento):
            if tabuleiro[linha][i] == "N":
                return True
    else:
        for i in range(linha, linha + comprimento):
            if tabuleiro[i][coluna] == "N":
                return True
    return False

# Função para colocar navios no tabuleiro
def colocar_navios(tabuleiro, modo_pvp=False): # False = computador
    posicao_navio = 0
    total_navios = len(tamanho_navios)

    while posicao_navio < total_navios:
        comprimento = tamanho_navios[posicao_navio]

        # Tabuleiro do computador coloca os navios automaticamente
        if tabuleiro is tabuleiro_computador and not modo_pvp:
            orientacao = random.choice(["H", "V"])
            linha = random.randint(0, tamanho_tabuleiro - 1)
            coluna = random.randint(0, tamanho_tabuleiro - 1)
            pode_colocar = (colocar_navio(comprimento, linha, coluna, orientacao) and not sobreposicao(tabuleiro, linha, coluna, orientacao, comprimento))
            # Confirmar que pode colocar o navio nesta orientação
            if pode_colocar:
                if orientacao == "H":
                    for i in range(coluna, coluna + comprimento):
                        tabuleiro[linha][i] = "N"
                else:
                    for i in range(linha, linha + comprimento):
                        tabuleiro[i][coluna] = "N"
                posicao_navio += 1
        # Tabuleiro do jogador solicita a posição do navio
        else:
            print(f"{VERDE}Coloque o navio de tamanho {comprimento}{RESET}")
            linha, coluna, orientacao = entrada_usuario()
            pode_colocar = (colocar_navio(comprimento, linha, coluna, orientacao) and not sobreposicao(tabuleiro, linha, coluna, orientacao, comprimento))
            # Confirmar que pode colocar o navio nesta orientação
            if pode_colocar:
                if orientacao == "H":
                    for i in range(coluna, coluna + comprimento):
                        tabuleiro[linha][i] = "N"
                else:
                    for i in range(linha, linha + comprimento):
                        tabuleiro[i][coluna] = "N"
                print(f"{CIANO}Tabuleiro depois de colocar o navio:{RESET}")
                print_tabuleiro(tabuleiro)
                posicao_navio += 1
            else:
                print(f"{VERMELHO}Posição inválida.{RESET}")

# Função para contar os navios afundados
def navios_afundados(tabuleiro):
    return sum(posicao == "X" for linha in tabuleiro for posicao in linha)

# Função para realizar o turno do jogador ou do computador
def turno(tabuleiro, alvo):
    if tabuleiro in [chute_jogador, chute_computador]:
        # Se for turno de jogador humano (chute_jogador), pede input
        if tabuleiro is chute_jogador:
            linha = -1
            coluna = -1
            tentativas = 0
            while ((linha not in range(tamanho_tabuleiro)) or (coluna not in range(tamanho_tabuleiro)) or (tabuleiro[linha][coluna] in ["-", "X"])) and tentativas < 100:
                if tentativas > 0 and tabuleiro[linha][coluna] in ["-", "X"]:
                    print(f"{VERMELHO}Você já tentou essa posição{RESET}")
                linha, coluna, i = entrada_usuario()
                tentativas += 1
            if alvo[linha][coluna] == "N":
                print(f"{VERDE}Acertou!{RESET}")
                tabuleiro[linha][coluna] = "X"
                alvo[linha][coluna] = "X"
            else:
                print(f"{CINZA}Errou.{RESET}")
                tabuleiro[linha][coluna] = "-"
        else:
            # Se for turno do computador (chute_computador), joga aleatório
            linha = random.randint(0, tamanho_tabuleiro - 1)
            coluna = random.randint(0, tamanho_tabuleiro - 1)
            tentativas = 0
            while tabuleiro[linha][coluna] in ["-", "X"] and tentativas < 100:
                linha = random.randint(0, tamanho_tabuleiro - 1)
                coluna = random.randint(0, tamanho_tabuleiro - 1)
                tentativas += 1
            if alvo[linha][coluna] == "N":
                tabuleiro[linha][coluna] = "X"
                alvo[linha][coluna] = "X"
                print(f"{VERMELHO}Computador acertou!{RESET}")
            else:
                tabuleiro[linha][coluna] = "-"
                print(f"{CINZA}Computador errou.{RESET}")

# Menu do Batalha Naval
def menu():
    print(f"{VERDE}Bem-vindo ao Batalha Naval!{RESET}")
    print("1. Jogar contra o computador")
    print("2. Jogar contra outro jogador")
    print("3. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        return "computador"
    elif escolha == "2":
        return "pvp"
    elif escolha == "3":
        return "sair"
    else:
        print(f"{VERMELHO}Opção inválida, tente novamente.{RESET}")
        time.sleep(2)
        return menu()

# Menu para escolher o tamanho do tabuleiro
def escolher_tamanho_tabuleiro():
    print("Escolha o tamanho do tabuleiro:")
    print("1. 10x10")
    print("2. 12x12")
    print("3. 15x15")
    escolha = input("Digite o número da opção: ")
    if escolha == "1":
        return 10
    elif escolha == "2":
        return 12
    elif escolha == "3":
        return 15
    else:
        print(f"{VERMELHO}Opção inválida, tente novamente{RESET}")
        time.sleep(2)
        return escolher_tamanho_tabuleiro()  # Chama novamente se a opção for inválida

# Execução para a escolha do tamanho do tabuleiro e configuração inicial
tamanho_tabuleiro = escolher_tamanho_tabuleiro()
letras_para_numero = escala_tabuleiro(tamanho_tabuleiro)

if tamanho_tabuleiro == 10:
    ultima_letra = "J"
elif tamanho_tabuleiro == 12:
    ultima_letra = "L"
else:
    tamanho_tabuleiro == 15
    ultima_letra = "O"

tabuleiro_jogador = [["~"] * tamanho_tabuleiro for i in range(tamanho_tabuleiro)]
tabuleiro_computador = [["~"] * tamanho_tabuleiro for i in range(tamanho_tabuleiro)]
chute_jogador = [["~"] * tamanho_tabuleiro for i in range(tamanho_tabuleiro)]
chute_computador = [["~"] * tamanho_tabuleiro for i in range(tamanho_tabuleiro)]

modo = menu()

# Modos de jogo
if modo == "computador":
    colocar_navios(tabuleiro_computador)
    print(f"{VERDE}Agora, você vai colocar seus navios:{RESET}")
    colocar_navios(tabuleiro_jogador)
    print(f"{VERDE}Seu tabuleiro final:{RESET}")
    print_tabuleiro(tabuleiro_jogador)
    while navios_afundados(chute_jogador) < 19 and navios_afundados(chute_computador) < 19:
        print(f"{CIANO}Sua vez de jogar{RESET}")
        print_tabuleiro(chute_jogador)
        turno(chute_jogador, tabuleiro_computador)
        if navios_afundados(chute_jogador) == 19:
            print(f"{VERDE}Você venceu!{RESET}")
        else:
            print(f"{CIANO}Agora é a vez do computador{RESET}")
            turno(chute_computador, tabuleiro_jogador)
            if navios_afundados(chute_computador) == 19:
                print(f"{VERMELHO}O computador ganhou.{RESET}")
elif modo == "pvp":
    print(f"{VERDE}Jogador 1, posicione seus navios:{RESET}")
    colocar_navios(tabuleiro_jogador, modo_pvp=True) # True = Jogador vs Jogador
    print("\n" * 100)
    print(f"{VERDE}Jogador 2, posicione seus navios:{RESET}")
    colocar_navios(tabuleiro_computador, modo_pvp=True) # True = Jogador vs Jogador
    print("\n" * 100)
    while navios_afundados(chute_jogador) < 19 and navios_afundados(chute_computador) < 19:
        print(f"{CIANO}Jogador 1, sua vez:{RESET}")
        print_tabuleiro(chute_jogador)
        turno(chute_jogador, tabuleiro_computador)
        if navios_afundados(chute_jogador) == 19:
            print(f"{VERDE}Jogador 1 venceu!{RESET}")
        else:
            print(f"{CIANO}Jogador 2, sua vez:{RESET}")
            print_tabuleiro(chute_computador)
            turno(chute_computador, tabuleiro_jogador)
            if navios_afundados(chute_computador) == 19:
                print(f"{VERDE}Jogador 2 venceu!{RESET}")
else:
    print(f"{VERMELHO}Saindo do jogo...{RESET}")
    print("Obrigado por jogar!")
    time.sleep(2)
    exit(0)