import pygame
import sys
import math

# ------- Setup Display -------------
pygame.init()
WIDTH, HEIGHT = 750, 598
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!!")

# Game Variables
game_status = 0
word = "DEVELOPER"
guessed = []
# Button Variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 450
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (RADIUS * 2 + GAP))
    letters.append([x, y, chr(A+i), True])

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
Word_Font = pygame.font.SysFont('comicsans', 60)
Title_Font = pygame.font.SysFont('comicsans', 70)

# --------- Load Images -----------
images = []
for i in range(7):
    image = pygame.image.load("Hangman_images/hangman" + str(i) + ".png")
    images.append(image)


# ---------- Set up game loop -----------
FPS = 60
clock = pygame.time.Clock()
run = True


def display_message(message):
    pygame.time.delay(1000)
    screen.fill(white)
    text = Word_Font.render(message, True, black)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


def draw():
    screen.fill(white)
    text = Title_Font.render("Hangman Demo", True, black)
    screen.blit(text, (WIDTH/2-text.get_width()/2, 20))
    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + ""
        else:
            display_word += "_ "
    text = Word_Font.render(display_word, True, black)
    screen.blit(text, (350, 250))
    # Draw Buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, black, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, True , black)
            screen.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

    screen.blit(images[game_status], (100, 100))
    pygame.display.update()


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            game_status += 1
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("You Won!!")
    if game_status == 6:
        display_message("You Lost!!")

pygame.quit()
sys.exit()

