# Clinton Chieng
# May 21, 2024
# pygame-example-shmup.py
# Shoot 'em up

import pygame as pg
import random

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 720
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)
ENEMY_SPAWN_TIME = 1000  # milliseconds

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/galaga_ship.png")
        self.rect = self.image.get_rect()

    def update(self):
        """Follow the mouse"""
        self.rect.center = pg.mouse.get_pos()

        # Keep it at the bottom of the screen
        if self.rect.top < HEIGHT - 200:
            self.rect.top = HEIGHT - 200


class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        """
        Params:
            player_loc: x,y coords of centerx and top
        """
        super().__init__()

        # Green rectangle
        self.image = pg.Surface((10, 25))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

        # Spawn at the Player
        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]

        # Vertical velocity
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # Remove bullet if it goes off screen
        if self.rect.bottom < 0:
            self.kill()


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Red rectangle as placeholder
        self.image = pg.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        
        self.speedx = random.choice([-3, 3])
        self.speedy = 1

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Move left to right
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speedx = -self.speedx
        
        # Remove enemy if it goes off screen
        if self.rect.top > HEIGHT:
            self.kill()


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    bullets = pg.sprite.Group()
    enemies = pg.sprite.Group()

    # Create the Player sprite object
    player = Player()
    all_sprites.add(player)

    pg.display.set_caption("Shoot 'Em Up")

    # Timer for enemy spawn
    pg.time.set_timer(pg.USEREVENT + 1, ENEMY_SPAWN_TIME)

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                bullet = Bullet((player.rect.centerx, player.rect.top))
                all_sprites.add(bullet)
                bullets.add(bullet)
            if event.type == pg.USEREVENT + 1:
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)

        # --- Update the world state
        all_sprites.update()

        # Check for bullet-enemy collisions
        hits = pg.sprite.groupcollide(bullets, enemies, True, True)

        # --- Draw items
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()