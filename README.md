🚢 Batalha Naval em Python

Este repositório contém um projeto de **Batalha Naval** desenvolvido em Python. É um jogo clássico de estratégia onde dois jogadores (ou um jogador contra o computador) posicionam navios em um tabuleiro e tentam afundar os navios do oponente.

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
