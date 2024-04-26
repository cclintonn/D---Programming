# Introduction to Pygame
#   - Boilerplate is useful to set up our enviroments
#   - The Sprite class has some really cool things in it

import pygame
import random  # Import random for generating random numbers

class Dvdlogo(pygame.sprite.Sprite):
    """Represents DVD logo sprite"""

    def __init__(self, x, y, vel_x, vel_y):
        super().__init__()

        self.image = pygame.image.load("./Images/dvd-logo.png")
        self.rect = self.image.get_rect(center=(x, y))  # Randomized initial position

        # Randomized Velocity of the Dvd Logo
        self.vel_x = vel_x
        self.vel_y = vel_y

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Bounce off the bottom
        if self.rect.bottom > 720:
            self.vel_y *= -1
        # Bounce off the top
        if self.rect.top < 0:
            self.vel_y *= -1
        # Bounce off the left
        if self.rect.left < 0:
            self.vel_x *= -1
        # Bounce off the right
        if self.rect.right > 1280:
            self.vel_x *= -1

def start():
    pygame.init()

    WIDTH = 1280  # Pixels
    HEIGHT = 720
    SCREEN_SIZE = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("DVD Logo Screensaver")
    done = False
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    # Create five DVD logos with random positions and velocities
    for _ in range(5):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        vel_x = random.randint(-20, 20)  # Random velocity in x
        vel_y = random.randint(-20, 20)  # Random velocity in y
        dvdlogo = Dvdlogo(x, y, vel_x, vel_y)
        all_sprites.add(dvdlogo)  # Add the new logo to the sprite group

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        all_sprites.update()

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)  # 60 fps

def main():
    start()

if __name__ == "__main__":
    main()