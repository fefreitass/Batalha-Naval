PT/BR

🚢 Batalha Naval em Python

Este repositório contém um projeto de **Batalha Naval** desenvolvido em Python.  
É um jogo clássico de estratégia onde dois jogadores (ou um contra o computador) posicionam navios em um tabuleiro e tentam afundar os navios inimigos.

---

🎮 Funcionalidades

- ✅ Jogo contra outro jogador (PvP)  
- ✅ Jogo contra o computador (PvC)  
- ✅ Três tamanhos de tabuleiro: 10x10, 12x12 ou 15x15  
- ✅ Validação de entrada do jogador (linha, coluna e orientação)  
- ✅ Cores no terminal para facilitar a visualização:  
  - 🌊 Água: Azul  
  - ❌ Erro: Cinza  
  - 💥 Acerto: Vermelho  
  - 🚢 Navios: Verde  
- ✅ Colocação automática dos navios do computador  
- ✅ Placar baseado na quantidade de navios destruídos  
- ✅ Interface de texto com menus interativos  

---

🧱 Estrutura do Código

- `escala_tabuleiro()`: Define o mapeamento de letras para colunas com base no tamanho do tabuleiro.  
- `print_tabuleiro()`: Imprime o tabuleiro com as cores e marcações necessárias.  
- `entrada_usuario()`: Coleta e valida as entradas do jogador.  
- `colocar_navio()` / `sobreposicao()`: Garante que os navios não ultrapassem os limites nem se sobreponham.  
- `colocar_navios()`: Posiciona todos os navios do jogador ou do computador.  
- `turno()`: Realiza o ataque de um jogador (ou do computador).  
- `menu()`: Menu principal do jogo.  
- `escolher_tamanho_tabuleiro()`: Define o tamanho da partida.  
- `navios_afundados()`: Conta os navios atingidos.  

---

ENG

🚢 Battleship in Python

This repository contains a **Battleship** game project developed in Python.  
It is a classic strategy game where two players (or one against the computer) place ships on a grid and try to sink the opponent's fleet.

---

🎮 Features

- ✅ Player vs Player (PvP) mode  
- ✅ Player vs Computer (PvC) mode  
- ✅ Three board sizes: 10x10, 12x12, or 15x15  
- ✅ Input validation for row, column, and orientation  
- ✅ Terminal color support for easy visualization:  
  - 🌊 Water: Blue  
  - ❌ Miss: Gray  
  - 💥 Hit: Red  
  - 🚢 Ships: Green  
- ✅ Automatic ship placement for the computer  
- ✅ Scoreboard based on the number of ships destroyed  
- ✅ Text-based interface with interactive menus  

---

🧱 Code Structure

- `escala_tabuleiro()`: Maps letters to columns based on board size.  
- `print_tabuleiro()`: Prints the board with colors and markers.  
- `entrada_usuario()`: Collects and validates player input.  
- `colocar_navio()` / `sobreposicao()`: Ensures ships stay within bounds and don't overlap.  
- `colocar_navios()`: Places all ships for the player or the computer.  
- `turno()`: Handles a player or computer's attack turn.  
- `menu()`: Displays the main game menu.  
- `escolher_tamanho_tabuleiro()`: Sets the board size.  
- `navios_afundados()`: Counts how many ships have been sunk.  
