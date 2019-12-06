import pygame
import os

from Object import Object
from Utils import Color

class Font(Object):
    def __init__(self, name, ttfPath, fontSize = 12 ,text="", color=Color.WHITE, antialias=True):
        super().__init__(name)

        self.fontSize = fontSize
        self.font = pygame.font.Font(''.join(["Resources/", ttfPath]), fontSize)

        self.text = text
        self.color = color
        self.isAntialias = antialias

        self.image = self.font.render(self.text,self.isAntialias,self.color)
        self.rect  = self.image.get_rect()
        
        self.isFontChange = False

    def Draw(self):
        if self.isFontChange == True:
            fontImage = self.font.render(self.text,self.isAntialias,self.color)
            self.image = pygame.transform.rotozoom(fontImage, self.angle, self.scale)
            self.rect  = self.image.get_rect()
            self.rect.center = (self.x,self.y)

            self.isFontChange = False

        return (self.image, self.rect)

    def SetPosition(self, x, y):
        super().SetPosition(x, y)
        self.rect.center = (self.x,self.y)

    def SetRotation(self,angle):
        super().SetRotation(angle)
        self.isFontChange = True

    def SetScale(self,scale):
        super().SetScale(scale)
        self.isFontChange = True

    def SetColor(self, color):
        self.color = color
        self.isFontChange = True

    def SetText(self, newText):
        self.text = newText

        self.isFontChange = True
    
    def GetText(self):
        return self.text