import pgzrun
from pygame import Rect
import random

# Tamanho da janela
WIDTH = 800
HEIGHT = 600

# Variáveis de estado: Usamos isso para: Saber se estamos no menu principal e saber se o som está ligado ou desligado
current_screen = 'menu'
sound_on = True
current_level = 1
sword_chest = Rect((700, 500), (40, 40))

# Botões como pygame.Rect (posição, tamanho) que cria um retangulo clicavvel
button_play = Rect((500, 200), (200, 50))
button_sound = Rect((500, 280), (200, 50))
button_quit = Rect((500, 360), (200, 50))

HERO_SPEED = 3
HERO_START_POS = [100, 100]

#classe Character para o jogador e para os inimigos
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

# Imagens para herói e inimigos

hero_idle = [images.hero_idle1, images.hero_idle2]
hero_walk = [images.hero_walk1, images.hero_walk2]

enemy_idle = [images.enemy_idle1, images.enemy_idle2]
enemy_walk = [images.enemy_walk1, images.enemy_walk2]

#criação de herois e inimigos
hero = Character(HERO_START_POS[0], HERO_START_POS[1], hero_idle, hero_walk)

enemies = []
for _ in range(3):
    x = random.randint(100, WIDTH - 150)
    y = random.randint(100, HEIGHT - 150)
    enemy = Character(x, y, enemy_idle, enemy_walk)
    enemies.append(enemy)

obstacles = [
    Rect((200, 150), (100, 100)),
    Rect((400, 300), (150, 50)),
    Rect((600, 100), (50, 200)),
]


# IA simples para inimigos
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

    # Testa movimento horizontal com colisão
    enemy.pos[0] += dx
    enemy.update()
    if any(enemy.rect.colliderect(ob) for ob in obstacles):
        enemy.pos[0] -= dx
        # opcional: muda de direção
        enemy.direction = random.choice(['up', 'down'])

    # Testa movimento vertical com colisão
    enemy.pos[1] += dy
    enemy.update()
    if any(enemy.rect.colliderect(ob) for ob in obstacles):
        enemy.pos[1] -= dy
        # opcional: muda de direção
        enemy.direction = random.choice(['left', 'right'])

    enemy.is_walking = (dx != 0 or dy != 0)
    enemy.update()



#Desenha o botão como um retângulo colorido e o texto centralizado nesse botão
def draw():
    screen.clear()

    if current_screen == 'menu':
        draw_menu()
    elif current_screen == 'jogo':
        draw_game()


def draw_menu():
    screen.fill((10, 50, 50))

    # Desenha os botões
    screen.draw.filled_rect(button_play, (50, 100, 200))
    screen.draw.text("Começar jogo", center=button_play.center, fontsize=30, color="white")

    screen.draw.filled_rect(button_sound, (50, 100, 200))
    sound_text = "Som: ON" if sound_on else "Som: OFF"
    screen.draw.text(sound_text, center=button_sound.center, fontsize=30, color="white")

    screen.draw.filled_rect(button_quit, (50, 100, 200))
    screen.draw.text("Sair", center=button_quit.center, fontsize=30, color="white")


def draw_game():
    screen.blit("background", (0, 0))

    for obstacle in obstacles:
        screen.draw.filled_rect(obstacle, (100, 100, 100))

    if current_level == 1:
        screen.draw.filled_rect(sword_chest, (255, 215, 0))

    hero.draw()

    for enemy in enemies:
        enemy.draw()


def update():
    global current_screen
    if current_screen == 'jogo':
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

            for enemy in enemies:
                enemy_ai(enemy)
                enemy.update()

                if hero.rect.colliderect(enemy.rect):
                   hero.pos = HERO_START_POS.copy()



def on_mouse_down(pos):
    global current_screen, sound_on

    if current_screen == 'menu':
        if button_play.collidepoint(pos):
            current_screen = 'jogo'
        elif button_sound.collidepoint(pos):
            sound_on = not sound_on
        elif button_quit.collidepoint(pos):
            quit()


pgzrun.go()
