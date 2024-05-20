import copy
from Melhor_movimento import add_probability

def possible_moves(state):
    '''Determina quais são os movimentos possiveis para jogar, conforme o tamanho do tabuleiro'''
    moves = []
    if state.tamanho == 5:
        moves = copy.deepcopy(state.positions_5x5)
    else:
        if state.quant_moves <= 20: moves = copy.deepcopy(state.positions_5x5)
        else: moves = copy.deepcopy(state.positions_7x7)
    return moves

def find_children(state,heuristic):
    '''Encontra os nos filhos do estado atual'''
    possible_states = []

    moves = possible_moves(state)

    moves = add_probability(state,moves,heuristic.__name__) # Adiciona os melhores movimentos no incio da lista 

    for move in moves:
        child_node = state.move(move[0],move[1]) # Executa o movimento
        possible_states.append(child_node) 

    return possible_states

def minimax_alphabeta(state,depth,alpha,beta,maxPlayer,heuristic):
    '''Executa o algoritmo minimax alphabeta cuts'''
    if depth == 0 or  state.state == 0: 
        return heuristic(state) 
    
    if maxPlayer:
        maxEval = float("-inf")
        children = find_children(state,heuristic)
        for child in children:
            evaluate = minimax_alphabeta(child,depth -1,alpha,beta,False,heuristic)
            maxEval = max(maxEval,evaluate)
            alpha = max(alpha,evaluate)
            if beta <= alpha:
                break
        return maxEval
    
    else:
        minEval = float("inf")
        children = find_children(state,heuristic)
        for child in children:
            evaluate = minimax_alphabeta(child,depth -1,alpha,beta,True,heuristic)
            minEval = min(minEval,evaluate)
            beta = min(beta,evaluate)
            if beta <= alpha:
                break
        return  minEval
    
def excute_minimax(game_state,depth,heuristic):
    best_score = float("-inf")
    best_move = (0,0)

    moves = possible_moves(game_state)
 
    moves = add_probability(game_state,moves,heuristic.__name__)# Adiciona os melhores movimentos no incio da lista

    for move in moves:
        score = minimax_alphabeta(game_state.move(move[0],move[1]),depth-1,best_score,float("inf"),False,heuristic)
        if score > best_score:
            best_score = score
            best_move = move

    return best_move