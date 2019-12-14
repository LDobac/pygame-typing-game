'''
    Font.py
    화면에 글씨를 출력한다.
    ttf 포맷의 폰트를 사용할 수 있다.
'''

import pygame
import os

from Object import Object
from Utils import Color

class Font(Object):
    '''
        Params
            ttfPath : ttf포맷 파일 경로
            fontSize : 폰트 크기
            text : 출력할 텍스트
            color : 폰트 색상
            antialias : 안티얼라이징 효과 
    '''
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

    # 화면에 폰트를 그린다. 폰트 이미지에 변형시 새로 생성한다.
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