from CreateBoard import create_board
from Resultado import main_resultado
from Modo_jogo import main_modo
from Dificuldade import main_dificuldade
from ClassBoard import main_PatHum
from Tamanho import main_tamanho
from Regras import rules
from Tela_inicial import tela_inicio
from Configuracoes import config
from Configurar_cores import cores
from Alterar_txt import change_color

def main():
    modo_inicio = tela_inicio()

    if modo_inicio != 1:
        if modo_inicio == 2: # Mudar as cores
            objeto = config()
            while (objeto != -1): # Não saiu sa interface
                cor = cores()
                if cor is not None:# Não saiu da interface
                    change_color(objeto,cor)
                objeto = config()

        elif modo_inicio == 3:rules() # Ver as regras
        elif modo_inicio == -1: return # Saiu do jogo
        return main()

    tamanho = main_tamanho() # Tamnho do tabuleiro
    if tamanho == -1: return main() # Fechou a janela sem escolher o tamanho

    modo = main_modo() # Modo do jogo

    if modo == -1: return main() # Não escolheu o modo de jogo

    dificuldade1, dificuldade2 = None, None

    #Defenir difculdade
    if (modo == 2 or modo == 3) : dificuldade1 = main_dificuldade()
    if dificuldade1 == -1: return main() # Fechar a tela quando esta a escolher a dificuldade 1

    if modo == 3: dificuldade2 = main_dificuldade()
    if dificuldade2 == -1: return main()# Fechar a tela quando esta a escolher a dificuldade 2
    
    board,list_holes = create_board(tamanho) # Tabuleiro e lista de buracos
            
    score1,score2 = main_PatHum(board,tamanho,list_holes, modo, dificuldade1, dificuldade2)

    if (score1 != -1): # Se o score for -1 significa que saiu do jogo antes de o acabar
        restart = main_resultado(score1,score2)
        if restart == 1: return main()
        else: return

    return main()
if __name__ == "__main__" : main()