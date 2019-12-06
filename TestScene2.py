import pygame
from pygame.mixer import music, Sound
import random
import math

import Game
from Event import Event
from Utils import GetResources
from Sprite import Sprite
from Font import Font
from Scene import Scene

class TestScene2(Scene):
    def __init__(self):
        super().__init__()

        self.frameText = Font('framerate_text','nago.ttf',15)
        self.AddObject(self.frameText)

        self.text = Font('font','nago.ttf',50,text="Test Text")
        self.AddObject(self.text)

        self.text.SetPosition(Game.WindowSize[0] / 2, Game.WindowSize[1] / 2)
        self.text.SetRotation(45)

        self.effect = None

    def Init(self):
        super().Init()

        Event.AddCallback(self.EventCallback)
        print(self.data)

        music.load(GetResources("Yeah.wav"))
        music.play()

        self.effect = Sound(GetResources("explode.wav"))

    def Update(self, deltaTime):
        self.frameText.SetText(str(math.floor(Game.Game.Instance().clock.get_fps())))
        self.frameText.SetPosition(self.frameText.rect.width/2, self.frameText.rect.height/2)

        self.text.SetText(str(deltaTime))
        
    def EventCallback(self, event):
        dx = 0
        dy = 0
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy -= 10
            if event.key == pygame.K_DOWN:
                dy += 10
            if event.key == pygame.K_LEFT:
                dx -= 10
            if event.key == pygame.K_RIGHT:
                dx += 10
            if event.key == pygame.K_r:
                self.text.SetRotation(self.text.GetRotation() + 30)
            if event.key == pygame.K_s:
                self.text.SetScale(random.random() * 3)
            if event.key == pygame.K_c:
                self.text.SetColor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if event.key == pygame.K_BACKSPACE:
                self.text.SetText(self.text.GetText()[:-1])
            if event.key == pygame.K_RETURN:
                self.effect.play()
        
        (x, y) = self.text.GetPosition()
        self.text.SetPosition(x + dx, y + dy)

    
