import pygame

from Game import Game
from Sprite import Sprite
from Font import Font
from Scene import Scene
from Event import Event
from Utils import WindowSize, Color
from File import JsonFile

import TitleScene

class ResultScene(Scene):
    def __init__(self):
        super().__init__()

        self.background = None

        self.scoreFont = None
        self.nameFont = None

    def Init(self):
        super().Init()

        Event.AddCallback(self.EventHandler)

        self.background = Sprite('background-image', "score_background.jpg")
        self.background.SetPosition(WindowSize[0]/2, WindowSize[1]/2)
        self.background.SetLayer(0)

        self.scoreFont = Font('ready','nago.ttf',60,"Your Score : " + str(self.data['score']) + " !")
        self.scoreFont.SetPosition(WindowSize[0]/2, WindowSize[1]/2)
        self.scoreFont.SetLayer(10)

        self.nameFont = Font('answer','nago.ttf',40,"",Color.BLACK)
        self.nameFont.SetPosition(WindowSize[0]/2, WindowSize[1] * 0.7 )
        self.nameFont.SetLayer(5)

        self.AddObject(self.background)
        self.AddObject(self.scoreFont)
        self.AddObject(self.nameFont)

    def EventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.nameFont.SetText(self.nameFont.GetText()[:-1])
            elif event.key == pygame.K_RETURN:
                
                name = self.nameFont.GetText()

                file = JsonFile("score")
                file.Load()
                data = file.jsonData

                if 'scores' in data:
                    data['scores'].insert(0, [name,self.data['score']])
                    data['scores'].sort(key=lambda score: score[1], reverse=True)

                    data['scores'] = data['scores'][:min(len(data['scores']), 6)]
                else:
                    data['scores'] = [[name, self.data['score']]]
                
                file.Save()
                
                Game.Instance().ChangeScene(TitleScene.TitleScene())
            elif event.unicode != '':
                newText = self.nameFont.GetText() + event.unicode
                self.nameFont.SetText(newText)

