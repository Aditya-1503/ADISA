import pygame
import random
pygame.init()

win = pygame.display.set_mode((550,650))
pygame.display.set_caption("Tic Tac Toe")

win.fill((10, 70, 105))
first = pygame.draw.rect(win, (100, 149, 237), (25, 25, 150, 150))
second = pygame.draw.rect(win, (100, 149, 237), (200, 25, 150, 150))
third = pygame.draw.rect(win, (100, 149, 237), (375, 25, 150, 150))
fourth = pygame.draw.rect(win, (100, 149, 237), (25, 200, 150, 150))
fifth = pygame.draw.rect(win, (100, 149, 237), (200, 200, 150, 150))
sixth = pygame.draw.rect(win, (100, 149, 237), (375, 200, 150, 150))
seventh = pygame.draw.rect(win, (100, 149, 237), (25, 375, 150, 150))
eigth = pygame.draw.rect(win, (100, 149, 237), (200, 375, 150, 150))
ninth = pygame.draw.rect(win, (100, 149, 237), (375, 375, 150, 150))
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fill1 = True
fill2 = True
fill3 = True
fill4 = True
fill5 = True
fill6 = True
fill7 = True
fill8 = True
fill9 = True

circ1 = False
circ2 = False
circ3 = False
circ4 = False
circ5 = False
circ6 = False
circ7 = False
circ8 = False
circ9 = False

rect1 = False
rect2 = False
rect3 = False
rect4 = False
rect5 = False
rect6 = False
rect7 = False
rect8 = False
rect9 = False
game = True
i = 0
p = 0
run = True

cross = pygame.image.load(r'Tictactoe/cross.png')
cross = pygame.transform.scale(cross, (120,120))

