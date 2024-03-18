import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((900,900),pygame.RESIZABLE)
done=True
fon=pygame.image.load("image/mickey.png")
rigthhand=pygame.image.load("image/mickeyright.png")
lefthand=pygame.image.load("image/mickeyleft.png")
while done:
        now = datetime.datetime.now()
        min= now.minute *6
        sec = now.second * 6 
        rotaterigth=pygame.transform.rotate(rigthhand,-min)
        rotateleft=pygame.transform.rotate(lefthand,-sec)
        screen.blit(fon, fon.get_rect(center = screen.get_rect().center))

        screen.blit(rotaterigth, rotaterigth.get_rect(center=(450,450)))
        screen.blit(rotateleft, rotateleft.get_rect(center=(450,450)))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done=False
                        pygame.quit()

#EX2
pygame.init()
pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
musics = ['music/music.mp3',
        'music/Murashki.mp3',
        'music/mercedes.mp3']
w = 800
h = 800
nextsong = 0
clock = pygame.time.Clock()
pause = False
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Music")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pause = True
                pygame.mixer.music.load(musics[nextsong])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                nextsong -= 1
                if nextsong == -1:
                    nextsong = len(musics) - 1
                pygame.mixer.music.load(musics[nextsong])
                pygame.mixer.music.play()

            elif event.key == pygame.K_RIGHT:
                nextsong += 1
                if nextsong == len(musics):
                    nextsong = 0
                pygame.mixer.music.load(musics[nextsong])
                pygame.mixer.music.play()

            elif event.key == pygame.K_SPACE and pause == False:
                pause = True
                pygame.mixer.music.pause()

            elif event.key == pygame.K_SPACE and pause == True:
                pause = False
                pygame.mixer.music.unpause()
    pygame.display.flip()
    clock.tick(60)
#EX3
pygame.init()
w = 600
h = 600
sc = pygame.display.set_mode((w,h), pygame.RESIZABLE)
pygame.display.set_caption("Red circle")
clock = pygame.time.Clock()
FPS = 60
x = w // 2
y = h //2
speed = 20
white = (255,255,255)
flLeft = flRight = False
flup = fldown = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
            elif event.key == pygame.K_UP:
                flup = True
            elif event.key == pygame.K_DOWN:
                fldown = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]:
                flLeft = flRight = fldown = flup = False
                
    if flLeft:
        x -= speed
    elif flRight:
        x += speed
    elif flup:
        y -= speed
    elif fldown:
        y+=speed
        
    sc.fill(white)
    pygame.draw.circle(sc, (255,0,0),(x,y), 50)
    pygame.display.update()
    clock.tick(FPS)
