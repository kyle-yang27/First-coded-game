## Experimental Python pgyame code
# Breakout

# Python

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

clock = pygame.time.Clock()

# Game reset function
#### Here is a function that includes all global variabes and the initizalization of the game for a reset
def reset_game():
    global paddle, ball, ball_dx, ball_dy
    global bricks, score, lives, font

    paddle = pygame.Rect(350, 550, 100, 20)

    ball = pygame.Rect(390, 300, 20, 20)
    ball_dx = 4
    ball_dy = -4

    bricks = []

    for row in range(5):
        for column in range(10):
            brick = pygame.Rect(
                column * 80,
                row * 30 + 50,
                75,
                20
            )

            bricks.append(brick)

    score = 0
    font = pygame.font.Font(None, 36)
    lives = 3
#### End of function   

reset_game() 

####This group of code replease the game reset function, intializing all included variables
#     paddle = pygame.Rect(350, 550, 100, 20)

#     # Create the Ball
#     ball = pygame.Rect(390, 300, 20, 20)

#     ball_dx = 4
#     ball_dy = -4

#     # Create the bricks
#     bricks = []
#     for row in range(5):
#         for column in range(10):

#             brick = pygame.Rect(
#                 column * 80,
#                 row * 30 + 50,
#                 75, 
#                 20
#             )
#             # Append the bricks to a bricks list
#             bricks.append(brick)


#     # Add a score
#     score = 0
#     font = pygame.font.Font(None, 36)

#     # Add lives
#     lives = 3
##### End code group

# Game state variable
game_state = "playing"

running = True


while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Listen for the R key for Restart on the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
                game_state = "playing"
        
    # Make the paddle move
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle.x -= 5
    
    if keys[pygame.K_RIGHT]:
        paddle.x += 5

    if paddle.left < 0:
        paddle.left = 0

    if paddle.right > WIDTH:
        paddle.right = WIDTH

    # Update the ball
    ball.x += ball_dx
    ball.y += ball_dy


    # Make the ball bounce off the walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx *= -1

    if ball.top <= 0:
        ball_dy *= -1

    # Ask if ball collides with rectangle
    if ball.colliderect(paddle):
        # ball_dy *= -1 # Original code for regular physics when ball collides with paddle

        #### Ball collision off paddle has different physics as a result (measures distant from center and launches ball in direction by factor of 10 in that direction)
        ball_dy = -4

        paddle_center = paddle.centerx
        ball_center = ball.centerx

        difference = ball_center - paddle_center

        ball_dx = difference / 10 # Ball can move at different horizontal speeds

    # Destroy Bricks
    for brick in bricks:
        
        if ball.colliderect(brick):
            bricks.remove(brick)
            score += 10
            ball_dy *= -1
            break

    # Detect if ball falls
    if ball.top > HEIGHT:
        lives -= 1

        ball.x = 390
        ball.y = 300

        ball_dx = 4
        ball_dy = -4

    # Create Game Over Screen // Stop game if all lives have been lost
    if lives <= 0:
        game_state = "game_over"
        # running = False # Comment out so the game will not close when game_over game state is reached

    # Stop game if all bricks are destropyed
    if len(bricks) == 0:
        game_state = "won"
        # running = False # Not sure if line of code works
    
    #### Draw Everything ####

     # Draw background
    screen.fill("black")

    # Draw the paddle
    pygame.draw.rect(screen, "white", paddle) # draws near bottom by default, according to the dimensions provided in pygame.Rect()

    # Draw the ball
    pygame.draw.ellipse(screen, "white", ball)

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(screen, "red", brick)

    # Display the score after each brick is destroyed
    score_text = font.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (10, 10)) 

    # Display the number of lives next to the score
    lives_text = font.render(f"Lives: {lives}", True, "white")
    screen.blit(lives_text, (650, 10))

    if game_state == "game_over":
        game_over_text = font.render("GAME_OVER", True, "white")
        screen.fill("black")
        screen.blit(game_over_text,(300, 280))

    if game_state == "won":
        win_text = font.render("YOU WIN!", True, "white")
        screen.fill("black")
        screen.blit(win_text, (300, 280))

    # Update the screen
    pygame.display.flip()

    # Limit game to 60 FPS
    clock.tick(60)

pygame.quit()