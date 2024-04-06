import pygame

# Константы
PLAYER_WIDTH = 80
PLAYER_HEIGHT = 80
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Определение класса Player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.is_sliding = False
        self.original_height = PLAYER_HEIGHT
        self.original_y = self.rect.y
        self.slide_distance = 100

    def update(self, keys):
        if keys[pygame.K_LCTRL]:
            if not self.is_sliding:
                self.is_sliding = True
                self.rect.height = self.original_height // 2
                self.rect.y = self.original_y + self.original_height // 2
                self.slide_distance = 100  # Сброс значения slide_distance для нового подката

        if self.is_sliding:
            if self.slide_distance > 0:
                self.rect.x += self.speed
                self.slide_distance -= self.speed
            else:
                self.is_sliding = False
                self.rect.height = self.original_height
                self.rect.y = self.original_y

# Инициализация Pygame
pygame.init()

# Создание экрана
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

player = Player(100, SCREEN_HEIGHT - PLAYER_HEIGHT)

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    player.update(keys)

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
