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
near_miss_distance = 70  # Distance threshold for near miss

# Store old positions for motion blur
enemy_trail = []
trail_length = 10  # Number of positions to store

player_trail = []
player_trail_length = 15

score = 0
game_over = False

def distance(pos1, pos2):
    return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # --- Movement Logic ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5

    # Add current position to the player's trail
    player_trail.append(tuple(player_pos))
    if len(player_trail) > player_trail_length:
        player_trail.pop(0)

    # Update enemy position
    enemy_pos[1] += enemy_speed

    # Add current position to the trail
    enemy_trail.append(tuple(enemy_pos))
    if len(enemy_trail) > trail_length:
        enemy_trail.pop(0)

    # --- Reset enemy if off screen ---
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        enemy_speed = random.randint(5, 25)
        player_size += 2
        score += 1
        print(f"Score: {score}")

    # --- Collision Detection ---
    if (
        enemy_pos[0] < player_pos[0] + player_size and
        enemy_pos[0] + enemy_size > player_pos[0] and
        enemy_pos[1] < player_pos[1] + player_size and
        enemy_pos[1] + enemy_size > player_pos[1]
    ):
        print("Game Over!")
        game_over = True

    # --- Near miss detection ---
    if distance(enemy_pos, player_pos) < near_miss_distance:
        # Trigger screen shake
        shake_frames = 15  # number of frames to shake
        shake_intensity = 10  # max shake offset

    # Determine shake offset
    if shake_frames > 0:
        offset_x = random.randint(-shake_intensity, shake_intensity)
        offset_y = random.randint(-shake_intensity, shake_intensity)
        shake_frames -= 1
    else:
        offset_x, offset_y = 0, 0

    # Drawing
    screen.fill((0, 0, 0))

    # Draw enemy trail
    for i, pos in enumerate(enemy_trail):
        fade_factor = (i + 1) / trail_length
        alpha = int(50 * fade_factor)
        trail_surface = pygame.Surface((enemy_size, enemy_size), pygame.SRCALPHA)
        trail_surface.fill((255, 0, 0, alpha))
        screen.blit(trail_surface, (pos[0] + offset_x, pos[1] + offset_y))

    # Draw player trail
    for i, pos in enumerate(player_trail):
        fade_factor = (i + 1) / player_trail_length
        alpha = int(50 * fade_factor)
        trail_surface = pygame.Surface((player_size, player_size), pygame.SRCALPHA)
        trail_surface.fill((0, 0, 255, alpha))
        screen.blit(trail_surface, (pos[0] + offset_x, pos[1] + offset_y))

    # Draw current enemy block
    pygame.draw.rect(screen, RED, (enemy_pos[0] + offset_x, enemy_pos[1] + offset_y, enemy_size, enemy_size))
    # Draw player
    pygame.draw.rect(screen, BLUE, (player_pos[0] + offset_x, player_pos[1] + offset_y, player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()