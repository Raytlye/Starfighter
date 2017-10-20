import sys
import os

if getattr(sys, 'frozen', False):
    CurrentPath = sys._MEIPASS

else:
    CurrentPath = os.path.dirname(__file__)

imageFolderPath = os.path.join(CurrentPath, 'images')

asteroidImg = pygame.image.load(path.join(imageFolderPath, 'asteroid.png'))
backgroundImg = pygame.image.load(path.join(imageFolderPath, 'background.jpg'))
icon = pygame.image.load(path.join(imageFolderPath, 'StarFighterBigIcon.png'))
starfighterImg = pygame.image.load(path.join(imageFolderPath, 'x_wing.png'))
