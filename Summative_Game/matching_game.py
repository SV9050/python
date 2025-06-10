import pygame, random, sys

# --- Config ---
W, H, ROWS, COLS, SZ, M, HEAD = 600, 700, 4, 4, 120, 20, 80
BG, TILE, REV, TXT, WHITE = (30, 30, 30), (80, 80, 200), (200, 200, 255), (0, 0, 0), (255, 255, 255)

pygame.init()
FONT = pygame.font.SysFont(None, 60)
SMALL = pygame.font.SysFont(None, 40)
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Memory Match - Symbols")

# Only symbols used
SYMBOLS = list("!@#$%^&*")


def create_board():
    symbols = SYMBOLS * 2
    random.shuffle(symbols)
    return [symbols[i:i + COLS] for i in range(0, ROWS * COLS, COLS)]


def draw(grid, revealed, matched, moves, win):
    screen.fill(BG)
    for r in range(ROWS):
        for c in range(COLS):
            x, y = M + c * (SZ + M), M + r * (SZ + M) + HEAD
            rect = pygame.Rect(x, y, SZ, SZ)
            color = REV if revealed[r][c] or matched[r][c] else TILE
            pygame.draw.rect(screen, color, rect)
            if revealed[r][c] or matched[r][c]:
                text = FONT.render(grid[r][c], True, TXT)
                screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))
    screen.blit(SMALL.render(f"Moves: {moves}", True, WHITE), (20, 20))
    if win:
        t = FONT.render(f"You won in {moves} moves!", True, WHITE)
        screen.blit(t, (W // 2 - t.get_width() // 2, H - 120))
        instruction = SMALL.render("Press A to Play Again", True, WHITE)
        screen.blit(instruction, (W // 2 - instruction.get_width() // 2, H - 80))
    pygame.display.flip()


def get_tile(pos):
    x, y = pos[0], pos[1] - HEAD
    for r in range(ROWS):
        for c in range(COLS):
            tx, ty = M + c * (SZ + M), M + r * (SZ + M)
            if pygame.Rect(tx, ty, SZ, SZ).collidepoint(x, y):
                return r, c
    return None


def main():
    grid = create_board()
    revealed = [[0] * COLS for _ in range(ROWS)]
    matched = [[0] * COLS for _ in range(ROWS)]
    first, moves, win = None, 0, False
    clock = pygame.time.Clock()

    while True:
        draw(grid, revealed, matched, moves, win)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not win and e.type == pygame.MOUSEBUTTONDOWN:
                tile = get_tile(pygame.mouse.get_pos())
                if tile:
                    r, c = tile
                    if not revealed[r][c] and not matched[r][c]:
                        revealed[r][c] = 1
                        if not first:
                            first = (r, c)
                        else:
                            r1, c1 = first
                            moves += 1
                            draw(grid, revealed, matched, moves, win)
                            pygame.display.flip()
                            pygame.time.delay(600)
                            if grid[r1][c1] == grid[r][c]:
                                matched[r1][c1] = matched[r][c] = 1
                            else:
                                revealed[r1][c1] = revealed[r][c] = 0
                            first = None

                            if all(all(row) for row in matched):
                                win = True
                                draw(grid, revealed, matched, moves, win)
                                pygame.display.flip()
            elif win and e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    return  # Exit this game loop to restart


if __name__ == "__main__":
    while True:`
        main()
