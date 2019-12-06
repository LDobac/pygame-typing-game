from Sprite import Sprite

import random

class TestSprite(Sprite):
    def __init__(self):
        super().__init__('test_ball','intro_ball.gif')
        
        self.SetPosition(random.randint(0, 320),random.randint(0, 480))

        self.rotationSpeed = random.random()
        self.move = [random.random() ,random.random()]

    def Update(self, deltaTime):
        super().Update(deltaTime)

        self.SetRotation(self.GetRotation() + self.rotationSpeed)
        
        if self.rect.left < 0:
            self.move[0] = random.random()
        elif self.rect.right > 320:
            self.move[0] = -random.random()
        elif self.rect.top < 0:
            self.move[1] = random.random()
        elif self.rect.bottom > 480:
            self.move[1] = -random.random()

        (x,y) = self.GetPosition()
        self.SetPosition(x + self.move[0], y + self.move[1])