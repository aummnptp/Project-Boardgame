from tkinter.constants import W
import pygame, math, random
from wordsforhangman import word_list
#from pygame import display

pygame.init()
width, hight = 900, 550
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
LETTER_FONT = pygame.font.Font("fontgame.TTF", 60)
WORD_FONT = pygame.font.Font("fontgame.TTF", 90)

PressSound= pygame.mixer.Sound('press.wav')

#load รูป
img = pygame.image.load('C:/Users/aumm/Desktop/PJ/spacebg.jpg')
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#color
BLACK = (0, 0, 12)
WHITE = (204,255,255)#240,248,255

#game vailable
hangman_status = 0
words = [random.choice(word_list).upper()]
word = random.choice(words)
guessed = []
print(word)



def draw():
    win.blit(img,(0,0))
    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, WHITE)
    win.blit(text, (300, 200))

    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            text = LETTER_FONT.render(ltr, 1 , WHITE)
            win.blit(text, (x - text.get_width()/1, y- text.get_height()/2))

    win.blit(images[hangman_status],(35, 100))
    pygame.display.update()
#score font
GAMEOVER_FONT = pygame.font.Font("fontgame.TTF",180)
SCORE_FONT = pygame.font.Font("fontgame.TTF",90)
def display_message(message1,message2,message3):
    win.fill(BLACK)
    text1 = GAMEOVER_FONT.render(message1, 1 , WHITE)
    text2 = SCORE_FONT.render(message2, 1 , WHITE)
    text3 = SCORE_FONT.render(message3, 1 , WHITE)
    win.blit(text1, (width/2 - text1.get_width()/2, hight/8 - text1.get_height()/10))
    win.blit(text2, (width/2 - text2.get_width()/2, hight/2 - text2.get_height()/2))
    win.blit(text3, (width/2 - text3.get_width()/2, hight/1.5 - text3.get_height()/10))
    pygame.display.update()
    pygame.time.delay(500)



#setgameloop
FPS = 60
clock = pygame.time.Clock()
run = True  
while run:
    clock.tick(FPS)
    pygame.display.flip()

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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
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
    
    word_correct = "Correct Answer is "
    #ถ้าชนะ
    if won:
        display_message("Congratulation", "YOU WON!","Press R & Try Again!")


    #ถ้าแพ้(hangman=6)
    if hangman_status == 6:
        word_correct += word
        display_message("GAME OVER", word_correct, "Press R & Try Again!")


pygame.quit()
