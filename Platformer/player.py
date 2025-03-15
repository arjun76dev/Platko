import pygame
from level import Level

class Player:
    def __init__(self, level):
        super().__init__()
        self.level = level  # Store level reference

        self.velocity = 5
        self.gravity = 0
        self.max_gravity = 100
        self.jump_power = -20

        self.on_ground = False
        self.display_surface = pygame.display.get_surface()
        self.rect = pygame.Rect(50, 50, 40, 40)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity

    def draw(self):
        pygame.draw.rect(self.display_surface, (255, 0, 0), self.rect)

    def apply_gravity(self):
        if not self.on_ground:
            self.gravity = min(self.gravity + 1, self.max_gravity)
            self.rect.y += self.gravity

    def handle_collisions(self):
        self.on_ground = False
        platforms = self.level.levels[self.level.level - 1]  # Get current level platforms

        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.gravity > 0 and self.rect.bottom > platform.top and self.rect.bottom - self.gravity <= platform.top:
                    self.rect.bottom = platform.top
                    self.gravity = 0
                    self.on_ground = True

                elif self.rect.right > platform.left and self.rect.left < platform.left:
                    self.rect.right = platform.left

                elif self.rect.left < platform.right and self.rect.right > platform.right:
                    self.rect.left = platform.right

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.on_ground:
            self.gravity = self.jump_power
            self.on_ground = False

    def load_level(self):
	    if self.rect.x >= 790:  # Right edge
	        if self.level.level == 1:
	            self.level.level = 2  # Switch to level 2
	            self.rect.x = 10  # Move player to the left side of the screen
	        elif self.level.level == 2:
	            self.level.level = 1  # Switch back to level 1
	            self.rect.x = 10

	    if self.rect.x <= 0:  # Left edge
	        if self.level.level == 2:
	            self.level.level = 1
	            self.rect.x = 790  # Move player to the right side of the screen
	        elif self.level.level == 1:
	            self.level.level = 2
	            self.rect.x = 790

