'''
    Game.py
    
    게임을 실행, 이벤트를 처리하는 클래스
'''

import pygame
import sys

from Utils import Color, WindowSize
from Event import Event

'''
    Game 클래스 - Singletone 객체
'''
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

    # pygame으로 부터 화면의 surface를 생성한다.
    def Init(self, startScene):
        self.screen = pygame.display.set_mode(self.windowSize)

        # 시작할 Scene 초기화
        startScene.Init()
        self.curScene = startScene

    def Loop(self):
        
        # 게임의 1 frame 업데이트

        # 30fps 고정
        deltaTime = self.clock.tick(30)
        # pygame.clock.tick의 반환값은 millisecond 단위로 반환, second 단위로 변경
        deltaTime *= 0.001

        # update시 생기는 이벤트(화면, 키보드/마우스 등) 처리
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
            # Clear, 화면을 검은색으로 비운다
            self.screen.fill(Color.BLACK)

            # Update Scene
            self.curScene.Update(deltaTime)

            # Draw Scene
            self.curScene.Draw(self.screen)

            # Flip backbuffer, 백 버퍼에 그려진 그림을 프론트 버퍼로 flip 한다
            pygame.display.flip()

    # Scene 변경
    def ChangeScene(self, newScene, data=None):
        self.newScene = newScene
        self.newScene.data = data

        Event.ClearCallbacks()

    # 게임 일시 정지
    def Pause(self):
        self.onPause = True

    # 게임 재개
    def Resume(self):
        self.onPause = False