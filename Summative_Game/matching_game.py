import pygame
import random
import time
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 700
ROWS, COLS = 4, 4
TILE_SIZE = 120
MARGIN = 20
FONT = pygame.font.SysFont(None, 60)
SMALL_FONT = pygame.font.SysFont(None, 40)

# Colors
BG_COLOR = (30, 30, 30)
TILE_COLOR = (80, 80, 200)
REVEALED_COLOR = (200, 200, 255)
TEXT_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Match - Pygame")

# Setup board
symbols = list("AABBCCDDEEFFGGHH")
random.shuffle(symbols)
grid = [symbols[i:i + COLS] for i in range(0, 16, COLS)]
revealed = [[False] * COLS for _ in range(ROWS)]
matched = [[False] * COLS for _ in range(ROWS)]

first_click = None
moves = 0
game_over = False

def draw_grid():
    screen.fill(BG_COLOR)
    for row in range(ROWS):
        for col in range(COLS):
            x = MARGIN + col * (TILE_SIZE + MARGIN)
            y = MARGIN + row * (TILE_SIZE + MARGIN) + 80
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

            if revealed[row][col] or matched[row][col]:
                pygame.draw.rect(screen, REVEALED_COLOR, rect)
                symbol = FONT.render(grid[row][col], True, TEXT_COLOR)
                screen.blit(symbol, (x + TILE_SIZE // 3, y + TILE_SIZE // 4))
            else:
                pygame.draw.rect(screen, TILE_COLOR, rect)

    # Draw move counter
    move_text = SMALL_FONT.render(f"Moves: {moves}", True, WHITE)
    screen.blit(move_text, (20, 20))

    if game_over:
        win_text = FONT.render(f"You won in {moves} moves!", True, WHITE)
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT - 60))

def get_tile(pos):
    x, y = pos
    y -= 80  # adjust for header
    for row in range(ROWS):
        for col in range(COLS):
            tx = MARGIN + col * (TILE_SIZE + MARGIN)
            ty = MARGIN + row * (TILE_SIZE + MARGIN)
            rect = pygame.Rect(tx, ty, TILE_SIZE, TILE_SIZE)
            if rect.collidepoint(x, y):
                return row, col
    return None

clock = pygame.time.Clock()
running = True

while running:
    draw_grid()
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            tile = get_tile(pos)
            if tile:
                r, c = tile
                if not revealed[r][c] and not matched[r][c]:
                    revealed[r][c] = True
                    if not first_click:
                        first_click = (r, c)
                    else:
                        second_click = (r, c)
                        moves += 1
                        draw_grid()
                        pygame.display.flip()
                        pygame.time.delay(600)

                        # Check match
                        r1, c1 = first_click
                        r2, c2 = second_click
                        if grid[r1][c1] == grid[r2][c2]:
                            matched[r1][c1] = True
                            matched[r2][c2] = True
                        else:
                            revealed[r1][c1] = False
                            revealed[r2][c2] = False
                        first_click = None

                        # Check win
                        if all(all(row) for row in matched):
                            game_over = True

pygame.quit()
sys.exit()
