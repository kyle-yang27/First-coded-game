# Python file
# Pygame file (use pygame-ce in venv my_game_env)

# Game of Snake

import pygame
import random

# Initialize Pygame()
pygame.init()

# ------------------
# Game settings
# ------------------

WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# ------------------
# Snake
# ------------------

snake = [
    [300, 200],
    [280, 200],
    [260, 200]
]

direction = [CELL_SIZE, 0]

# ------------------
# FOOD
# ------------------

food = [
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE)
]

# ------------------
# SCORE
# ------------------

score = 0
font = pygame.font.SysFont(None, 36)

# ------------------
# Game Loop
# ------------------

running = True
game_over = False

while running:

    # ------------------
    # Handle Events
    # ------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    direction = [0, -CELL_SIZE]

                elif event.key == pygame.K_DOWN:
                    direction = [0, CELL_SIZE]

                elif event.key == pygame.K_LEFT:
                    direction = [-CELL_SIZE, 0]

                elif event.key == pygame.K_RIGHT:
                    direction = [CELL_SIZE, 0]

    # -----------------
    # Move Snake
    # -----------------

    if not game_over:

        new_head = [
            snake[0][0] + direction[0],
            snake[0][1] + direction[1]
        ]

        snake.insert(0, new_head)

        # ---------------
        # Eat Food
        # ---------------

        if snake[0] == food:
            
            score += 1

            food = [
                random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE)
            ]

        else:
            # Remove the tail
            snake.pop()

        # -------------------
        # Wall Collision
        # -------------------

        head_x = snake[0][0]
        head_y = snake[0][1]

        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
        ):
            game_over = True

        # -------------------
        # Self Collision
        # -------------------

        if snake[0] in snake[1:]:
            game_over = True

    # ------------------
    # Draw Everything 
    # ------------------

    screen.fill((0, 0, 0))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (segment[0], segment[1], CELL_SIZE, CELL_SIZE)
        )
    
    # Draw Food
    pygame.draw.rect(
        screen,
        (255,0,0),
        (food[0], food[1], CELL_SIZE, CELL_SIZE)
    )

    # Draw Score
    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (10, 10))

    # Game over message
    if game_over:

        game_over_text = font.render(
            "GAME OVER",
            True,
            (255, 255, 255)
        )

        screen.blit(
            game_over_text,
            (WIDTH // 2 - 80, HEIGHT // 2)
        )

    pygame.display.flip()

    # Control game speed
    clock.tick(10)

pygame.quit()