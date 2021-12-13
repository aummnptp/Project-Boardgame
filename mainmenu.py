import pygame, sys, os
import random
from tkinter import *
from pygame import mixer

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Arcade Python Boardgame') #game window name
screen = pygame.display.set_mode((1280, 720),0,32)
icon = pygame.image.load('images/icon.png') #icon image
pic1 = pygame.image.load('images/logo3.png') #icon image
pic2 = pygame.image.load('images/logo2.png') #icon image
pic3 = pygame.image.load('images/logo1.png') #icon image
pic4 = pygame.image.load('images/logo4.png') #icon image
pic5 = pygame.image.load('images/logo5.png') #icon image
pic8 = pygame.image.load('images/logo8.png') #icon image
pygame.display.set_icon(icon) #window icon
pygame.display.set_caption("Arcade Python Boardgame")
soundObj = pygame.mixer.Sound('mainmenu.mp3')
soundObj.set_volume(0.025)

font = pygame.font.SysFont(None, 26)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
global click
click = False
 
def main_menu():
    while True:
        global click
        soundObj.play(-1, 0)
        screen.fill((0,0,0))
        screen.blit(pic1, (110, 127))
        screen.blit(pic2, (462, 127))
        screen.blit(pic3, (814, 127))
        screen.blit(pic4, (285, 329))
        screen.blit(pic5, (637, 329))
        screen.blit(pic8, (1190, 630))
        draw_text('Arcade Python Boardgame', font, (255, 255, 255), screen, 525, 50)
        
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(110, 127, 350, 200)
        button_2 = pygame.Rect(462, 127, 350, 200)
        button_3 = pygame.Rect(814, 127, 350, 200)
        button_4 = pygame.Rect(285, 329, 350, 200)
        button_5 = pygame.Rect(637, 329, 350, 200)
        button_6 = pygame.Rect(1010, 630, 80, 80)
        button_7 = pygame.Rect(1100, 630, 80, 80)
        button_8 = pygame.Rect(1190, 630, 80, 80)
        pygame.draw.rect(screen, (255, 0, 0), button_6)
        pygame.draw.rect(screen, (255, 0, 0), button_7)
        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.pause()
                rockpasci()
        if button_2.collidepoint((mx, my)):
            if click:
                hang()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.mixer.pause()
                tict()
        if button_4.collidepoint((mx, my)):
            if click:
                fast()
        if button_5.collidepoint((mx, my)):
            if click:
                numg()
        if button_6.collidepoint((mx, my)):
            if click:
                pass
        if button_8.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)

# def togglemusic():
#     if pygame.mixer.get_busy():
#         pygame.mixer.pause()
#     else:
#         pygame.mixer.unpause()


def credits():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('credits', font, (255, 255, 255), screen, 20, 20)
        draw_text('made by', font, (255, 255, 255), screen, 20, 60)
        draw_text('64070046', font, (255, 255, 255), screen, 20, 100)
        draw_text('64070063', font, (255, 255, 255), screen, 20, 140)
        draw_text('64070079', font, (255, 255, 255), screen, 20, 180)
        draw_text('64070086', font, (255, 255, 255), screen, 20, 220)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def rockpasci():
    """game interface"""

    p1_all_re = {'wins':0, 'losses':0, 'ties':0} #แถบแสดงผลทั้งหมด

    def game_rule(p1_shoot, p2_shoot): #กติกา
        """rule of RPS"""
        if p1_shoot == p2_shoot:
            p1_all_re['ties'] += 1
            pygame.mixer.music.load('click.mp3')
            pygame.mixer.music.play()
            return "tied"
        elif (p1_shoot == "rock" and p2_shoot == "scissors") or (p1_shoot == "paper" and p2_shoot == "rock") or \
            (p1_shoot == "scissors" and p2_shoot == "paper"):
            p1_all_re['wins'] += 1
            pygame.mixer.music.load('click.mp3')
            pygame.mixer.music.play()
            return "P1 won"
        else:
            p1_all_re['losses'] += 1
            pygame.mixer.music.load('click.mp3')
            pygame.mixer.music.play()
            return "P1 lost"

    def on_click(e): #แสดงแถบผลการเล่นในรอบนั้นๆ
        p1_shoot = e.widget["text"]
        p2_shoot = random.choice(shoot)
        result = game_rule(p1_shoot, p2_shoot)
        tv_result.set(f'p1:{p1_shoot} - p2:{p2_shoot} >>> {result}')
        result_all.set(f'{p1_all_re["wins"]} wins, {p1_all_re["ties"]} ties, {p1_all_re["losses"]} losses')

    root = Tk()
    root.eval('tk::PlaceWindow . center')
    root.title('Rock Paper Scissors')
    root.option_add("*Font", "consolas 20")
    root.configure(bg='black')
    shoot = ['rock', 'paper', 'scissors']
    p1_shoot = [PhotoImage(file=f'{img}.png') for img in shoot]
    f1 = Frame(root)
    f1.grid(row=0, column=0)
    f2 = Frame(root)
    f2.grid(row=1, column=0)

    tv_result = StringVar()
    result_all = StringVar()

    for i in range(len(p1_shoot)):
        w = Button(f1, image=p1_shoot[i], text=shoot[i], bd=0, bg='black')
        w.pack(side=LEFT)
        w.bind('<Button-1>', on_click)
    Label(f2, textvariable=tv_result, width=40, bd=0, fg='white', bg='black').pack()
    Label(f2, textvariable=result_all, width=40, bd=0, fg='white', bg="black").pack()
    root.mainloop()
    pygame.mixer.unpause()

