import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

shake_frames = 0
shake_intensity = 0

# Store old positions for motion blur
enemy_trail = []
trail_length = 10  # Number of positions to store

player_trail = []
player_trail_length = 15

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    

    # --- BUG 1: Movement Logic ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  # Should move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  # Should move right

    # Add current position to the player's trail
    player_trail.append(tuple(player_pos))  # Store a copy of the current position

    # Limit the player's trail length
    if len(player_trail) > player_trail_length:
        player_trail.pop(0)

    # Update enemy position
    enemy_pos[1] += enemy_speed

    # Add current position to the trail
    enemy_trail.append(tuple(enemy_pos))  # Store a copy of the current position

    # Limit the trail length
    if len(enemy_trail) > trail_length:
        enemy_trail.pop(0)

    # --- BUG 2: Resetting the Enemy ---
    if enemy_pos[1] > HEIGHT:
        # The enemy should go back to the top with a new X position
        # but the code below is missing something to make it "restart"
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        enemy_speed = random.randint(5, 25)  # Random speed for the next enemy
        player_size += 2
        score += 1
        print(f"Score: {score}")




    # --- BUG 3: Collision Detection ---
    # This logic is mathematically incorrect for rectangular collision
    if (
        enemy_pos[0] < player_pos[0] + player_size and
        enemy_pos[0] + enemy_size > player_pos[0] and
        enemy_pos[1] < player_pos[1] + player_size and
        enemy_pos[1] + enemy_size > player_pos[1]
    ):
        print("Game Over!")
        game_over = True


    # Drawing
    screen.fill((0, 0, 0))
    
    # Draw the trail
    for i, pos in enumerate(enemy_trail):
        fade_factor = (i + 1) / trail_length  # Calculate fade factor
        alpha = int(50 * fade_factor)  # Transparency (0 = fully transparent, 255 = fully opaque)

        # Create a semi-transparent surface for the trail segment
        trail_surface = pygame.Surface((enemy_size, enemy_size), pygame.SRCALPHA)
        trail_surface.fill((255, 0, 0, alpha))  # Red with transparency

        # Blit the trail segment onto the screen
        screen.blit(trail_surface, (pos[0], pos[1]))



    for i, pos in enumerate(player_trail):
        fade_factor = (i + 1) / player_trail_length  # Calculate fade factor
        alpha = int(50 * fade_factor)  # Transparency (0 = fully transparent, 255 = fully opaque)

        # Create a semi-transparent surface for the trail segment
        trail_surface = pygame.Surface((player_size, player_size), pygame.SRCALPHA)
        trail_surface.fill((0, 0, 255, alpha))  # Red with transparency

        # Blit the trail segment onto the screen
        screen.blit(trail_surface, (pos[0], pos[1]))

    # Draw the current enemy block
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()

# Near miss detection (adjust threshold as needed)
near_miss_distance = 10
if (
    abs(enemy_pos[0] - player_pos[0]) < player_size and  # horizontally close
    abs(enemy_pos[1] + enemy_size - player_pos[1]) < near_miss_distance and  # just passed the player
    enemy_pos[1] < player_pos[1]  # enemy is above or at the player
):
    shake_frames = 10  # number of frames to shake
    shake_intensity = 8  # pixels to shake

# Drawing
screen.fill((0, 0, 0))

# Screen shake offset
offset_x, offset_y = 0, 0
if shake_frames > 0:
    offset_x = random.randint(-shake_intensity, shake_intensity)
    offset_y = random.randint(-shake_intensity, shake_intensity)
    shake_frames -= 1

# Draw the trail (enemy)
for i, pos in enumerate(enemy_trail):
    fade_factor = (i + 1) / trail_length
    alpha = int(50 * fade_factor)
    trail_surface = pygame.Surface((enemy_size, enemy_size), pygame.SRCALPHA)
    trail_surface.fill((255, 0, 0, alpha))
    screen.blit(trail_surface, (pos[0] + offset_x, pos[1] + offset_y))

# Draw the trail (player)
for i, pos in enumerate(player_trail):
    fade_factor = (i + 1) / player_trail_length
    alpha = int(50 * fade_factor)
    trail_surface = pygame.Surface((player_size, player_size), pygame.SRCALPHA)
    trail_surface.fill((0, 0, 255, alpha))
    screen.blit(trail_surface, (pos[0] + offset_x, pos[1] + offset_y))

# Draw the current enemy block
pygame.draw.rect(screen, RED, (enemy_pos[0] + offset_x, enemy_pos[1] + offset_y, enemy_size, enemy_size))
pygame.draw.rect(screen, BLUE, (player_pos[0] + offset_x, player_pos[1] + offset_y, player_size, player_size))
