import pygame

from Game import Game
from Sprite import Sprite
from Font import Font
from Scene import Scene
from Event import Event
from Utils import WindowSize, Color
from File import JsonFile

import TitleScene

class ScoreScene(Scene):
    def __init__(self):
        super().__init__()

        self.background = None

    def Init(self):
        super().Init()

        Event.AddCallback(self.EventHandler)

        self.background = Sprite('background-image', "score_background.jpg")
        self.background.SetPosition(WindowSize[0]/2, WindowSize[1]/2)
        self.background.SetLayer(0)

        file = JsonFile("score")
        file.Load()
        data = file.jsonData

        if 'scores' in data:
            scoreList = data['scores']
            for i in range(len(scoreList)):
                name = scoreList[i][0]
                score = scoreList[i][1]

                scoreFont = Font('ready','nago.ttf',60,str(name) + " : " + str(score))
                scoreFont.SetPosition(WindowSize[0]/2, WindowSize[1] * (0.1 * i + 0.3))
                scoreFont.SetLayer(10)
            
                self.AddObject(scoreFont)
        else:
            noneScoreFont = Font('ready','nago.ttf',60,"아직 기록이 없습니다!")
            noneScoreFont.SetPosition(WindowSize[0]/2, WindowSize[1]/2)
            noneScoreFont.SetLayer(10)
            self.AddObject(noneScoreFont)

        scoreTitleFont = Font('ready','nago.ttf',60,"점수", Color.BLACK)
        scoreTitleFont.SetPosition(WindowSize[0]/2, WindowSize[1] * 0.1)
        scoreTitleFont.SetLayer(10)
        self.AddObject(scoreTitleFont)

        self.AddObject(self.background)

    def EventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Game.Instance().ChangeScene(TitleScene.TitleScene())
