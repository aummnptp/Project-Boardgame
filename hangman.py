import pygame, math, random
from wordsforhangman import word_list
from pygame import display

pygame.init()
width, hight = 800, 500
win = pygame.display.set_mode((width,hight))
pygame.display.set_caption("Hangman")
pygame.mixer.init()


#ปุ่ม variables
RADIUS = 20
GAP = 15
letters = []
startx = round((width-(RADIUS * 2 + GAP)*13) /2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i% 13)
    y = starty + ((i//13)*(GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True]) 

#fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 30)
WORD_FONT = pygame.font.SysFont('comicsans', 55)

#Sound
PressSound= pygame.mixer.Sound('press.wav')
#load รูป
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#game vailable
hangman_status = 0
words = [random.choice(word_list).upper()]
word = random.choice(words)
guessed = []
print(word)
 
def draw():
    win.fill(WHITE)
    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (300, 200))

    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win,BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1 , BLACK)
            win.blit(text, (x - text.get_width()/2, y- text.get_height()/2))

    win.blit(images[hangman_status],(35, 100))
    pygame.display.update()

def display_message(message):
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1 , BLACK)
    win.blit(text, (width/2 - text.get_width()/2, hight/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)

#setgameloop
FPS = 60
clock = pygame.time.Clock()
run = True 
    
while run:
    clock.tick(FPS)

    draw()

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
                            hangman_status += 1
                        PressSound.play()#เสียงตอนกดปุ่ม
        if event.type == pygame.KEYDOWN:
            #รีเซตเกม
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                hangman_status = 0
                words = [random.choice(word_list).upper()]
                word = random.choice(words)
                letters = []
                guessed = []
                images = []

                for i in range(7):
                    image = pygame.image.load("hangman" + str(i) + ".png")
                    images.append(image)
                print(word)
                for i in range(26):
                    x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i% 13)
                    y = starty + ((i//13)*(GAP + RADIUS * 2))
                    letters.append([x, y, chr(A + i), True])
    
   won = True
    for letter in word:
        if letter not in guessed:
            won = False
    
    word_correct = "Correct word:" 
    #ถ้าชนะ
    if won:
        display_message("YOU WON!")

    #ถ้าแพ้(hangman=6)
    if hangman_status == 6:
        word_correct += word
        display_message(word_correct)





pygame.quit()
