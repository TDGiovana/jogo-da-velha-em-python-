👾✨


## 🎮 Jogo da Velha (Tic-Tac-Toe) Múltiplo

Bem-vindo ao **Jogo da Velha Avançado**, um projeto desenvolvido em Python para a disciplina de **Técnicas de Desenvolvimento de Algoritmo**. Este jogo CLI (Interface de Linha de Comando) combina a simplicidade do clássico Tic-Tac-Toe com uma lógica robusta e modularizada.


## ✨ Recursos Principais

Nosso jogo oferece modos de jogo e funcionalidades essenciais para uma experiência completa:

  * **Modos Flexíveis:** Escolha entre jogar contra um amigo (**PVP** 🤝) ou desafiar o **Sistema (IA)** 🤖.
  * **IA Inteligente:** A Inteligência Artificial implementa uma lógica de prioridade: ela sempre tenta **vencer** 🏆, depois tenta **bloquear** o jogador humano 🛑, e usa estratégias como ocupar o centro e os cantos.
  * **Gestão de Sessão:** Registre nomes dos jogadores e acompanhe o **Placar Persistente** 📊 em múltiplas rodadas.
  * **Distribuição Fácil:** O código foi otimizado para ser transformado em um executável (`.exe`) usando PyInstaller, facilitando o uso em qualquer máquina Windows.

-----

## 💻 Estrutura e Acadêmica (Onde o Código Brilha\!)

Este projeto atende e excede todos os requisitos de avaliação da faculdade, demonstrando o uso avançado de Python:

### 💡 Lógica e Algoritmo

O código é eficiente e fácil de seguir. A complexidade está nas funções **`verificar_vitoria`** (que checa rapidamente 8 condições) e **`jogada_da_ia`**, garantindo que o fluxo do jogo seja impecável.

### 📚 Estruturas de Dados

  * **Listas:** O **Tabuleiro** é uma **Lista de Listas** (`[[ ], [ ], [ ]]`) para representação matricial 3x3.
  * **Dicionários:** Usamos **Dicionários** para mapear Símbolos para Nomes e para manter o estado da partida (`dados_jogo`) e o placar total (`placar_geral`).

### 🔄 CRUD e Modularização

  * **CRUD:** As funções do jogo simulam um CRUD de dados: **Create** (no `inicializar_jogo`), **Read** (no `exibir_tabuleiro`), **Update** (no `fazer_jogada`), e **Delete/Reset** (no ciclo de reinício da rodada).
  * **Funções:** O código é 100% modular, com funções de responsabilidade única (ex: `limpar_tela`, `obter_nomes`, `jogar`), garantindo o máximo de **reutilização** e clareza. 🧩

-----

## ▶️ Como Rodar

Para executar o jogo:

1.  Baixe o arquivo .rar
2.  Extraia os arquivs e exeute o jogo da velha :)
3.  
