import copy
import numpy as np

class PahTum():

    points_stones = {3:3,4:10,5:25,6:56,7:119} # Pontos de cada seqência de pedras

    def __init__(self,board,list_holes,player,tamanho) -> None:
        self.board = copy.deepcopy(board)

        self.player = player
        self.state = -1 # -1 -- > a jogar 0 --> terminou 
        self.quant_moves = 0 # Quantos movimentos foram feitos 
        self.tamanho = tamanho

        #Listas de possiveis movimentos e quantidade de movimentos maximos
        if self.tamanho == 5:
            self.positions_5x5 = [(i, j) for i in range(5) for j in range(5) if (i,j) not in list_holes]
            self.max_moves = 22
        else:
            self.positions_5x5 = [(i, j) for i in range(1,6) for j in range(1,6) if (i,j) not in list_holes]
            self.positions_7x7 = [(i, j) for i in range(7) for j in range(7) if (i,j) not in list_holes]
            self.max_moves = 44

        self.last_row = -1
        self.last_col = -1
        self.penult_last_row = -1
        self.penult_last_col = -1

    def move(self,row,col):
        '''Coloca a peça no tabuleiro para depois o estado ser adicionado à lista find_children'''
        state_copy = copy.deepcopy(self)

        state_copy.board[row][col] = self.player #Joga a peça
        
        state_copy.remove_possible_position(row,col) # Remove das posições jogaveis

        state_copy.quant_moves += 1 #  Adiciona um nos movimentos

        state_copy.player = 3 - self.player # Muda o jogador
        
        state_copy.update_lastmoves(row,col) # Atualiza as ultimas posições

        if state_copy.quant_moves == self.max_moves: state_copy.state = 0 # Verifica se é estado final

        return state_copy

    def count_sequence(self,line, player):
        '''Cantas sequências de pedra existem'''
        indices = np.where(line == player)[0] # Posição das pessas do player
        sequencias = []
        sequencia_atual = []
        for indice in indices:
            if not sequencia_atual or sequencia_atual[-1] == indice - 1: # Verifica se a seq atual está vazia ou o indice atual é o esperado 
                sequencia_atual.append(indice)
            else:
                if len(sequencia_atual) > 2:# So é verifica se a sequência for maoir que dois
                    sequencias.append(len(sequencia_atual))# Adiciona o tamanho da sequencia à lista
                sequencia_atual = [indice]
        if len(sequencia_atual) > 2: 
            sequencias.append(len(sequencia_atual))
        return sequencias

    @staticmethod
    def add_seq(seq_stones,seq):
        '''Adiciona ao dicionario do respetivo jogador a quantidade de sequencias'''
        for quant in seq:
            seq_stones[quant] += 1

    def seq_stones(self):
        '''A função é utilizada para calcular a quantidade sequencia de pedras para cada jogador'''
        seq_stones_player1 = {3:0,4:0,5:0,6:0,7:0}
        seq_stones_player2 = {3:0,4:0,5:0,6:0,7:0}
        # Keys -- > quantas pedras seguidas
        # Values -- > quantas vezes ocorreu

        board = self.board
        board_T = np.transpose(self.board) # Transposta da matriz

        for row in range(len(board)):
            sequence = self.count_sequence(board[row],1) # sequencia na linha 
            sequence_T = self.count_sequence(board_T[row],1) # sequencia na coluna
            self.add_seq(seq_stones_player1,sequence) # Adiciona a qauntidade de sequencias na linha para o player1
            self.add_seq(seq_stones_player1,sequence_T) # Adiciona a qauntidade de sequencias na coluna para o player1
            
            sequence = self.count_sequence(board[row],2) # sequencia na linha 
            sequence_T = self.count_sequence(board_T[row],2) # sequencia na coluna
            self.add_seq(seq_stones_player2,sequence) # Adiciona a qauntidade de sequencias na linha para o player2
            self.add_seq(seq_stones_player2,sequence_T) # Adiciona a qauntidade de sequencias na coluna para o player2
            
        return seq_stones_player1,seq_stones_player2

    def calc_score(self,weight = {}):
        '''Calcula a pontuação dos jogadores'''
        score_player1,score_player2 = 0,0
        seq_stones_player1,seq_stones_player2 = self.seq_stones()
        for seq,quant in seq_stones_player1.items():
            score_player1 += quant * self.points_stones[seq] * (weight[seq] if seq in weight.keys() else 1)
        for seq,qaunt in seq_stones_player2.items():
            score_player2 += qaunt * self.points_stones[seq] * (weight[seq] if seq in weight.keys() else 1)
        return score_player1,score_player2
    
    def play_board(self,row,col):
        self.board[row][col] = self.player

    def change_player(self):
        self.player = 3 - self.player
    
    def update_lastmoves(self,row,col):
        if self.last_row == -1:        
            self.last_row = row
            self.last_col = col
        else: 
            self.penult_last_row = self.last_row
            self.penult_last_col = self.last_col
            self.last_row = row
            self.last_col = col

    def remove_possible_position(self,row,col):
        if self.tamanho == 5:
            self.positions_5x5.remove((row,col))
        else:
            if (row,col) in self.positions_5x5: self.positions_5x5.remove((row,col))
            self.positions_7x7.remove((row,col))

        
def heuristic_easy(state): 
    score_player1,score_player2 = state.calc_score()
    if state.player == 2:
        return score_player2 - score_player1
    return score_player1 - score_player2
def heuristic_normal(state):
    weight = {3:3,4:6,5:9,6:15,7:20}
    score_player1,score_player2 = state.calc_score(weight)
    if state.player == 2:
        return score_player2 - score_player1
    return score_player1 - score_player2
def heurisic_hard(state):
    weight = {3:5,4:15,5:35,6:60,7:100}
    score_player1,score_player2 = state.calc_score(weight)
    if state.player == 2:
        return score_player2 - score_player1
    return score_player1 - score_player2