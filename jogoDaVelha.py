import os # importa a biblioteca para interagir com o sistema operacional (usada para limpar a tela)
import random # importa a biblioteca para gerar números/escolhas aleatórias (usada pela IA)
import time # importa a biblioteca para funções de tempo (usada para o atraso da IA)

# partes que será usadas no jogo.
SIMBOLO_X = 'X'
SIMBOLO_O = 'O'
TABULEIRO_VAZIO = ' '

# dicionário persistente para o placar da sessão
placar_geral = {SIMBOLO_X: 0, SIMBOLO_O: 0, 'Empates': 0} #inicializa o placar com zero vitórias e empates

# funções setup e exibição 

def limpar_tela():
    #limpa o console usando o comando nativo do sistema operacional (otimizado para .EXE)
    os.system('cls' if os.name == 'nt' else 'clear') 

def selecionar_modo_jogo():
    #permite ao usuário escolher entre jogador vs jogador (1) ou jogador vs sistema (2).
    print("\n--- Seleção de Modo de Jogo ---")
    while True: # loop para garantir uma entrada válida
        modo = input("Escolha o modo: 1 - Jogador vs Jogador (PVP), 2 - Jogador vs Sistema (PVE): ")
        if modo in ['1', '2']: # verifica se a entrada é válida
            return modo # retorna a escolha do modo
        print("Poxa... Opção inválida. Digite 1 ou 2.") #caso dê erro 

def obter_nomes(modo_jogo):
    #pede e armazena os nomes dos jogadores, ajustando para o modo IA.
    print("\n--- Configuração de Nomes ---")
    nome_x = input(f"Digite o nome para {SIMBOLO_X} (Padrão: Jogador 1): ") or "Jogador 1"
    
    if modo_jogo == '1':
        # modo PVP
        nome_o = input(f"Digite o nome para {SIMBOLO_O} (Padrão: Jogador 2): ") or "Jogador 2"
    else:
        # modo PVE (IA)
        nome_o = "Sistema (IA)"
        print(f"O Jogador {SIMBOLO_O} será o Sistema (IA).")
        
    return {SIMBOLO_X: nome_x, SIMBOLO_O: nome_o}

def inicializar_jogo(nomes_jogadores):
    #inicializa um novo tabuleiro e os dados do jogo
    tabuleiro = [
        [TABULEIRO_VAZIO, TABULEIRO_VAZIO, TABULEIRO_VAZIO],
        [TABULEIRO_VAZIO, TABULEIRO_VAZIO, TABULEIRO_VAZIO],
        [TABULEIRO_VAZIO, TABULEIRO_VAZIO, TABULEIRO_VAZIO]
    ]

    dados_jogo = {
        'jogador_atual': SIMBOLO_X,
        'jogadas': 0,
        'fim_de_jogo': False,
        'vencedor': None,
        'simbolos': nomes_jogadores 
    }
    return tabuleiro, dados_jogo

def exibir_placar(placar_geral, nomes_jogadores):
    #exibe o placar da sessão atual
    print("\n" + "="*34)
    print("         PLACAR GERAL     ")
    print("="*34)
    nome_x = nomes_jogadores[SIMBOLO_X]
    nome_o = nomes_jogadores[SIMBOLO_O]
    
    print(f" {SIMBOLO_X} ({nome_x}): {placar_geral[SIMBOLO_X]} vitórias")
    print(f" {SIMBOLO_O} ({nome_o}): {placar_geral[SIMBOLO_O]} vitórias")
    print(f" Empates: {placar_geral['Empates']}")
    print("="*34 + "\n")


def exibir_tabuleiro(tabuleiro, nomes_jogadores):
    #desenha o tabuleiro atualizado no console.
    
    limpar_tela() 
    
    print("\n--- Jogo da Velha ---")
    exibir_placar(placar_geral, nomes_jogadores)
    
    print(f"  0   1   2")
    for i in range(3):
        linha_formatada = f"{tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]}"
        print(f"{i} {linha_formatada}")
        if i < 2:
            print("  --+---+--")
    print("-" * 34)

#FUNÇÕES DE LÓGICA E IA 

def verificar_vitoria(tabuleiro, simbolo):
    #verifica as 8 combinações de vitória.
    for i in range(3):
        #linhas e colunas
        if all(tabuleiro[i][j] == simbolo for j in range(3)): return True
        if all(tabuleiro[j][i] == simbolo for j in range(3)): return True

    #diagonais
    if all(tabuleiro[i][i] == simbolo for i in range(3)): return True
    if all(tabuleiro[i][2 - i] == simbolo for i in range(3)): return True

    return False

def obter_posicoes_vazias(tabuleiro):
    #retorna uma lista de tuplas (linha, coluna) das posições vazias.
    posicoes = []
    for r in range(3):
        for c in range(3):
            if tabuleiro[r][c] == TABULEIRO_VAZIO:
                posicoes.append((r, c))
    return posicoes

