import pgzrun
from pygame import Rect

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

#Desenha o botão como um retângulo colorido e o texto centralizado nesse botão
def draw():
    screen.clear()

    if current_screen == 'menu':
        draw_menu()
    elif current_screen == 'jogo':
        draw_game()


def draw_menu():
    screen.fill((30, 30, 30))  # Fundo escuro

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
