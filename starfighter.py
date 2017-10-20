import pygame
import time
import random
import shelve

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

starfighter_width = 160

highscore = 0
icon = pygame.image.load('images/StarFighterBigIcon.png')
icon = pygame.transform.scale(icon, (32,32))
pygame.display.set_icon(icon)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Starfighter')
clock = pygame.time.Clock()

backgroundImg = pygame.image.load('images/background.jpg')

asteroidImg = pygame.image.load('images/asteroid.png')
asteroidImg = pygame.transform.scale(asteroidImg, (100,100))

starfighterImg = pygame.image.load('images/x_wing.png')
starfighterImg = pygame.transform.scale(starfighterImg, (160, 100))

def save_score(score):
    d = shelve.open('score.txt')
    if score > d['score']:
        d['score'] = score
    
    d.close()

def get_highscore():
    d = shelve.open('score.txt')
    global highscore
    if d['score']:
        highscore = d['score']
    d.close()

def display_highscore():
    global highscore
    font = pygame.font.SysFont(None, 25)
    text = font.render("Highscore: " + str(highscore), True, white)
    gameDisplay.blit(text,(660, 0))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, white)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy):
    gameDisplay.blit(asteroidImg, (thingx, thingy))

def starfighter(x,y):
    gameDisplay.blit(starfighterImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',85)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('Crashed you have')

def pause():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                
        largeText = pygame.font.Font('freesansbold.ttf',85)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                intro = False
                
        gameDisplay.blit(backgroundImg, (0,0))
        largeText = pygame.font.Font('freesansbold.ttf',85)
        TextSurf, TextRect = text_objects("Starfighter", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        smallText = pygame.font.Font('freesansbold.ttf',35)
        TextSurf, TextRect = text_objects("Press any key", smallText)
        TextRect.center = ((display_width/2),(display_height/2 + 50))

        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    get_highscore()

    global paused

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_ESCAPE:
                    pause()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.blit(backgroundImg, (0,0))

        things(thing_startx, thing_starty)
        thing_starty += thing_speed
        starfighter(x,y)
        things_dodged(dodged)
        display_highscore()

        if x > display_width - starfighter_width or x < 0:
            save_score(dodged)
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.3

        if y < thing_starty + thing_height:

            if x + starfighter_width > thing_startx and x < thing_startx + thing_width:
                save_score(dodged)
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
