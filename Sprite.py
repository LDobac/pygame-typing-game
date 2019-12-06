import os
import pygame

from Object import Object
from Utils import GetResources

class Sprite(Object):
    def __init__(self,name,fileName):
        super().__init__(name)

        self.originImage = pygame.image.load(GetResources(fileName))

        self.image = self.originImage.copy()
        self.rect = self.image.get_rect()

        self.isImageUpdate = False

    def Draw(self):

        if self.isImageUpdate == True:
            self.image = pygame.transform.rotozoom(self.originImage, self.angle, self.scale)
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            self.isImageUpdate = False

        return (self.image, self.rect)

    def SetPosition(self, x, y):
        super().SetPosition(x, y)
        self.rect.center = (self.x,self.y)

    def SetRotation(self,angle):
        super().SetRotation(angle)
        self.isImageUpdate = True

    def SetScale(self,scale):
        super().SetScale(scale)
        self.isImageUpdate = True