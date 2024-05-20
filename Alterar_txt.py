def set_color():
    '''Abre o ficheiro e define as cores dos elementos do jogo'''
    with open("cores.txt","r") as cores:
        core_rocha1 = tuple(map(int,cores.readline().split()))
        core_rocha2 = tuple(map(int,cores.readline().split()))
        core_tabuleiro = tuple(map(int,cores.readline().split()))
        core_buraco = tuple(map(int,cores.readline().split()))
    return core_rocha1,core_rocha2,core_tabuleiro,core_buraco

def change_color(objeto,core):
    '''Atualiza as cores guardadas no ficheiro'''
    with open("cores.txt","r") as cores:
        linhas = cores.readlines()
        linhas[objeto -1] = core + "\n"
    with open("cores.txt","w") as cores:
        cores.writelines(linhas)