def jogada_da_ia(tabuleiro, simbolo_ia, simbolo_humano):
    #lógica da IA: Prioriza vencer, bloquear, centro, e depois cantos/lados.
    
    #1.checar vitória ou bloqueio
    for simbolo_atual in [simbolo_ia, simbolo_humano]:
        for r, c in obter_posicoes_vazias(tabuleiro):
            #tenta fazer a jogada temporariamente
            tabuleiro[r][c] = simbolo_atual
            
            if verificar_vitoria(tabuleiro, simbolo_atual):
                tabuleiro[r][c] = TABULEIRO_VAZIO #desfaz a jogada
                return r, c #éa jogada de vitória OU a jogada de bloqueio
                
            tabuleiro[r][c] = TABULEIRO_VAZIO #desfaz a jogada

    #2.estratégia de jogo
    posicoes_vazias = obter_posicoes_vazias(tabuleiro)

    #2a.centro (1, 1)
    if (1, 1) in posicoes_vazias:
        return 1, 1

    #2b. cantos
    cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
    posicoes_cantos_vazias = [p for p in cantos if p in posicoes_vazias]
    if posicoes_cantos_vazias:
        return random.choice(posicoes_cantos_vazias)

    # 2c.aleatório (qualquer posição restante - laterais)
    if posicoes_vazias:
        return random.choice(posicoes_vazias)

    #fallback (não deve ocorrer)
    return -1, -1

def fazer_jogada(tabuleiro, dados_jogo, linha, coluna):
    #executa a jogada e atualiza o estado.
    simbolo = dados_jogo['jogador_atual']
    
    if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == TABULEIRO_VAZIO:
        tabuleiro[linha][coluna] = simbolo
        dados_jogo['jogadas'] += 1
        
        #checagem de fim de jogo
        if verificar_vitoria(tabuleiro, simbolo):
            dados_jogo['vencedor'] = simbolo
            dados_jogo['fim_de_jogo'] = True
        elif dados_jogo['jogadas'] == 9:
            dados_jogo['fim_de_jogo'] = True
        else:
            dados_jogo['jogador_atual'] = SIMBOLO_O if simbolo == SIMBOLO_X else SIMBOLO_X
        
        return True
    else:
        return False

def obter_jogada_do_usuario(dados_jogo):
    #solicita e valida a entrada do usuário
    simbolo = dados_jogo['jogador_atual']
    nome = dados_jogo['simbolos'][simbolo]
    while True:
        try:
            jogada_str = input(f"Vez de {simbolo} ({nome}). Digite linha,coluna (ex: 0,1): ")
            linha, coluna = map(int, jogada_str.split(','))
            
            if 0 <= linha <= 2 and 0 <= coluna <= 2:
                return linha, coluna
            else:
                print("OOps... Coordenadas fora do intervalo (0 a 2). Tente novamente.")
        except ValueError:
            print("OOps... Entrada inválida. Use o formato 'linha,coluna', separados por vírgula.")

def jogar(nomes_jogadores, modo_jogo):
    #gerencia uma única rodada do jogo, com suporte à IA
    global placar_geral
    
    tabuleiro, dados_jogo = inicializar_jogo(nomes_jogadores)

    while not dados_jogo['fim_de_jogo']:
        
        exibir_tabuleiro(tabuleiro, nomes_jogadores)
        
        simbolo_atual = dados_jogo['jogador_atual']
        
        if modo_jogo == '2' and simbolo_atual == SIMBOLO_O:
            # JOGADA DA IA (SIMBOLO_O)
            print(f"Vez de {simbolo_atual} ({nomes_jogadores[simbolo_atual]}). A IA está pensando...")
            time.sleep(1) #simula atraso
            
            linha, coluna = jogada_da_ia(tabuleiro, SIMBOLO_O, SIMBOLO_X)
            fazer_jogada(tabuleiro, dados_jogo, linha, coluna)
            
        else:
            # JOGADA DO USUÁRIO (PVP ou Humano no PVE)
            linha, coluna = obter_jogada_do_usuario(dados_jogo)
            
            if not fazer_jogada(tabuleiro, dados_jogo, linha, coluna):
                print("OOps... Posição já ocupada ou inválida. Tente novamente.")
                continue # volta ao início do loop para repetir a jogada

            
    #fim do jogo: atualizar placar
    exibir_tabuleiro(tabuleiro, nomes_jogadores)
    
    if dados_jogo['vencedor']:
        vencedor_simbolo = dados_jogo['vencedor']
        vencedor_nome = dados_jogo['simbolos'][vencedor_simbolo]
        placar_geral[vencedor_simbolo] += 1
        print(f"PARABÉNS! O VENCEDOR É: {vencedor_simbolo} ({vencedor_nome})!")
    else:
        placar_geral['Empates'] += 1
        print("O JOGO TERMINOU EMPATADO!")
        
    print("\nRodada finalizada.")


def main_session():
    #loop principal para múltiplas rodadas e gestão de modos/nomes/placar.
    modo_jogo = selecionar_modo_jogo()
    nomes_jogadores = obter_nomes(modo_jogo)
    
    while True:
        jogar(nomes_jogadores, modo_jogo) #passa o modo de jogo
        
        #pergunta se quer jogar novamente
        jogar_novamente = input("\nDeseja jogar novamente para atualizar o placar? (s/n): ").lower()
        if jogar_novamente != 's':
            print("\nObrigado por jogar! Placar final:")
            exibir_placar(placar_geral, nomes_jogadores)
            break

#execução do jogo
if __name__ == "__main__":
    main_session()