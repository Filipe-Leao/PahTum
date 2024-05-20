import numpy as np
import random

# 0 --> vazio
# 1 --> pedra preta
# 2 --> pedra branca
# -1 --> buraco

def black_holes(tamanho):
    '''Gera aleatoriamente onde os buracos do tabuleiro'''
    list_holes = []
    quant_wholes = tamanho - 2
    while quant_wholes != 0:
        row = random.randint(0,tamanho - 1)
        col = random.randint(0,tamanho - 1)
        if (row,col) not in list_holes:
            list_holes.append((row,col))
            quant_wholes -= 1
    return list_holes

def put_wholes(board,black_wholes):
    '''Coloca os buracos nos seus resptivos lugares'''
    for (row,col) in black_wholes:
        board[row][col] = -1
    return board 

def create_board(tamanho):
    if tamanho == 5: NUM_ROWS = NUM_COLS = 5
    else : NUM_ROWS = NUM_COLS = 7
    
    board = np.zeros((NUM_ROWS,NUM_COLS)) # Cria o tabuleiro, com todas as posições a zero
    list_holes = black_holes(tamanho)  # Posições dos buracos
    board = put_wholes(board,list_holes) # Coloca os buracos no tabuleiro
    
    return board,list_holes