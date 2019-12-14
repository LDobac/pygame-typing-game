'''
    Sprite.py
    이미지를 출력하는 Sprite 구현 클래스
'''

import os
import pygame

from Object import Object
from Utils import GetResources

# Scene에 띄어져야 하므로 Object 상속
class Sprite(Object):
    def __init__(self,name,fileName):
        super().__init__(name)

        '''
            pygame image load 함수를 사용한다.
            이미지 변형 함수를 사용하려면 무변형 이미지가 필요하므로 원본 이미지를 따로 저장한다.
        '''
        self.originImage = pygame.image.load(GetResources(fileName))

        # 변형이미지, 원본 이미지를 복사해 사용한다.
        self.image = self.originImage.copy()
        # 이미지가 띄어질 크기 지정
        self.rect = self.image.get_rect()

        # 이미지에 변형이 일어났을 때 새 이미지를 생성하도록 하는 플래그
        self.isImageUpdate = False

    '''
        Sprite를 그리는 함수
        이미지에 변형이 있을 경우 새 이미지를 생성해 반환한다.
        Scene에서 해당 이미지를 그릴 수 있게 image와 rect를 반환한다
    '''
    def Draw(self):
        if self.isImageUpdate == True:
            self.image = pygame.transform.rotozoom(self.originImage, self.angle, self.scale)
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            self.isImageUpdate = False

        return (self.image, self.rect)

    # 이미지 위치 변경
    def SetPosition(self, x, y):
        super().SetPosition(x, y)
        self.rect.center = (self.x,self.y)

    # 이미지 회전값 변경
    def SetRotation(self,angle):
        super().SetRotation(angle)
        self.isImageUpdate = True

    # 이미지 크기 변경
    def SetScale(self,scale):
        super().SetScale(scale)
        self.isImageUpdate = True