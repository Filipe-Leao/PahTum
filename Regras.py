import pygame
import os

# Define as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Define o tamanho da tela
screen_width = 400
screen_height = 500 

def rules():
    running = True
    pygame.init() # Inica o pygame

    # Define as caracteristicas da tela
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Regras")
    
    background_image = pygame.image.load("fundo.png").convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    font_path = os.path.join("MedievalSharp-Regular.ttf") 
    custom_font = pygame.font.Font(font_path, 32)
    regras_font = pygame.font.Font(font_path, 25)

    while running:
        # Eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi dentro de uma das opções
                if leave_rect.collidepoint(event.pos):
                    running = False
        
        screen.blit(background_image, (0, 0))  # Desenhar na tela a imagem de fundo
        
        rules_button = custom_font.render("Regras", True, BLACK)
        rules_rect = rules_button.get_rect(center=(screen_width//2, 130))
        screen.blit(rules_button, rules_rect)
        
        texto1_button = regras_font.render("O objetivo do jogo é", True, BLACK)
        texto1_rect = texto1_button.get_rect(center=(screen_width//2, 170))
        screen.blit(texto1_button, texto1_rect)

        texto2_button = regras_font.render("fazer linhas de 3 pedras", True, BLACK)
        texto2_rect = texto2_button.get_rect(center=(screen_width//2, 195))
        screen.blit(texto2_button, texto2_rect)
        
        texto3_button = regras_font.render("ou mais da mesma cor", True, BLACK)
        texto3_rect = texto3_button.get_rect(center=(screen_width//2, 220))
        screen.blit(texto3_button, texto3_rect)

        texto4_button = regras_font.render("3 pedras = 3 pontos", True, BLACK)
        texto4_rect = texto4_button.get_rect(center=(screen_width//2, 250))
        screen.blit(texto4_button, texto4_rect)
         
        texto5_button = regras_font.render("4 pedras = 10 pontos", True, BLACK)
        texto5_rect = texto5_button.get_rect(center=(screen_width//2, 275))
        screen.blit(texto5_button, texto5_rect)             

        texto6_button = regras_font.render("5 pedras = 25 pontos", True, BLACK)
        texto6_rect = texto6_button.get_rect(center=(screen_width//2, 300))
        screen.blit(texto6_button, texto6_rect) 
        
        texto6_button = regras_font.render("6 pedras = 56 pontos", True, BLACK)
        texto6_rect = texto6_button.get_rect(center=(screen_width//2, 325))
        screen.blit(texto6_button, texto6_rect) 
        
        texto6_button = regras_font.render("7 pedras = 119 pontos", True, BLACK)
        texto6_rect = texto6_button.get_rect(center=(screen_width//2, 350))
        screen.blit(texto6_button, texto6_rect) 

        leave_button = custom_font.render("1. Sair", True, BLACK)
        leave_rect = rules_button.get_rect(center=(screen_width//2, 400))
        screen.blit(leave_button, leave_rect)
        
        pygame.display.flip()
        
    pygame.quit()