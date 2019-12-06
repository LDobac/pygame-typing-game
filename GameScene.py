import pygame
import random

from Game import Game
from Sprite import Sprite
from Font import Font
from Scene import Scene
from Event import Event
from Utils import WindowSize, Color
from WordGenerator import WordGenerator

import TitleScene
import ResultScene

class GameScene(Scene):
    def __init__(self):
        super().__init__()

        self.background = None
        self.generator = None

        self.stateFont = None
        self.answerFont = None
        self.scoreFont = None

        self.wordDrops = []

        self.preStart = True
        self.readyDuration = 2
        self.goDuration = 0.5
        self.gameoverDuration = 1.5

        self.timer = 0

        self.score = 0
        self.gameOver = False

    def __del__(self):
        Event.RemoveCallback(self.EventHandler)

    def Init(self):
        super().Init()

        Event.AddCallback(self.EventHandler)

        self.generator = WordGenerator()

        self.background = Sprite('background-image', "game_background.jpg")
        self.background.SetPosition(WindowSize[0]/2, WindowSize[1]/2)
        self.background.SetLayer(0)

        self.stateFont = Font('ready','nago.ttf',60,"Ready...")
        self.stateFont.SetPosition(WindowSize[0]/2, WindowSize[1]/2)
        self.stateFont.SetLayer(10)

        self.answerFont = Font('answer','nago.ttf',40,"",Color.BLACK)
        self.answerFont.SetPosition(WindowSize[0]/2, WindowSize[1] * 0.9 )
        self.answerFont.SetLayer(5)

        self.scoreFont = Font('word','nago.ttf', 30, "Score : ",Color.BLACK)
        self.scoreFont.SetLayer(15)
        self.scoreFont.SetPosition(self.scoreFont.rect.width//2 + 10, self.scoreFont.rect.height//2)

        self.AddObject(self.background)
        self.AddObject(self.stateFont)
        self.AddObject(self.answerFont)
        self.AddObject(self.scoreFont)

    def Update(self,deltaTime):
        super().Update(deltaTime)

        self.scoreFont.SetText("Score : " + str(self.score))

        if self.preStart:
            if (self.timer > self.readyDuration) and (self.timer < self.readyDuration + self.goDuration):
                self.stateFont.SetText("Go!")
            elif self.timer > self.readyDuration + self.goDuration:
                self.stateFont.SetPosition(-WindowSize[0]/2, -WindowSize[1]/2)
                self.stateFont.SetText("")
                self.preStart = False

                self.GenerateWordRain()

            self.timer += deltaTime
        elif not self.preStart and not self.gameOver:
            for wordDrop in self.wordDrops:
                wordFont = wordDrop[0]
                speed = wordDrop[1]

                wordFont.SetY(wordFont.GetY() + speed * deltaTime)

                if(wordFont.GetY() > WindowSize[1]*1.1):
                    self.gameOver = True
                    self.timer = 0

            if len(self.wordDrops) < 5:
                self.GenerateWordRain()
        elif self.gameOver:
            self.stateFont.SetPosition(WindowSize[0]/2, WindowSize[1]/2)
            self.stateFont.SetText("GameOver!")

            if self.timer > self.gameoverDuration:
                Game.Instance().ChangeScene(ResultScene.ResultScene(),{'score' : self.score})
            self.timer += deltaTime

    def EventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Game.Instance().ChangeScene(TitleScene.TitleScene())
            elif event.key == pygame.K_BACKSPACE:
                self.answerFont.SetText(self.answerFont.GetText()[:-1])
            elif event.key == pygame.K_RETURN:
                answer = self.answerFont.GetText()
                self.answerFont.SetText('')

                self.CheckAnswer(answer)
            elif event.unicode != '':
                newText = self.answerFont.GetText() + event.unicode
                self.answerFont.SetText(newText)

            if event.key == pygame.K_DOWN:
                Game.Instance().ChangeScene(ResultScene.ResultScene(),{'score' : self.score})
            elif event.key == pygame.K_UP:
                self.score += 1

    def GenerateWordRain(self):
        wordList = self.generator.GetWord(10)
        for word in wordList:
            font = self.WordToFontRain(word)
            self.AddObject(font)

            speed = random.randint(10,60)
            self.wordDrops.insert(0, [font,speed])

    def WordToFontRain(self, word):
        newFont = Font('word','nago.ttf', 30, word,Color.BLACK)
        newFont.SetLayer(2)

        newFont.SetPosition(
            random.randint(newFont.rect.width//2, WindowSize[0] - newFont.rect.width//2),
            random.randint(-100, -10)
        )

        return newFont

    def CheckAnswer(self, answer):
        for wordDrop in self.wordDrops:
            if wordDrop[0].GetText() == answer:
                self.wordDrops.remove(wordDrop)
                self.RemoveObject(wordDrop[0])

                self.score += 1

                return True

        return False
        