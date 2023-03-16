import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen size
screen_width = 480
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set game variables
block_size = 20
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)


# Define functions
def draw_snake(block_size, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, block_size, block_size])


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [screen_width / 6, screen_height / 3])


# Main game loop
def gameLoop():
    game_exit = False
    game_over = False

    # Set starting position for snake
    lead_x = screen_width / 2
    lead_y = screen_height / 2
    lead_x_change = 0
    lead_y_change = 0

    # Set starting position for food
    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    # Set starting length for snake
    snake_list = []
    snake_length = 1

    while not game_exit:

        # Check for game over condition
        while game_over:
            screen.fill(black)
            message_to_screen("Game over. Press Q to quit or C to play again.", red)
            pygame.display.update()

            # Handle events while game over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        # Handle events while game is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # Check for collision with wall
        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y < 0:
            game_over = True

        # Update snake position and length
        lead_x += lead_x_change
        lead_y += lead_y_change
        snake_head = [lead_x, lead_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with self
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        # Draw game elements
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])
        draw_snake(block_size, snake_list)
        pygame.display.update()

        # Check for collision with food
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1

        # Update game clock
        clock.tick(10)

    # Quit Pygame and exit program
    pygame.quit()
    quit()


if __name__ == '__main__':
    gameLoop()
