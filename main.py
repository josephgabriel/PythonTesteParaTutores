import pgzrun
from pygame import Rect
import random

WIDTH = 800
HEIGHT = 600

current_screen = 'menu'
sound_on = True
current_level = 1
background_name = "background"
sword_chest = Rect((700, 500), (40, 40))
sword_chest2 = Rect((600, 500), (40, 40))
sword_chest3 = Rect((600, 450), (40, 100))
enemies = []
music_playing = False

button_play = Rect((500, 200), (200, 50))
button_sound = Rect((500, 280), (200, 50))
button_quit = Rect((500, 360), (200, 50))

HERO_SPEED = 3
HERO_START_POS = [100, 100]

class Character:
    def __init__(self, x, y, images_idle, images_walk):
        self.pos = [x, y]
        self.rect = Rect(x, y, 50, 50)
        self.images_idle = images_idle
        self.images_walk = images_walk
        self.frame = 0
        self.animation_speed = 0.15
        self.is_walking = False

        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.move_timer = 0
        self.move_duration = random.randint(60, 180)

    def update(self):
        self.frame += self.animation_speed
        frames = self.images_walk if self.is_walking else self.images_idle
        if self.frame >= len(frames):
            self.frame = 0
        self.current_image = frames[int(self.frame)]
        self.rect.topleft = (self.pos[0], self.pos[1])

    def draw(self):
        screen.blit(self.current_image, (self.pos[0], self.pos[1]))

    def move(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy
        self.is_walking = (dx != 0 or dy != 0)

hero_idle = [images.hero_idle1, images.hero_idle2]
hero_walk = [images.hero_walk1, images.hero_walk2]

enemy_idle = [images.enemy_idle1, images.enemy_idle2]
enemy_walk = [images.enemy_walk1, images.enemy_walk2]

hero = Character(HERO_START_POS[0], HERO_START_POS[1], hero_idle, hero_walk)

obstacles = [
    Rect((200, 150), (100, 100)),
    Rect((400, 300), (150, 50)),
    Rect((600, 100), (50, 200)),
]

def enemy_ai(enemy):
    speed = 0.30
    dx = dy = 0

    enemy.move_timer += 1
    if enemy.move_timer >= enemy.move_duration:
        enemy.direction = random.choice(['left', 'right', 'up', 'down'])
        enemy.move_timer = 0
        enemy.move_duration = random.randint(60, 180)

    if enemy.direction == 'left':
        dx = -speed
    elif enemy.direction == 'right':
        dx = speed
    elif enemy.direction == 'up':
        dy = -speed
    elif enemy.direction == 'down':
        dy = speed

    
    enemy.pos[0] += dx
    enemy.update()
    if any(enemy.rect.colliderect(ob) for ob in obstacles):
        enemy.pos[0] -= dx
        
        enemy.direction = random.choice(['up', 'down'])

    enemy.pos[1] += dy
    enemy.update()
    if any(enemy.rect.colliderect(ob) for ob in obstacles):
        enemy.pos[1] -= dy

        enemy.direction = random.choice(['left', 'right'])

    enemy.is_walking = (dx != 0 or dy != 0)
    enemy.update()

    enemy_width = enemy.rect.width
    enemy_height = enemy.rect.height

    if enemy.pos[0] < 0:
        enemy.pos[0] = 0
    elif enemy.pos[0] > WIDTH - enemy_width:
        enemy.pos[0] = WIDTH - enemy_width

    if enemy.pos[1] < 0:
        enemy.pos[1] = 0
    elif enemy.pos[1] > HEIGHT - enemy_height:
        enemy.pos[1] = HEIGHT - enemy_height

def load_level(level):
    global current_level, obstacles, background_name, hero, enemies

    current_level = level
    enemies = []

    if level == 1:
        background_name = "background"

        obstacles = [
            Rect((200, 150), (100, 100)),
            Rect((400, 300), (150, 50)),
            Rect((600, 100), (50, 200)),
        ]

        enemy_positions = [(300, 300)]
        for pos in enemy_positions:
            enemy = Character(pos[0], pos[1], enemy_idle, enemy_walk)
            enemies.append(enemy)

        hero.pos = HERO_START_POS.copy()
        hero.update()

    elif level == 2:
        hero.images_idle = [images.herolv2_idle1, images.herolv2_idle2]
        hero.images_walk = [images.herolv2_walk1, images.herolv2_walk2]

        background_name = "background2"

        obstacles = [
            Rect((150, 80), (200, 30)),
            Rect((300, 250), (50, 200)),
            Rect((500, 400), (200, 50)),
        ]

        enemy_positions = [(100, 400), (600, 300)]
        for pos in enemy_positions:
            enemy = Character(pos[0], pos[1], enemy_idle, enemy_walk)
            enemies.append(enemy)

        hero.pos = HERO_START_POS.copy()
        hero.update()

    elif level == 3:
        hero.images_idle = [images.herolv3_idle1, images.herolv3_idle2]
        hero.images_walk = [images.herolv3_walk1, images.herolv3_walk2]

        background_name = "background3"

        obstacles = [
            Rect((150, 80), (200, 30)),
            Rect((220, 250), (90, 150)),
            Rect((300, 220), (170, 170)),
            ]
        
        enemy_positions = [(200, 200), (400, 400), (600, 100)]
        for pos in enemy_positions:
            enemy = Character(pos[0], pos[1], enemy_idle, enemy_walk)
            enemies.append(enemy)

        hero.pos = HERO_START_POS.copy()
        hero.update()

    elif level == 4:
        hero.images_idle = [images.herolv4_idle1, images.herolv4_idle2]
        hero.images_walk = [images.herolv4_walk1, images.herolv4_walk2]

        background_name = "last"
        obstacles = []
        enemies = []
        hero.pos = HERO_START_POS.copy()
        hero.update()

        if sound_on:
         sounds.background_music.stop()

load_level(current_level)

def draw():
    screen.clear()

    if current_screen == 'menu':
        draw_menu()
    elif current_screen == 'jogo':
        draw_game()


def draw_menu():
    screen.fill((10, 50, 50))
    screen.draw.text("Eu quero uma espada maior!", center=(WIDTH // 2, 100), fontsize=60, color="gold")

    screen.draw.text("Desvie dos inimigos, ache os baús, pegue as espadas e ajude o cavaleiro reaLizar seu sonho!", center=(WIDTH // 2, 150), fontsize=20, color="gold")

    screen.draw.filled_rect(button_play, (50, 100, 200))
    screen.draw.text("Começar jogo", center=button_play.center, fontsize=30, color="white")

    screen.draw.filled_rect(button_sound, (50, 100, 200))
    sound_text = "Som: ON" if sound_on else "Som: OFF"
    screen.draw.text(sound_text, center=button_sound.center, fontsize=30, color="white")

    screen.draw.filled_rect(button_quit, (50, 100, 200))
    screen.draw.text("Sair", center=button_quit.center, fontsize=30, color="white")


def draw_game():
    screen.blit(background_name, (0, 0))

    for obstacle in obstacles:
        screen.draw.filled_rect(obstacle, (100, 100, 100))

    hero.draw()

    for enemy in enemies:
        enemy.draw()

    if current_level == 1:
        screen.draw.filled_rect(sword_chest, (255, 215, 0))

    if current_level == 2:
        screen.draw.filled_rect(sword_chest2, (255, 215, 0))

    if current_level == 3:
        screen.draw.filled_rect(sword_chest3, (255, 255, 0))

    if current_level == 4:
        screen.draw.text("Você ganhou!", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="yellow")
        screen.draw.text("Jogo feito por José Gabriel Soares dos Santos", center=(WIDTH // 2, HEIGHT // 1.3), fontsize=30, color="white")

def update():
    global current_screen
    if current_screen == 'jogo':
        global music_playing

        if sound_on and not music_playing:
         sounds.background_music.play(-1) 
         music_playing = True
        elif not sound_on and music_playing:
          sounds.background_music.stop()
          music_playing = False

        dx = dy = 0
        if keyboard.left:
            dx = -HERO_SPEED
        elif keyboard.right:
            dx = HERO_SPEED
        if keyboard.up:
            dy = -HERO_SPEED
        elif keyboard.down:
            dy = HERO_SPEED

       
        hero.pos[0] += dx
        hero.update()
        if any(hero.rect.colliderect(ob) for ob in obstacles):
           hero.pos[0] -= dx  

        hero.pos[1] += dy
        hero.update()
        if any(hero.rect.colliderect(ob) for ob in obstacles):
           hero.pos[1] -= dy  

        hero.is_walking = (dx != 0 or dy != 0)
        hero.update()

        if current_level == 1 and hero.rect.colliderect(sword_chest):
            load_level(2)

        if current_level == 2 and hero.rect.colliderect(sword_chest2):
            load_level(3)

        if current_level == 3 and hero.rect.colliderect(sword_chest3):
          if sound_on:
            sounds.victory.play()
          load_level(4)


        hero_width = hero.rect.width
        hero_height = hero.rect.height

        if hero.pos[0] < 0:
          hero.pos[0] = 0

        elif hero.pos[0] > WIDTH - hero_width:
           hero.pos[0] = WIDTH - hero_width

        if hero.pos[1] < 0:
           hero.pos[1] = 0

        elif hero.pos[1] > HEIGHT - hero_height:
           hero.pos[1] = HEIGHT - hero_height

        hero.update()

        for enemy in enemies:
         enemy_ai(enemy)
         enemy.update()

         if current_level in [1, 2, 3]:
           enemy.draw()
 
         if hero.rect.colliderect(enemy.rect):
            if sound_on:
             sounds.hit.play()
            hero.pos = HERO_START_POS.copy()
            hero.update()


def on_mouse_down(pos):
    global current_screen, sound_on, music_playing

    if current_screen == 'menu':
        if button_play.collidepoint(pos):
            current_screen = 'jogo'
        elif button_sound.collidepoint(pos):
            sound_on = not sound_on
            if not sound_on:
                sounds.background_music.stop()
                music_playing = False
        elif button_quit.collidepoint(pos):
            quit()



pgzrun.go()
