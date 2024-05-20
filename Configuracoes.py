import pygame, os

# Defenir as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Define o tamanho da tela
screen_width = 400
screen_height = 500

def config():
    pygame.init() # Inica o pygame

    # Define as características da tela
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Configurações")
    selected = None
    
    font_path = os.path.join("MedievalSharp-Regular.ttf")
    custom_font = pygame.font.Font(font_path, 32)
    
    # Carregar imagem de fundo
    background_image = pygame.image.load("fundo.png").convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    running = True
    while running:
        # Eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                selected = -1
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected = 1
                elif event.key == pygame.K_2:
                    selected = 2
                elif event.key == pygame.K_3:
                    selected = 3
                elif event.key == pygame.K_4:
                    selected = 4
                elif event.key == pygame.K_5:
                    selected = -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi dentro de uma das opções
                if player1_rect.collidepoint(event.pos):
                    selected = 1
                elif player2_rect.collidepoint(event.pos):
                    selected = 2
                elif tabuleiro_rect.collidepoint(event.pos):
                    selected = 3
                elif buracos_rect.collidepoint(event.pos):
                    selected = 4
                elif leave_rect.collidepoint(event.pos):
                    selected = -1
        
        screen.blit(background_image, (0, 0))  # Desenhar na tela a imagem de fundo
        
        text = custom_font.render("Mudar cor de:", True, BLACK)
        text_rect = text.get_rect(center=(screen_width//2, 150))
        screen.blit(text, text_rect)
        
        # Botões para os modos de jogo
        player1_button = custom_font.render("1. Player 1", True, BLACK)
        player1_rect = player1_button.get_rect(center=(screen_width//2, 200))
        screen.blit(player1_button, player1_rect)
        
        player2_button = custom_font.render("2. Player 2", True, BLACK)
        player2_rect = player2_button.get_rect(center=(screen_width//2, 250))
        screen.blit(player2_button, player2_rect)
        
        tabuleiro_button = custom_font.render("3. Tabuleiro", True, BLACK)
        tabuleiro_rect = tabuleiro_button.get_rect(center=(screen_width//2, 300))
        screen.blit(tabuleiro_button, tabuleiro_rect)
        
        buracos_button = custom_font.render("4. Buracos", True, BLACK)
        buracos_rect = tabuleiro_button.get_rect(center=(screen_width//2, 350))
        screen.blit(buracos_button, buracos_rect)
        
        leave_button = custom_font.render("5. Sair", True, BLACK)
        leave_rect = tabuleiro_button.get_rect(center=(screen_width//2, 400))
        screen.blit(leave_button, leave_rect)


        pygame.display.flip()
        
        # Se um modo foi selecionado, sair do loop
        if selected:
            break
    
    pygame.quit()
    return selected