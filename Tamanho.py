import pygame
import os

# Define as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Define o tamanho da tela
screen_width = 400
screen_height = 500 

def main_tamanho():
    pygame.init() #Inica o pygame

    # Define as caracteristicas da tela
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tamanho do tabuleiro")

    selected_size = None

    background_image = pygame.image.load("fundo.png").convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    font_path = os.path.join("MedievalSharp-Regular.ttf") 
    custom_font = pygame.font.Font(font_path, 32)

    while True:
        # Eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return -1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_size = 7
                elif event.key == pygame.K_2:
                    selected_size = 5
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi dentro de uma das opções
                if seven_button_rect.collidepoint(event.pos):
                    selected_size = 7
                elif five_button_rect.collidepoint(event.pos):
                    selected_size = 5
        
        screen.blit(background_image, (0, 0))  # Desenha na tela a imagem de fundo
        
        text = custom_font.render("Tamanho do tabuleiro", True, BLACK)
        text_rect = text.get_rect(center=(screen_width//2 - 10, 170))
        screen.blit(text, text_rect)
        
        # Botões para os modos de jogo
        seven_button = custom_font.render("1. 7x7", True, BLACK)
        seven_button_rect = seven_button.get_rect(center=(screen_width//2, 250))
        screen.blit(seven_button, seven_button_rect)
        
        five_button = custom_font.render("2. 5x5", True, BLACK)
        five_button_rect = five_button.get_rect(center=(screen_width//2, 300))
        screen.blit(five_button, five_button_rect)
        
        pygame.display.flip()
        
        # Se um modo foi selecionado, sair do loop
        if selected_size:
            pygame.quit()
            return selected_size