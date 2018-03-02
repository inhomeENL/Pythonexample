import pygame, sys
from pygame.locals import *
import time

pygame.init()
"""
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
RectObj = pygame.Rect(100, 50, 300, 250)
RectObj.center = (200, 150)
textRectObj = textSurfaceObj.get_rect()

while True:
    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF, GREEN, RectObj)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    textRectObj.center = (200, 80)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    textRectObj.center = (200, 150)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    textRectObj.center = (200, 200)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
"""

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption("Sound")

while True:
    soundObj = pygame.mixer.Sound("beep1.ogg")
    soundObj.play()
    time.sleep(1)
    soundObj.stop()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()