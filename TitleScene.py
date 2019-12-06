import pygame
import sys

from Game import Game
from Sprite import Sprite
from Font import Font
from Scene import Scene
from Event import Event
from Utils import WindowSize

from GameScene import GameScene
from ScoreScene import ScoreScene

class TitleScene(Scene):
    def __init__(self):
        super().__init__()

        self.arrowCursor = None 
        self.background = None

        self.titleFont = None
        self.startMenuFont = None
        self.scoreMenuFont = None

        self.selectMenu = 1

    def __del__(self):
        Event.RemoveCallback(self.EventHandler)

    def Init(self):
        super().Init()

        Event.AddCallback(self.EventHandler)

        self.arrow = Sprite('arrow-cursor',"arrow.png")
        self.arrow.SetPosition(WindowSize[0] * 0.4, WindowSize[1] * 0.6)
        self.arrow.SetScale(0.1)
        self.arrow.SetLayer(2)

        self.background = Sprite('background-image', "title_background.jpg")
        self.background.SetPosition(WindowSize[0]/2, WindowSize[1]/2)
        self.background.SetLayer(0)

        self.titleFont = Font('start-menu','nago.ttf',80,"-게임-")
        self.titleFont.SetPosition(WindowSize[0]/2, WindowSize[1] * 0.2)
        self.titleFont.SetLayer(2)

        self.startMenuFont = Font('start-menu','nago.ttf',45,"게임 시작")
        self.startMenuFont.SetPosition(WindowSize[0]/2, WindowSize[1] * 0.6)
        self.startMenuFont.SetLayer(2)

        self.scoreMenuFont = Font('score-menu','nago.ttf',45,"스코어")
        self.scoreMenuFont.SetPosition(WindowSize[0]/2, WindowSize[1] * 0.75)
        self.scoreMenuFont.SetLayer(2)

        self.AddObject(self.arrow)
        self.AddObject(self.background)
        self.AddObject(self.titleFont)
        self.AddObject(self.startMenuFont)
        self.AddObject(self.scoreMenuFont)

    def EventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.selectMenu == 2:
                self.selectMenu = 1
                self.arrow.SetY(WindowSize[1] * 0.6)
            elif event.key == pygame.K_DOWN and self.selectMenu == 1:
                self.selectMenu = 2
                self.arrow.SetY(WindowSize[1] * 0.75)
            elif event.key == pygame.K_RETURN:
                if self.selectMenu == 1:
                    Game.Instance().ChangeScene(GameScene())
                elif self.selectMenu == 2:
                    Game.Instance().ChangeScene(ScoreScene())
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
