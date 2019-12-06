import pygame
import sys

from Utils import Color, WindowSize
from Event import Event

class Game:

    _instance = None

    def Instance():
        if Game._instance == None:
            Game._instance = Game(WindowSize)
        
        return Game._instance

    def __init__(self, size):
        pygame.init()
        
        self.windowSize = size
        
        self.screen = None
        self.clock = pygame.time.Clock()

        self.curScene = None
        self.newScene = None

        self.onPause = False

    def Init(self, startScene):
        self.screen = pygame.display.set_mode(self.windowSize)

        startScene.Init()
        self.curScene = startScene

    def Loop(self):
        
        deltaTime = self.clock.tick(30)
        deltaTime *= 0.001

        for event in pygame.event.get():
            Event.RaiseEvent(event)
            if event.type == pygame.QUIT:
                sys.exit()

        # Scene Change
        if self.newScene != None:
            self.curScene.Close()
            self.newScene.Init()
            self.curScene = self.newScene
            self.newScene = None

        if not self.onPause:
            # Clear
            self.screen.fill(Color.BLACK)

            # Update Scene
            self.curScene.Update(deltaTime)

            # Draw Scene
            self.curScene.Draw(self.screen)

            # Flip backbuffer
            pygame.display.flip()

    def ChangeScene(self, newScene, data=None):
        self.newScene = newScene
        self.newScene.data = data

        Event.ClearCallbacks()

    def Pause(self):
        self.onPause = True

    def Resume(self):
        self.onPause = False