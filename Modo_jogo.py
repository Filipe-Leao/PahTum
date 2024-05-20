import pygame
import os

# Defenir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Defenir tamanho da tela
screen_width = 400
screen_height = 500 

def main_modo():

    pygame.init() # Incia o pygame

    # Define as caracteristicas da tela
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Modos de Jogo")

    selected_mode = None
    
    background_image = pygame.image.load("fundo.png").convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    font_path = os.path.join("MedievalSharp-Regular.ttf") 
    custom_font = pygame.font.Font(font_path, 32)
    running = True
    
    while running:
        # Eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                selected_mode = -1
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_mode = 1
                elif event.key == pygame.K_2:
                    selected_mode = 2
                elif event.key == pygame.K_3:
                    selected_mode = 3
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi dentro de uma das opções
                if human_human_rect.collidepoint(event.pos):
                    selected_mode = 1
                elif human_cpu_rect.collidepoint(event.pos):
                    selected_mode = 2
                elif cpu_cpu_rect.collidepoint(event.pos):
                    selected_mode = 3                    
        
        screen.blit(background_image, (0, 0))  # Desenha na tela a imagem de fundo
        
        text = custom_font.render("Modo de Jogo", True, BLACK)
        text_rect = text.get_rect(center=(screen_width//2, 150))
        screen.blit(text, text_rect)
        
        # Botões para os modos de jogo
        human_human_button = custom_font.render("1. Humano vs Humano", True, BLACK)
        human_human_rect = human_human_button.get_rect(center=(screen_width//2, 225))
        screen.blit(human_human_button, human_human_rect)
        
        human_cpu_button = custom_font.render("2. Humano vs CPU", True, BLACK)
        human_cpu_rect = human_cpu_button.get_rect(center=(screen_width//2, 275))
        screen.blit(human_cpu_button, human_cpu_rect)
        
        cpu_cpu_button = custom_font.render("3. CPU vs CPU", True, BLACK)
        cpu_cpu_rect = cpu_cpu_button.get_rect(center=(screen_width//2, 325))
        screen.blit(cpu_cpu_button, cpu_cpu_rect)
        
        pygame.display.flip()
        
        # Se um modo foi selecionado, sair do loop
        if selected_mode:
            break
        
    pygame.quit()
    return selected_mode