import pgzrun
from pygame import Rect
import random

# Tamanho da janela
WIDTH = 800
HEIGHT = 600

# Variáveis de estado: Usamos isso para: Saber se estamos no menu principal e saber se o som está ligado ou desligado
current_screen = 'menu'
sound_on = True

# Botões como pygame.Rect (posição, tamanho) que cria um retangulo clicavvel
button_play = Rect((500, 200), (200, 50))
button_sound = Rect((500, 280), (200, 50))
button_quit = Rect((500, 360), (200, 50))

HERO_SPEED = 3

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
hero = Character(100, 100, hero_idle, hero_walk)

enemies = []
for _ in range(3):
    x = random.randint(100, WIDTH - 150)
    y = random.randint(100, HEIGHT - 150)
    enemy = Character(x, y, enemy_idle, enemy_walk)
    enemies.append(enemy)

# IA simples para inimigos
def enemy_ai(enemy):
    radius = 50
    center_x, center_y = enemy.pos
    dx = random.choice([-1, 0, 1]) * 2
    dy = random.choice([-1, 0, 1]) * 2
    new_x = enemy.pos[0] + dx
    new_y = enemy.pos[1] + dy

    if abs(new_x - center_x) < radius:
        enemy.pos[0] = new_x
    if abs(new_y - center_y) < radius:
        enemy.pos[1] = new_y

    enemy.is_walking = (dx != 0 or dy != 0)


#Desenha o botão como um retângulo colorido e o texto centralizado nesse botão
def draw():
    screen.clear()

    if current_screen == 'menu':
        draw_menu()
    elif current_screen == 'jogo':
        draw_game()


def draw_menu():
    screen.fill((10, 50, 50))  # Fundo escuro

    # Desenha os botões
    screen.draw.filled_rect(button_play, (50, 100, 200))
    screen.draw.text("Começar jogo", center=button_play.center, fontsize=30, color="white")

    screen.draw.filled_rect(button_sound, (50, 100, 200))
    sound_text = "Som: ON" if sound_on else "Som: OFF"
    screen.draw.text(sound_text, center=button_sound.center, fontsize=30, color="white")

    screen.draw.filled_rect(button_quit, (50, 100, 200))
    screen.draw.text("Sair", center=button_quit.center, fontsize=30, color="white")


def draw_game():
    screen.fill((0, 0, 0))  # Fundo preto
    screen.draw.text("Jogo iniciou!", center=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="white")

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

        hero.move(dx, dy)
        hero.update()

        for enemy in enemies:
            enemy_ai(enemy)
            enemy.update()


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
