import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
screen_width = 600
screen_height = 400
block_size = 20
player_color = (0, 255, 0)
maze_color = (0, 0, 255)
background_color = (0, 0, 0)
player_position = [50, 50]
player_speed = 20

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

# Maze data (1's are walls, 0's are paths)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Function to draw the maze
def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, maze_color, (col * block_size, row * block_size, block_size, block_size))
            else:
                pygame.draw.rect(screen, background_color, (col * block_size, row * block_size, block_size, block_size))

# Function to draw the player
def draw_player():
    pygame.draw.rect(screen, player_color, (player_position[0], player_position[1], block_size, block_size))

# Function to handle player movement
def move_player(keys):
    global player_position
    if keys[pygame.K_LEFT] and player_position[0] > 0 and maze[player_position[1] // block_size][(player_position[0] - block_size) // block_size] == 0:
        player_position[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_position[0] < screen_width - block_size and maze[player_position[1] // block_size][(player_position[0] + block_size) // block_size] == 0:
        player_position[0] += player_speed
    if keys[pygame.K_UP] and player_position[1] > 0 and maze[(player_position[1] - block_size) // block_size][player_position[0] // block_size] == 0:
        player_position[1] -= player_speed
    if keys[pygame.K_DOWN] and player_position[1] < screen_height - block_size and maze[(player_position[1] + block_size) // block_size][player_position[0] // block_size] == 0:
        player_position[1] += player_speed

# Main game loop
def game_loop():
    running = True
    while running:
        screen.fill(background_color)
        draw_maze()
        draw_player()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        move_player(keys)
        
        pygame.display.update()
        pygame.time.Clock().tick(30)  # Frame rate

    pygame.quit()

if __name__ == "__main__":
    game_loop()
