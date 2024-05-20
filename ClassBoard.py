import pygame, time
from ClassPuhTum import PahTum
from Algoritmo_minimax import excute_minimax
from Alterar_txt import set_color

class PatHum_board():
    def __init__(self,width,height,game_state,modo_jogo,dificuldade1,dificuldade2) -> None:

        #Caracteristicas da tela
        self.WIDTH = width
        self.HEIGHT = height
        self.CELL_SIZE = 100
        self.BORDER = 5

        #Defenir cores
        self.rocha1,self.rocha2,self.color_board,self.holes = set_color()
        self.BLACK = (0, 0, 0)
        
        # Estado do tabuleiro
        self.game_state = game_state

        #Caracteristicas do jogo
        self.dificuldade1 = dificuldade1
        self.dificuldade2 = dificuldade2
        self.modo_jogo = modo_jogo

        if self.modo_jogo == 1: # Humano x Humano
            self.player1_func = self.player2_func = self.mouse_click
        elif self.modo_jogo == 2: # Humano x CPU
            self.player1_func = self.mouse_click
            self.player2_func = self.click_minimax
            self.depth1 = self.define_depth(dificuldade1)
        else: # CPU x CPU
            self.player1_func = self.player2_func = self.click_minimax
            self.depth1 = self.define_depth(dificuldade1)
            self.depth2 = self.define_depth(dificuldade2)


    def define_depth(self,dificuldade):
        if self.game_state.tamanho == 5:
            if dificuldade.__name__ != "heurisic_hard": return 4
            return 6
        return 4
    def drawn_board(self,screen):
        '''Desenha o tabuleiro'''
        for row in range(self.WIDTH // 100):
            for col in range(self.WIDTH // 100):
                if self.game_state.board[row][col] == 0:
                    pygame.draw.rect(screen, self.color_board, (col*self.CELL_SIZE, row*self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
                elif self.game_state.board[row][col] == 1:
                    pygame.draw.rect(screen, self.color_board, (col*self.CELL_SIZE, row*self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
                    pygame.draw.circle(screen,self.rocha1, ((col*self.CELL_SIZE)+(self.CELL_SIZE//2), (row*self.CELL_SIZE)+(self.CELL_SIZE//2)), self.CELL_SIZE // 3)
                elif self.game_state.board[row][col] == 2:
                    pygame.draw.rect(screen, self.color_board, (col*self.CELL_SIZE, row*self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
                    pygame.draw.circle(screen, self.rocha2, ((col*self.CELL_SIZE)+(self.CELL_SIZE//2), (row*self.CELL_SIZE)+(self.CELL_SIZE//2)), self.CELL_SIZE // 3)
                else:
                    pygame.draw.rect(screen, self.holes, (col*self.CELL_SIZE, row*self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
                # Desenha as bordas pretas entre os quadrados
                if row < 6:
                    pygame.draw.line(screen,self.BLACK, (col*self.CELL_SIZE, (row+1)*self.CELL_SIZE), ((col+1)*self.CELL_SIZE, (row+1)*self.CELL_SIZE), self.BORDER)
                if col < 6:
                    pygame.draw.line(screen,self.BLACK, ((col+1)*self.CELL_SIZE, row*self.CELL_SIZE), ((col+1)*self.CELL_SIZE, (row+1)*self.CELL_SIZE), self.BORDER)

    def change_states(self,row,col):
        '''Metodo para atualizar o estado do jogo em game_state'''
        self.game_state.play_board(row,col)
        self.game_state.change_player()
        self.game_state.remove_possible_position(row,col)
        self.game_state.quant_moves += 1
        self.game_state.update_lastmoves(row,col)

    def mouse_click(self):
        '''Metodo para receber o click do jogador'''
        mouse_pos = pygame.mouse.get_pos() # Posição do rato
        if pygame.mouse.get_pressed()[0] == True:
            clicked_row = mouse_pos[1] // self.CELL_SIZE 
            clicked_col = mouse_pos[0] // self.CELL_SIZE
            # O valor da linha e coluna são modificados para serem aceites como posição na matriz
            if self.game_state.board[clicked_row][clicked_col] == 0: # Verifica se a posição é jogavel 
                return (clicked_row,clicked_col)

    def click_minimax(self):
        '''Metodo para receber as cordenadas que foram jogadas pelo algoritmo'''
        try:
           depth = self.depth1 if self.game_state.player == 1 else self.depth2 
        except AttributeError: depth = self.depth1
        
        if self.modo_jogo == 2:
            row,col = excute_minimax(self.game_state,depth,self.dificuldade1)
        else:
            if self.game_state.player == 1: row,col = excute_minimax(self.game_state,depth,self.dificuldade1)
            else: row,col = excute_minimax(self.game_state,depth,self.dificuldade2)
        return (row,col)
    
    def run_gameplay(self,screen):
        self.drawn_board(screen) #Desenhe o tabuleiro atualizado
        pygame.display.flip() # Atualize a tela
        while self.game_state.state == -1: # Enquanto não é um estado final do jogo ou não fechou a tela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_state.state = 0
            if self.game_state.player == 1: move = self.player1_func()
            else: move = self.player2_func()

            if move is not None:
                self.change_states(move[0],move[1])
                self.drawn_board(screen) #Desenhe o tabuleiro atualizado
                pygame.display.flip() # Atualize a tela

            if self.game_state.quant_moves == self.game_state.max_moves: # Terminou o jogo
                time.sleep(1)
                self.game_state.state = 0

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('PahTum')

        self.run_gameplay(screen)

        pygame.quit()

def main_PatHum(board,tamanho,list_holes,modo_jogo,dificuldade1,dificuldade2):
    # Cria os objetos das classes que representam o estado do jogo  
    game_state = PahTum(board,list_holes,1,tamanho)
    Board = PatHum_board(tamanho*100,tamanho*100,game_state,modo_jogo,dificuldade1,dificuldade2)

    Board.start()

    if game_state.quant_moves < game_state.max_moves: # Retorna -1 se fechar o jogo antes de o terminar
        return -1,-1
    return game_state.calc_score()