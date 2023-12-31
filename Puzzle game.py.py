import pygame, random

# Initialize the game
pygame.init()

# Set up the game window
WINDOW_WIDTH = 901
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Puzzle Game')

FPS = 10
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (220, 20, 60)
YELLOW = (255, 127, 0)

bg = pygame.image.load('Doreamon.jpg')
bg_rect = bg.get_rect()
bg_rect.topleft = (0, 0)

font_title = pygame.font.Font('SharpAxe.ttf', 64)
font_content = pygame.font.Font('SharpAxe.ttf', 40)

# start screen
title_text = font_title.render('Puzzle Game', True, PINK)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 80)

choose_text = font_content.render('Choose your difficulty', True, PINK)
choose_rect = choose_text.get_rect()
choose_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20)

easy_text = font_content.render("Press 'E' - Easy (3x3)", True, YELLOW)
easy_rect = easy_text.get_rect()
easy_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 40)

medium_text = font_content.render("Press 'M' - Medium (4x4)", True, YELLOW)
medium_rect = medium_text.get_rect()
medium_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 90)

hard_text = font_content.render("Press 'H' - Hard (5x5)", True, YELLOW)
hard_rect = hard_text.get_rect()
hard_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 140)

# end screen
play_again_text = font_title.render('Play Again?', True, BLACK)
play_again_rect = play_again_text.get_rect()
play_again_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font_content.render('Press Space and again run the code', True, BLACK)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)


selected_img = None
is_game_over = False
show_start_screen = True

rows = None
cols = None

cell_width = None
cell_height = None

cells = []

def start_game(mode):
    global cells, cell_width, cell_height, show_start_screen

    rows = mode
    cols = mode
    num_cells = rows * cols

    cell_width = WINDOW_WIDTH // rows
    cell_height = WINDOW_HEIGHT // cols

    cell = []
    rand_indexes = list(range(0, num_cells))

    for i in range(num_cells):
        x = (i % rows) * cell_width
        y = (i // cols) * cell_height
        rect = pygame.Rect(x, y, cell_width, cell_height)
        rand_pos = random.choice(rand_indexes)
        rand_indexes.remove(rand_pos)
        cells.append({'rect': rect, 'border': WHITE, 'order': i, 'pos':rand_pos})

    show_start_screen = False

# Game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False


            if show_start_screen:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:
                    start_game(3)
                elif keys[pygame.K_m]:
                    start_game(4)
                elif keys[pygame.K_h]:
                    start_game(5)



        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not is_game_over:
            mouse_pos = pygame.mouse.get_pos()

            for cell in cells:
                rect = cell['rect']
                order = cell['order']

                if rect.collidepoint(mouse_pos):
                    if not selected_img:
                        selected_img = cell
                        cell['border'] = RED
                    else:
                        current_img = cell
                        if current_img['order'] != selected_img['order']:
                            #swap images
                            temp = selected_img['pos']
                            cells[selected_img['order']]['pos'] = cells[current_img['order']]['pos']
                            cells[current_img['order']]['pos'] = temp

                            cells[selected_img['order']]['border'] = WHITE
                            selected_img = None

                            # check if puzzle is solved
                            is_game_over = True
                            for cell in cells:
                                if cell['order'] != cell['pos']:
                                    is_game_over = False


    if show_start_screen:
        screen.fill(BLACK)
        screen.blit(title_text, title_rect)
        screen.blit(choose_text, choose_rect)
        screen.blit(easy_text, easy_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(hard_text, hard_rect)
    else:

        screen.fill(WHITE)

        if not is_game_over:
            for i, val in enumerate(cells):
                pos = cells[i]['pos']
                img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cell_width, cell_height)
                screen.blit(bg, cells[i]['rect'], img_area)
                pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1)
        else:
            screen.blit(bg, bg_rect)
            screen.blit(play_again_text, play_again_rect)
            screen.blit(continue_text, continue_rect)

    # Render graphics here
    pygame.display.update()
    clock.tick(FPS)

# Quit the game
pygame.quit()

