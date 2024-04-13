# Jogo PahTum

Pathum é um dos jogos mais antigos da história da humanidade. Os tabuleiros mais antigos deste jogo foram encontrados na Antiga Mezopotâmia e na Asíria. O jogo tem um tabuleiro 7x7 com um numero impar de buracos,cinco, que são gerados aleatoriamente para cada jogo. Neste projeto também foi implementado um tabuleiro 5x5 com 3 buracos.
No PahTum cada jogador coloca a sua pedra no tabuleiro no seu devido turno. A pedra so pode ser colocada em quadrados que não contenham outra peça ou um buraco. O objetivo é criar mais linhas de pedras contíguas que o adversário. As linhas consideradas são as verticais e horizontais. Cada sequência de pedras tem a sua propria pontuação, valendo apenas pontos a partir de duas peças.

## Download do programa e sua execução
- Para que o porgrama seja executado é necessario que tenha o python instalado;caso não tenha, escreva no terminal o seguinte codigo:

		$ sudo apt install python3
- Além disso é necessario ter a biblioteca Numpy e Pygame; caso não tenhas as bibliotecas, no terminal escreva o seguinte codigo:

		$ pip install pygame
		$ pip install numpy
- Após certificar-se que tem todos os requisitos necessarios pode executar o programa através da linha de codigo:

		$ python3 main.py
  
## Caracteristicas do Projeto
Neste trabalho o objetivo é implementar um jogo de tabuleiro, com diferentes modos de jogo e a utlização de um algoritmo de IA que possa jogar contra um ser humano.
Temos três modos de jogo Humano x Humano, Humano x CPU e CPU x CPU. Temos 3 dificuldades para as CPUs sendo estas fácil, médio e dificil, cada uma com a sua propria heuristica. Todas as dificuldades utilizam o algoritmo Minimax αβ cuts.
