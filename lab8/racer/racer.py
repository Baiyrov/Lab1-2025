import pygame
import random


pygame.init()


w, h = 400, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)


player_img = pygame.image.load(r"lab8/racer/Player.png")
enemy_img = pygame.image.load(r"lab8/racer/Enemy.png")
coin_img = pygame.image.load(r"lab8/racer/Coin.png")
street_img = pygame.image.load(r"lab8/racer/AnimatedStreet.png")
crash_sound = pygame.mixer.Sound(r"lab8/racer/Lab8_racer_crash.wav")
background_sound = pygame.mixer.Sound(r"lab8/racer/Lab8_racer_background.wav")


coin_img = pygame.transform.scale(coin_img, (30, 30))

screen = pygame.display.set_mode((w, h))


background_sound.play(-1)  

font = pygame.font.Font(None, 50)


bg_y1 = 0
bg_y2 = -h
bg_speed = 5


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(w // 2, h - 100))  
    
    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < w:
            self.rect.x += 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(midtop=(random.randint(50, w - 50), 0))
        self.speed = 5
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > h:
            self.rect.midtop = (random.randint(50, w - 50), 0)

# Класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect(midtop=(random.randint(50, w - 50), 0))
        self.speed = 3  
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > h:
            self.kill()


all_sprites = pygame.sprite.Group()
player = Player()
enemy = Enemy()
coins = pygame.sprite.Group()
all_sprites.add(player, enemy)

# Основной игровой цикл
running = True
clock = pygame.time.Clock()
score = 0  
score_font = pygame.font.Font(None, 36)

def show_game_over():
    """Экран окончания игры"""
    global running, score, all_sprites, coins, player, enemy
    game_over_running = True
    while game_over_running:
        screen.fill(RED)
        text = font.render("Game Over", True, WHITE)
        score_text = score_font.render(f"Монеты: {score}", True, WHITE)
        restart_text = score_font.render("       Enter Space", True, WHITE)
        
        screen.blit(text, (w // 2 - 100, h // 2 - 70))
        screen.blit(score_text, (w // 2 - 70, h // 2 - 20))
        screen.blit(restart_text, (w // 2 - 130, h // 2 + 30))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_running = False
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                score = 0
                all_sprites = pygame.sprite.Group()
                coins = pygame.sprite.Group()
                player = Player()
                enemy = Enemy()
                all_sprites.add(player, enemy)
                game_over_running = False

# Таймер для создания монет
coin_spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(coin_spawn_timer, 1500)  
while running:
    screen.fill(WHITE)

    # Прокрутка фона
    bg_y1 += bg_speed
    bg_y2 += bg_speed
    if bg_y1 >= h:
        bg_y1 = -h
    if bg_y2 >= h:
        bg_y2 = -h

    screen.blit(street_img, (0, bg_y1))
    screen.blit(street_img, (0, bg_y2))
    
    #
    keys = pygame.key.get_pressed()
    player.update(keys)
    enemy.update()
    coins.update()

    
    if pygame.sprite.collide_rect(player, enemy):
        crash_sound.play()
        show_game_over()

    collected_coins = pygame.sprite.spritecollide(player, coins, True)
    score += len(collected_coins)

    
    all_sprites.draw(screen)
    coins.draw(screen)

    
    score_text = score_font.render(f"Счёт: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    
    pygame.display.flip()
    clock.tick(60)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == coin_spawn_timer:
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)

pygame.quit()
