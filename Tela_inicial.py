import pygame, os

# Define as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Define o tamanho da tela
screen_width = 400
screen_height = 500

def tela_inicio():

    pygame.init() #Inica o pygame

    # Define as caracteristicas da tela
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pahtum")
    selected = None
    
    font_path = os.path.join("MedievalSharp-Regular.ttf")
    custom_font = pygame.font.Font(font_path, 32)
    
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
                    selected = -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi dentro de uma das opções
                if inicar_rect.collidepoint(event.pos):
                    selected = 1
                elif config_rect.collidepoint(event.pos):
                    selected = 2
                elif rules_rect.collidepoint(event.pos):
                    selected = 3
                elif quit_rect.collidepoint(event.pos):
                    selected = -1

        screen.blit(background_image, (0, 0))  # Desenhar na tela a imagem de fundo
        
        text = custom_font.render("PahTum", True, BLACK)
        text_rect = text.get_rect(center=(screen_width//2, 150))
        screen.blit(text, text_rect)
        
        # Botões para os modos de jogo
        inicar_button = custom_font.render("1. Iniciar", True, BLACK)
        inicar_rect = inicar_button.get_rect(center=(screen_width//2, 225))
        screen.blit(inicar_button, inicar_rect)
        
        config_button = custom_font.render("2. Configurações", True, BLACK)
        config_rect = config_button.get_rect(center=(screen_width//2, 275))
        screen.blit(config_button, config_rect)

        rules_button = custom_font.render("3. Regras", True, BLACK)
        rules_rect = rules_button.get_rect(center=(screen_width//2, 325))
        screen.blit(rules_button, rules_rect)
        
        quit_button = custom_font.render("4. Sair", True, BLACK)
        quit_rect = quit_button.get_rect(center=(screen_width//2, 375))
        screen.blit(quit_button, quit_rect)

        pygame.display.flip()   
        
        # Se um modo foi selecionado, sair do loop
        if selected:
            break

    pygame.quit()
    return selected