click = True
while run:

    
    
    # pygame.time.delay(300)
    
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False
        if i % 2 == 0 and game:
            turn = pygame.image.load(r'Tictactoe/Your.png')
            turn = pygame.transform.scale(turn, (550, 70))
            win.blit(turn, (0, 540))
        elif i % 2 == 1 and game:
            turn = pygame.image.load(r'Tictactoe/Comp.png')
            turn = pygame.transform.scale(turn, (550, 70))
            win.blit(turn, (0, 540))

        if event.type == pygame.MOUSEBUTTONUP and game:
            pos = pygame.mouse.get_pos()
        
            if first.collidepoint(pos) and fill1:
                fill1 = False
                p = 1
                if i % 2 == 0:
                    win.blit(cross, (40, 40))
                    rect1 = True
                else:
                    pygame.draw.circle(win, (255, 255, 255), (100, 100), 60, 20)
                    circ1 = True

            elif second.collidepoint(pos) and fill2:
                fill2 = False
                p = 2
                if i % 2 == 0:
                    win.blit(cross, (215, 40))
                    rect2 = True
                else:
                    pygame.draw.circle(win, (255, 255, 255), (275, 100), 60, 20)
                    circ2 = True

            elif third.collidepoint(pos) and fill3:
                fill3 = False
                p = 3
                if i % 2 == 0:
                    win.blit(cross, (390, 40))
                    rect3 = True
                else:
                    pygame.draw.circle(win, (255, 255, 255), (450, 100), 60, 20)
                    circ3 = True

            elif fourth.collidepoint(pos) and fill4:
                fill4 = False
                p = 4
                if i % 2 == 0:
                    win.blit(cross, (40, 215))
                    rect4 = True
                else:
                    pygame.draw.circle(win, (255, 255, 255), (100, 275), 60, 20)
                    circ4 = True

            elif fifth.collidepoint(pos) and fill5:
                fill5 = False
                p = 5
                if i % 2 == 0:
                    win.blit(cross, (215, 215))
                    rect5 = True
                else:
                    pygame.draw.circle(win, (255, 255, 255), (275, 275), 60, 20)
                    circ5 = True

            elif sixth.collidepoint(pos) and fill6:
                fill6 = False
                p = 6
                if i % 2 == 0:
                    win.blit(cross, (390, 215))
                    rect6 = True
                else:
                    pygame.draw.circle(win, (255, 255, 255), (450, 275), 60, 20)
                    circ6 = True

            elif seventh.collidepoint(pos) and fill7:
                fill7 = False
                p = 7
                if i % 2 == 0:
                    win.blit(cross, (40, 390))
                    rect7 = True
                else:
                    pygame.draw.circle(win, (255, 255, 255), (100, 450), 60, 20)
                    circ7 = True

            elif eigth.collidepoint(pos) and fill8:
                fill8 = False
                p = 8
                
                if i % 2 == 0:
                    win.blit(cross, (215, 390))
                    rect8 = True
                else:
                    pygame.draw.circle(win, (255, 255, 255), (275, 450), 60, 20)
                    circ8 = True

            elif ninth.collidepoint(pos) and fill9:
                fill9 = False
                p = 9
                if i % 2 == 0:
                    win.blit(cross, (390, 390))
                    rect9 = True
                else:
                    pygame.draw.circle(win, (255, 255, 255), (450, 450), 60, 20)
                    circ9 = True
            else:
                click = False
        if keys[pygame.K_RETURN]:
            win.fill((10, 70, 105))
            first = pygame.draw.rect(win, (100, 149, 237), (25, 25, 150, 150))
            second = pygame.draw.rect(win, (100, 149, 237), (200, 25, 150, 150))
            third = pygame.draw.rect(win, (100, 149, 237), (375, 25, 150, 150))
            fourth = pygame.draw.rect(win, (100, 149, 237), (25, 200, 150, 150))
            fifth = pygame.draw.rect(win, (100, 149, 237), (200, 200, 150, 150))
            sixth = pygame.draw.rect(win, (100, 149, 237), (375, 200, 150, 150))
            seventh = pygame.draw.rect(win, (100, 149, 237), (25, 375, 150, 150))
            eigth = pygame.draw.rect(win, (100, 149, 237), (200, 375, 150, 150))
            ninth = pygame.draw.rect(win, (100, 149, 237), (375, 375, 150, 150))
            i=0
            fill1 = True
            fill2 = True
            fill3 = True
            fill4 = True
            fill5 = True
            fill6 = True
            fill7 = True
            fill8 = True
            fill9 = True
            circ1 = False
            circ2 = False
            circ3 = False
            circ4 = False
            circ5 = False
            circ6 = False
            circ7 = False
            circ8 = False
            circ9 = False
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            game = True
            rect1 = False
            rect2 = False
            rect3 = False
            rect4 = False
            rect5 = False
            rect6 = False
            rect7 = False
            rect8 = False
            rect9 = False
            game = True
        if (rect1 == True and rect2 == True and rect3 == True) or (circ1 == True and circ2 == True and circ3):
            pygame.draw.line(win, (0, 0, 0), (15, 100), (535, 100), width=15)
            game = False
            if circ1:
                turn = pygame.image.load(r'Tictactoe/uloose.png')
            else:
                turn = pygame.image.load(r'Tictactoe/uwin.png')
            turn = pygame.transform.scale(turn, (550, 70))
            win.blit(turn, (0, 540))
            end=True
        if (rect1 and rect4 and rect7) or (circ1 and circ4 and circ7):
            pygame.draw.line(win, (0, 0, 0), (100, 15), (100, 535), width=15)
            game = False
            if circ1:
                turn = pygame.image.load(r'Tictactoe/uloose.png')
            else:
                turn = pygame.image.load(r'Tictactoe/uwin.png')
            turn = pygame.transform.scale(turn, (550, 70))
            win.blit(turn, (0, 540))
            end=True
        if (rect1 and rect5 and rect9) or (circ1 and circ5 and circ9):
            pygame.draw.line(win, (0, 0, 0), (15, 15), (535, 535), width=20)
            game = False
            if circ1:
                turn = pygame.image.load(r'Tictactoe/uloose.png')
            else:
                turn = pygame.image.load(r'Tictactoe/uwin.png')
            turn = pygame.transform.scale(turn, (550, 70))
            win.blit(turn, (0, 540))
            end=True
        if (rect2 and rect5 and rect8) or (circ2 and circ5 and circ8):
            pygame.draw.line(win, (0, 0, 0), (275, 15), (275, 535), width=15)
            game = False
            if circ2:
                turn = pygame.image.load(r'Tictactoe/uloose.png')
            else:
                turn = pygame.image.load(r'Tictactoe/uwin.png')
            turn = pygame.transform.scale(turn, (550, 70))
            win.blit(turn, (0, 540))
            end=True
        if (rect3 and rect6 and rect9) or (circ3 and circ6 and circ9):
            pygame.draw.line(win, (0, 0, 0), (450, 15), (450, 535), width=15)
            game = False
            if circ3:
                turn = pygame.image.load(r'Tictactoe/uloose.png')
            else:
                turn = pygame.image.load(r'Tictactoe/uwin.png')
            turn = pygame.transform.scale(turn, (550, 70))
            win.blit(turn, (0, 540))
            end=True
        if (rect5 and rect4 and rect6) or (circ5 and circ4 and circ6):
            pygame.draw.line(win, (0, 0, 0), (15, 275), (535, 275), width=15)
            game = False
            if circ5:
                turn = pygame.image.load(r'Tictactoe/uloose.png')
            else:
                turn = pygame.image.load(r'Tictactoe/uwin.png')
            turn = pygame.transform.scale(turn, (550, 70))
            win.blit(turn, (0, 540))
            end=True
        if (rect8 and rect9 and rect7) or (circ8 and circ9 and circ7):
            pygame.draw.line(win, (0, 0, 0), (15, 450), (535, 450), width=15)
            game = False
            if circ8:
                turn = pygame.image.load(r'Tictactoe/uloose.png')
            else:
                turn = pygame.image.load(r'Tictactoe/uwin.png')
            turn = pygame.transform.scale(turn, (550, 70))
            win.blit(turn, (0, 540))
            end = True
        if (rect5 and rect3 and rect7) or (circ5 and circ3 and circ7):
            pygame.draw.line(win, (0, 0, 0), (15, 535), (535, 15), width=20)
            game = False
            if circ5:
                turn = pygame.image.load(r'Tictactoe/uloose.png')
            else:
                turn = pygame.image.load(r'Tictactoe/uwin.png')
            turn = pygame.transform.scale(turn, (550, 70))
            win.blit(turn, (0, 540))
            end=True
        

            #AI
        if event.type == pygame.MOUSEBUTTONUP and game and click:
            
            if p in x and len(x)-1 > 0:
                
                x.remove(p)
            
                y = random.choice(x)
                if y == 1 and fill1:
                    
                    pygame.draw.circle(win, (255, 255, 255), (100, 100), 60, 20)
                    circ1 = True
                    fill1 = False
                if y == 2 and fill2:
                    pygame.draw.circle(win, (255, 255, 255), (275, 100), 60, 20)
                    circ2 = True
                    fill2 = False
                if y == 3 and fill3:
                    pygame.draw.circle(win, (255, 255, 255), (450, 100), 60, 20)
                    circ3 = True
                    fill3 = False
                if y == 4 and fill4:
                    pygame.draw.circle(win, (255, 255, 255), (100, 275), 60, 20)
                    circ4 = True
                    fill4 = False
                if y == 5 and fill5:
                    pygame.draw.circle(win, (255, 255, 255), (275, 275), 60, 20)
                    circ5 = True
                    fill5 = False
                if y == 6 and fill6:
                    pygame.draw.circle(win, (255, 255, 255), (450, 275), 60, 20)
                    circ6 = True
                    fill6 = False
                if y == 7 and fill7:
                    pygame.draw.circle(win, (255, 255, 255), (100, 450), 60, 20)
                    circ7 = True
                    fill7 = False
                if y == 8 and fill8:
                    pygame.draw.circle(win, (255, 255, 255), (275, 450), 60, 20)
                    circ8 = True
                    fill8 = False
                if y == 9 and fill9:
                    pygame.draw.circle(win, (255, 255, 255), (450, 450), 60, 20)
                    circ9 = True
                    fill9 = False
                x.remove(y)
            elif len(x) == 1:
                turn = pygame.image.load(r'Tictactoe/draw.png')
                turn = pygame.transform.scale(turn, (550, 70))
                win.blit(turn, (0, 540))
                game = False

    font = pygame.font.SysFont('calibri', 17, False, False)
    press = font.render("PRESS  ", False, (255, 255, 255))
    win.blit(press, (10, 620))

    restart = pygame.image.load(r'Tictactoe/enter-key.png')
    restart = pygame.transform.scale(restart, (25, 25))
    win.blit(restart, (64, 615))

    res = font.render("  TO RESTART", False, (255, 255, 255))
    win.blit(res, (90, 620))

    click = True
    pygame.display.update()
    

pygame.quit()
