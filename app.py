'''
    app.py
    게임을 실행한다.
'''

from Game import Game

from TitleScene import TitleScene

if __name__ == "__main__":
    game = Game.Instance()

    titleScene = TitleScene()
    game.Init(titleScene)

    while True:
        game.Loop()