import random

def verify_five(state,row,col):
    '''Função utilizada para verificar se a posição no tabuleiro 5x5 é valida'''
    if (row,col) in state.positions_5x5: # Se exitir em todas as possiblidades que ainda são validas no tabuleiro a posição pode ser utilizada
        return True
    return False
def verify_seven(state,row,col):
    '''Função utilizada para verificar se a posição no tabuleiro 7x7 é valida'''
    if (row,col) in state.positions_7x7: # Se exitir em todas as possiblidades que ainda são validas no tabuleiro a posição pode ser utilizada
        return True
    return False

def add_position_enemy(state,moves,heuristic):
    '''Esta função irá adicionar,caso seja esse o caso, as posições em torno da ultima jogda do adversario à lista dos possiveis movimentos. Se o tabuleiro
    for 5x5 como o bot esta a jogar em todo o tabuleiro, as posições em torno da utlima peça jogada(adversário)
    são colocadas primeiro, pois são posições mais importantes. Se for o tabuleiro 7x7 devido as diferentes dificuldades
    só o modo dificil e medio poderam sair da zona em que estão a jogar, pois o bot nas jogadas iniciais vê apenas o tabuleiro
    5x5 e depois de 20 jogadas passa a jogar no 7x7. A dificuldade media tem 50% de probabilidade de conseguir verificar
    estas posições já o modo dificil vê sempre estas posições.'''
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        row = state.last_row + dr
        col = state.last_col + dc

        if (state.tamanho == 5 and verify_five(state,row,col)):
            moves.remove((row,col))
            moves.insert(0,(row,col))

        elif (state.tamanho == 7 and verify_seven(state,row,col)):
            if (row,col) in moves:
                moves.remove((row,col))
                moves.insert(0,(row,col))

            elif heuristic != "heuristic_easy":  
                if heuristic == "heuristic_normal":
                    if (random.randint(1,100) % 2 == 0):
                        moves.insert(0,(row,col))
                else:
                    moves.insert(0,(row,col))
    return moves

def add_position(state,moves):
    '''A função coloca as posições em torno da ultima jogada do bot nas posições inicias da lista'''
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        row = state.penult_last_row + dr
        col = state.penult_last_col + dc

        if (state.tamanho == 5 and verify_five(state,row,col)):
            moves.remove((row,col))
            moves.insert(0,(row,col))

        elif (state.tamanho == 7 and verify_seven(state,row,col)):
            if (row,col) in moves:
                moves.remove((row,col))
                moves.insert(0,(row,col))
    return moves

def center_first(state,moves):
    '''Se nenhum dos bots jogou, a posição mais favoravel é a do centro do tabuleiro, que são colocadas no inicio da lista'''
    position = (2 if state.tamanho == 5 else 3,2 if state.tamanho == 5 else 3)
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        row = position[0] + dr
        col = position[1] + dc
        if (row,col) in moves: # Se a posição for um buraco não podemos utilizar a posição
            moves.remove((row,col))
            moves.insert(0,(row,col))
    if position in moves: # Se a posição for um buraco não podemos utilizar a posição
        moves.remove(position)
        moves.insert(0,position)
    return moves

def add_probability(state,moves,heuristic):
    if state.last_row == -1:
        moves = center_first(state,moves)
    else:
        moves = add_position_enemy(state,moves,heuristic)
    if state.penult_last_row != -1:
        moves = add_position(state,moves)
    return moves