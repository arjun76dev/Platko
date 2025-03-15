import pygame

class Level:
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.level = 1  

        self.floor = pygame.Rect(0, 580, 800, 20)

        # Level 1 platforms
        self.platform_rects = [
            self.floor,
            pygame.Rect(50, 480, 200, 20),
            pygame.Rect(400, 400, 200, 20),
        ]

        # Level 2 platforms
        self.platform_rects2 = [
            self.floor,
            pygame.Rect(100, 480, 200, 20),
            pygame.Rect(450, 400, 200, 20),
        ]

        self.levels = [self.platform_rects, self.platform_rects2]  # Store platforms by level

    def draw(self):
        platforms = self.levels[self.level - 1]
        color = (255, 0, 0) if self.level == 1 else (0, 255, 0)
        
        for platform in platforms:
            pygame.draw.rect(self.display_surface, color, platform)
