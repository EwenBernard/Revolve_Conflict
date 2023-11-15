import pygame
import sys
import math

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

