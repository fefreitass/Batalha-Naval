🚢 Batalha Naval / Battleship in Python

Este repositório contém um projeto de **Batalha Naval** desenvolvido em Python.  
This repository contains a **Battleship** project developed in Python.

É um jogo clássico de estratégia onde dois jogadores (ou um contra o computador) posicionam navios em um tabuleiro e tentam afundar os navios inimigos.  
It’s a classic strategy game where two players (or one against the computer) place ships on a board and attempt to sink the opponent’s fleet.

---

🎮 Funcionalidades / Features

- ✅ Jogo contra outro jogador (PvP)  
  ✅ Player vs Player (PvP) mode

- ✅ Jogo contra o computador (PvC)  
  ✅ Player vs Computer (PvC) mode

- ✅ Três tamanhos de tabuleiro: 10x10, 12x12 ou 15x15  
  ✅ Three board sizes: 10x10, 12x12, or 15x15

- ✅ Validação de entrada do jogador (linha, coluna e orientação)  
  ✅ Player input validation (row, column, and orientation)

- ✅ Cores no terminal para facilitar a visualização:  
  ✅ Terminal color support for better visualization:
  - 🌊 Água: Azul / Water: Blue  
  - ❌ Erro: Cinza / Miss: Gray  
  - 💥 Acerto: Vermelho / Hit: Red  
  - 🚢 Navios: Verde / Ships: Green

- ✅ Colocação automática dos navios do computador  
  ✅ Automatic ship placement for the computer

- ✅ Placar baseado na quantidade de navios destruídos  
  ✅ Scoreboard based on the number of ships destroyed

- ✅ Interface de texto com menus interativos  
  ✅ Text-based interface with interactive menus

---

🧱 Estrutura do Código / Code Structure

- `escala_tabuleiro()`: Define o mapeamento de letras para colunas com base no tamanho do tabuleiro.  
  Maps letters to columns based on the board size.

- `print_tabuleiro()`: Imprime o tabuleiro com cores e marcações.  
  Prints the board with colors and markings.

- `entrada_usuario()`: Coleta e valida as entradas do jogador.  
  Collects and validates player input.

- `colocar_navio()` / `sobreposicao()`: Garante que os navios não ultrapassem os limites nem se sobreponham.  
  Ensures ships don’t overlap or go out of bounds.

- `colocar_navios()`: Posiciona todos os navios do jogador ou do computador.  
  Places all ships for the player or the computer.

- `turno()`: Realiza o ataque de um jogador (ou do computador).  
  Handles a player's (or computer’s) attack turn.

- `menu()`: Menu principal do jogo.  
  Main game menu.

- `escolher_tamanho_tabuleiro()`: Define o tamanho da partida.  
  Sets the board size for the match.

- `navios_afundados()`: Conta os navios atingidos.  
  Counts the number of sunk ships.
