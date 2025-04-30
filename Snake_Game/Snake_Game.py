import pygame
import random
import time

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 640, 480
BLOCK_SIZE = 20       # Snake block size
FOOD_SIZE = 15        # Food is smaller
SPEED = 12
BLACK, WHITE, GREEN, YELLOW = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 255, 0)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sachin's Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Draw messages
def show_message(text, color, y_offset=0):
    msg = font.render(text, True, color)
    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 + y_offset))

# Draw the snake with head in a different color
def draw_snake(snake):
    for index, segment in enumerate(snake):
        color = YELLOW if index == len(snake) - 1 else GREEN
        pygame.draw.rect(screen, color, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

# Show score
def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Intro screen
def show_intro():
    while True:
        screen.fill(BLACK)
        show_message("Sacxx's Snake Game", WHITE, -60)
        show_message("Press SPACE to Start", WHITE)
        show_message("Press Q to Quit", WHITE, 40)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: return
                if event.key == pygame.K_q: pygame.quit(); quit()

# Game loop
def game_loop():
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy, length = 0, 0, 1
    snake = [[x, y]]
    food_x = random.randrange(0, WIDTH - FOOD_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - FOOD_SIZE, BLOCK_SIZE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: running = False
                if event.key == pygame.K_LEFT and dx == 0: dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0: dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0: dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0: dx, dy = 0, BLOCK_SIZE

        x, y = (x + dx) % WIDTH, (y + dy) % HEIGHT
        snake.append([x, y])
        if len(snake) > length: snake.pop(0)

        # Collision with self
        if [x, y] in snake[:-1]:
            show_message("FY - NISHID  ", WHITE)
            show_score(length - 1)
            pygame.display.update()
            time.sleep(2)
            break

        # Collision with food
        if abs(x - food_x) < BLOCK_SIZE and abs(y - food_y) < BLOCK_SIZE:
            food_x = random.randrange(0, WIDTH - FOOD_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - FOOD_SIZE, BLOCK_SIZE)
            length += 1

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))  # Food
        draw_snake(snake)
        show_score(length - 1)
        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()

# Start the game
show_intro()
game_loop()
