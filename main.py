import pygame
from datetime import datetime
import webbrowser

pygame.init()
app_screen = pygame.display.set_mode((380, 650))
pygame.display.set_caption('Home')
logo = pygame.image.load(r'widgets/adisa.png')
logo = pygame.transform.scale(logo, (200, 112))
def ti():
    date = datetime.date
    now = datetime.now()
    time = now.strftime("%H:%M")
    date_today = now.date()
    date_today = date_today.strftime("%b %d")
    day = now.strftime("%a")

    font = pygame.font.SysFont('times new roman', 17, True, False)
    time_str = str(now.strftime("%H:%M"))
    text = font.render(time_str, True, (255, 255, 255))
    app_screen.blit(text, (10, 4))
    # (255, 255, 255)
    # (0, 0, 0)
    font = pygame.font.SysFont('calibiri', 60)
    text = font.render(time_str, True, (255, 255, 255))
    app_screen.blit(text, (235, 480))

    font = pygame.font.SysFont('calibiri', 34)
    text = font.render(day, True, (255, 255, 255))
    app_screen.blit(text, (30, 480))

    font = pygame.font.SysFont('calibiri', 34)
    text = font.render(date_today, True, (255, 255, 255))
    app_screen.blit(text, (30, 500))

    return 0


cl = pygame.draw.rect(app_screen, (0, 0, 0), (235, 480, 110, 40))
calculator = pygame.image.load(r'widgets/calculator-icon.png')
calculator = pygame.transform.scale(calculator, (60, 60))
rcal = pygame.draw.rect(app_screen, (255, 255, 255), (120, 550, 40, 60))

clock = pygame.image.load(r'widgets/clock.png')
clock = pygame.transform.scale(clock, (60, 60))
rclock = pygame.draw.rect(app_screen, (255, 255, 255), (30, 550, 60, 60))

music = pygame.image.load(r'widgets/musicicon2.png')
music = pygame.transform.scale(music, (50, 60))
rmusic = pygame.draw.rect(app_screen, (255, 255, 255), (30, 380, 50, 60))

notepad = pygame.image.load(r'widgets/Notepadicon1.png')
notepad = pygame.transform.scale(notepad, (60, 60))
rnote = pygame.draw.rect(app_screen, (255, 255, 255), (290, 544, 60, 55))

game = pygame.image.load(r'widgets/tictactoeicon2.png')
game = pygame.transform.scale(game, (60, 60))
rgame = pygame.draw.rect(app_screen, (255, 255, 255), (280, 380, 60, 60))


net = pygame.image.load(r'widgets/net.png')
net = pygame.transform.scale(net, (25, 25))

weather = pygame.image.load(r'widgets/weather.png')
weather = pygame.transform.scale(weather, (60, 60))
weath = pygame.draw.rect(app_screen, (255, 255, 255), (210, 547, 50, 50))

g = pygame.image.load(r'widgets/4g.png')
g = pygame.transform.scale(g, (25, 25))

wallpaper = pygame.image.load(r'widgets/wallpaper13.png')
wallpaper = pygame.transform.scale(wallpaper, (400, 900))


# wallpaper = pygame.draw.rect(app_screen, (0, 0, 0), (0, 0, 400, 650))

search = pygame.image.load(r'widgets/searchbar.png')
search = pygame.transform.scale(search, (330, 65))

# pygame.draw.rect(app_screen, (200, 200, 200), (0, 0, 400, 25))
searchbar = pygame.draw.rect(app_screen, (0, 0, 0), (35, 70, 310, 43))


def bl():
    app_screen.blit(wallpaper, (0, 0))
    app_screen.blit(logo, (90, 150))
    app_screen.blit(calculator, (120, 550))
    app_screen.blit(clock, (30, 550))
    app_screen.blit(notepad, (290, 544))

    app_screen.blit(game, (280, 380))
    app_screen.blit(music, (30, 380))

    app_screen.blit(net, (325, 0))
    app_screen.blit(g, (350, -1))
    app_screen.blit(search, (25, 60))

    app_screen.blit(weather, (210, 547))

    ti()
    return 0


bl()


def tic():
    import tictactoe


def note():
    import notepad


def mus():
    import Music_player


def clo():
    import alarmclock


def cal():
    import Calculator


run = True


ti()


pygame.display.update()

while run:
    pygame.time.set_timer(100, bl())
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if rgame.collidepoint(pos):
                pos = (0, 0)
                tic()
            if rnote.collidepoint(pos):
                pos = (0, 0)
                note()
            if rmusic.collidepoint(pos):
                pos = (0, 0)
                mus()

            if rclock.collidepoint(pos):
                pos = (0, 0)
                clo()
            if rcal.collidepoint(pos):
                pos = (0, 0)
                cal()
            if rgame.collidepoint(pos):
                run = False

            if searchbar.collidepoint(pos):
                webbrowser.open(r'https://google.com/')

            if weath.collidepoint(pos):
                webbrowser.open(r'https://weather.com/en-IN/weather/today/l/ef9f1493b5b13e4670d9fa9b79e8d11258c08d37aad'
                                r'4705cbdff135a602c98d4')

            if cl.collidepoint((pos)):
                clo()

            else:
                pygame.display.update()
pygame.quit()
