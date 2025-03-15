import pygame
from player import Player
from level import Level

pygame.init()

class Game:
    def __init__(self):
        super().__init__()
        self.clock = pygame.time.Clock()
        self.width, self.height = 800, 600
        self.fps = 60

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('StopFire')

        self.level = Level()
        self.player = Player(self.level)  # Pass level to player

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.level.level = 2 if self.level.level == 1 else 1  # Switch levels

            self.screen.fill((0, 0, 0))
            self.level.draw()
            self.player.move()
            self.player.apply_gravity()
            self.player.handle_collisions()
            self.player.jump()
            self.player.load_level()
            self.player.draw()

            pygame.display.update()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    game = Game()
    game.run()

pygame.quit()
