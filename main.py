import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 200
BG_COLOR = (0, 0, 0)
RAY_COLOR = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ASCII Ray Tracing")

# Ray-tracing function
def ray_trace(origin, direction, t_min, t_max):
    for t in range(t_min, t_max):
        x, y = origin[0] + int(direction[0] * t), origin[1] + int(direction[1] * t)
        pygame.draw.circle(screen, RAY_COLOR, (x, y), 1)
        pygame.display.flip()

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BG_COLOR)

        # Define the ray parameters
        origin = (WIDTH // 2, HEIGHT // 2)
        angle = pygame.time.get_ticks() % 360  # Change the angle over time
        direction = (math.cos(math.radians(angle)), math.sin(math.radians(angle)))

        # Ray trace
        ray_trace(origin, direction, 0, 100)

        pygame.display.flip()

if __name__ == "__main__":
    main()

