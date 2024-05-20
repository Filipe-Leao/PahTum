import pygame, os

def main_resultado(player1_score, player2_score):

    pygame.init() #Inica o pygame

    # Define as caracteristicas da tela
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 500
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Score")

    font_path = os.path.join("MedievalSharp-Regular.ttf") 
    custom_font = pygame.font.Font(font_path, 36)
    
    background_image = pygame.image.load("fundo.png").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    selected_mode = None

    # Define as cores
    BLACK = (0, 0, 0)
    BROWN = (125, 75, 0)

    def display_scores():
        score_text = custom_font.render("Player 1: {}".format(player1_score), True, BLACK)
        score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH//2,150))
        screen.blit(score_text,score_text_rect)
        
        human_human_button = custom_font.render("Player 2: {} ".format(player2_score), True, BLACK)
        human_human_rect = human_human_button.get_rect(center=(SCREEN_WIDTH // 2, 250))
        screen.blit(human_human_button, human_human_rect)

    running = True
    while running:
        screen.fill(BROWN)
        # Eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_mode = 1
                elif event.key == pygame.K_2:
                    selected_mode = 2
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi dentro de uma das opções
                if leave_rect.collidepoint(event.pos):
                    selected_mode = 2
                elif restart_rect.collidepoint(event.pos):
                    selected_mode = 1
          
        screen.blit(background_image, (0, 0))  # Desenhar na tela imagem de fundo
        
        display_scores() # Display scores

        leave_button = custom_font.render("2. Sair", True, BLACK)
        leave_rect = leave_button.get_rect(center=(SCREEN_WIDTH//2, 375))
        screen.blit(leave_button, leave_rect)

        restart_button = custom_font.render("1. Reiniciar", True, BLACK)
        restart_rect = restart_button.get_rect(center=(SCREEN_WIDTH//2, 325))
        screen.blit(restart_button, restart_rect)        

        pygame.display.flip()

        pygame.time.Clock().tick(30)
        if selected_mode: break

    pygame.quit()
    return selected_mode