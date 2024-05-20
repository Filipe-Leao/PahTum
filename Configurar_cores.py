import pygame, os

# Defenir cores
WHITE =  "255 255 255"
BLACK = "0 0 0"
GRAY =  "150 150 150"
YELLLOW =  "238 173 45"
GREEN =  "0 128 0"
BLUE = "135 206 250"
BROWN = "150 125 50"
RED = "255 127 127"

# Defenir o tamanho da tela
screen_width = 400
screen_height = 500

black = (0,0,0)

def cores():

    pygame.init() #Inica o pygame

    # Define as caracteristicas da tela
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Configurações")
    selected = None
    
    font_path = os.path.join("MedievalSharp-Regular.ttf")
    custom_font = pygame.font.Font(font_path, 32)
    text_font = pygame.font.Font(font_path, 28)
    
    # Carregar imagem de fundo
    background_image = pygame.image.load("fundo.png").convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    running = True

    while running:
        # Eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                selected = None
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected = WHITE
                elif event.key == pygame.K_2:
                    selected = BLACK
                elif event.key == pygame.K_3:
                    selected = RED
                elif event.key == pygame.K_4:
                    selected = BLUE
                elif event.key == pygame.K_5:
                    selected = YELLLOW
                elif event.key == pygame.K_6:
                    selected = BROWN
                elif event.key == pygame.K_7:
                    selected = GRAY
                elif event.key == pygame.K_8:
                    selected = GREEN
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi dentro de uma das opções
                if white_rect.collidepoint(event.pos):
                    selected = WHITE
                elif black_rect.collidepoint(event.pos):
                    selected = BLACK
                elif red_rect.collidepoint(event.pos):
                    selected = RED
                elif blue_rect.collidepoint(event.pos):
                    selected = BLUE
                elif yellow_rect.collidepoint(event.pos):
                    selected = YELLLOW
                elif brown_rect.collidepoint(event.pos):
                    selected = BROWN
                elif gray_rect.collidepoint(event.pos):
                    selected = GRAY
                elif green_rect.collidepoint(event.pos):
                    selected = GREEN

        screen.blit(background_image, (0, 0))  # Desenhar na tela a imagem de fundo
        
        text = custom_font.render("Cores:", True, black)
        text_rect = text.get_rect(center=(screen_width//2, 150))
        screen.blit(text, text_rect)
        
        # Botões para os modos de jogo
        white_button = text_font.render("1. Branco", True, black)
        white_rect = white_button.get_rect(center=(screen_width//2, 200))
        screen.blit(white_button, white_rect)
        
        black_button = text_font.render("2. Preto", True, black)
        black_rect = black_button.get_rect(center=(screen_width//2, 230))
        screen.blit(black_button, black_rect)
        
        red_button = text_font.render("3. Vermelho", True, black)
        red_rect = red_button.get_rect(center=(screen_width//2, 260))
        screen.blit(red_button, red_rect)
        
        blue_button = text_font.render("4. Azul", True, black)
        blue_rect = blue_button.get_rect(center=(screen_width//2, 290))
        screen.blit(blue_button, blue_rect)
        
        yellow_button = text_font.render("5. Amarelo", True, black)
        yellow_rect = yellow_button.get_rect(center=(screen_width//2, 320))
        screen.blit(yellow_button, yellow_rect)
        
        brown_button = text_font.render("6. Castanho", True, black)
        brown_rect = brown_button.get_rect(center=(screen_width//2, 350))
        screen.blit(brown_button, brown_rect)
        
        gray_button = text_font.render("7. Cinzento", True, black)
        gray_rect = gray_button.get_rect(center=(screen_width//2, 380))
        screen.blit(gray_button, gray_rect)
        
        green_button = text_font.render("8.Verde", True, black)
        green_rect = green_button.get_rect(center=(screen_width//2, 410))
        screen.blit(green_button, green_rect)
        
        pygame.display.flip()
        
        # Se um modo foi selecionado, sair do loop
        if selected:
            break
    
    pygame.quit()
    return selected