import pygame

from Event import Event
from Game import Game
from Scene import Scene
from TestSprite import TestSprite
from TestScene2 import TestScene2

from File import JsonFile

class TestScene(Scene):

    def EventCallback(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                Game.Instance().ChangeScene(TestScene2(), {'A' : 'Hello'})

    def __init__(self):
        super().__init__()

        self.ball1 = TestSprite()
        self.ball1.SetLayer(1)
        self.ball1.SetScale(0.2)

        self.ball2 = TestSprite()
        self.ball2.SetLayer(2)
        self.ball2.SetScale(0.4)

        self.ball3 = TestSprite()
        self.ball3.SetLayer(3)
        self.ball3.SetScale(0.6)

        self.ball4 = TestSprite()
        self.ball4.SetLayer(4)
        self.ball4.SetScale(0.8)

        self.ball5 = TestSprite()
        self.ball5.SetLayer(5)
        self.ball5.SetScale(1.0)

        self.AddObject(self.ball1)
        self.AddObject(self.ball2)
        self.AddObject(self.ball3)
        self.AddObject(self.ball4)
        self.AddObject(self.ball5)

        self.file = JsonFile("testfile")
        self.file.Load()
        print(self.file.jsonData)
        self.file.jsonData = {
            'a' : 'hello',
            'b' : 'bello',
            'c' : 'cello'
        }
        self.file.Save()

    def Init(self):
        super().Init()

        Event.AddCallback(self.EventCallback)