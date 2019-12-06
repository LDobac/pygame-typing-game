from WordGenerator import WordGenerator
from Game import Game

from TitleScene import TitleScene

game = Game.Instance()

titleScene = TitleScene()
game.Init(titleScene)

while True:
    game.Loop()