def fast():
    pass

def numg():
    pass

def tict():
    import pygame, sys
    import numpy as np

    pygame.init()

    width = 600
    height = 600
    line_width =15
    board_rows = 3
    board_cols = 3
    square_size = width//board_cols
    circle_r = square_size//3
    circle_w = 15
    cross_w = 25
    space = square_size//4
    #color = RGB
    bg_color = (0, 0, 0)
    line_color = (20, 20, 20)
    circle_color = (250, 237, 39)
    cross_color = (255, 16, 240)
    green = (0, 250, 0)
    #screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TIC TAC TOE (Press R to play again!)")
    screen.fill(bg_color)
    #board
    board = np.zeros((board_rows, board_cols))

    def drawlines():
        #1 horizontal line
        pygame.draw.line(screen, line_color, (0, square_size), (width, square_size), line_width)
        #2 horizontal line
        pygame.draw.line(screen, line_color, (0, 2*square_size), (width, 2*square_size), line_width)
        #1 vertical line
        pygame.draw.line(screen, line_color, (square_size, 0), (square_size, height), line_width)
        #2 vertical line
        pygame.draw.line(screen, line_color, (2*square_size, 0), (2*square_size, height), line_width)

    def draw_figures():
        for row in range(board_rows):
            for col in range(board_cols):
                if board[row][col] == 1:
                    pygame.draw.circle(screen, circle_color, (int(col * square_size + square_size//2), int(row * square_size + square_size//2)), circle_r, circle_w)
                elif board[row][col] == 2:
                    pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + square_size - space), (col * square_size + square_size - space, row * square_size + space), cross_w)
                    pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + space), (col * square_size + square_size - space, row * square_size + square_size - space), cross_w)

    #mark squares for player
    def mark_square(row, col, player):
        board[row][col] = player

    #check available square(s)
    def avaiable_square(row, col):
        if board[row][col] == 0:
            return True
        else:
            return False

    #if board is full return True
    def isboard_full():
        for row in range(board_rows):
            for col in range(board_cols):
                if board[row][col] == 0:
                    return False
        return True

    def check_win(player):
        #vertical win check
        for col in range(board_cols):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                draw_vert_winline(col, player)
                return True
        #horizontal win check
        for row in range(board_rows):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                draw_hori_winline(row, player)
                return True
        #ascending diag win check
        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            draw_ascdiag_line(player)
            return True
        #descending diag win check
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            draw_desdiag_line(player)
            return True

        return False

    def draw_vert_winline(col, player):
        posX = col * square_size + square_size//2
        if player == 1:
            color = green
        elif player == 2:
            color = green

        pygame.draw.line(screen, color, (posX, 15), (posX, height - 15), 15)

    def draw_hori_winline(row, player):
        posY = row * square_size + square_size//2
        if player == 1:
            color = green
        elif player == 2:
            color = green

        pygame.draw.line(screen, color, (15, posY), (width - 15, posY), 15)

    def draw_ascdiag_line(player):
        if player == 1:
            color = green
        elif player == 2:
            color = green

        pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), 15)

    def draw_desdiag_line(player):
        if player == 1:
            color = green
        elif player == 2:
            color = green

        pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)

    def restart():
        screen.fill(bg_color)
        drawlines()
        player = 1
        for row in range(board_rows):
            for col in range(board_cols):
                board[row][col] = 0

    drawlines()

    player = 1
    gameover = False

    #mainloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN and not gameover:

                mouseX = event.pos[0] #x
                mouseY = event.pos[1] #y
                
                click_row = int(mouseY // square_size)
                click_col = int(mouseX // square_size)

                if avaiable_square(click_row, click_col):
                    mark_square(click_row, click_col, player)
                    if check_win(player):
                        gameover = True
                    player = player % 2 + 1

                    draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    gameover = False
        pygame.display.update()

def hang():
    os.system('python hang.py')

main_menu()
