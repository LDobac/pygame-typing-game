class Object:
    def __init__(self, name):
        self.name = name

        self.layer = 0

        self.x = 0
        self.y = 0
        self.angle = 0
        self.scale = 1

    def Update(self, deltaTime):
        pass

    def Draw(self):
        pass

    def SetLayer(self, layer):
        self.layer = layer
    
    def GetLayer(self):
        return self.layer

    def SetPosition(self, x, y):
        self.x = x
        self.y = y

    def GetPosition(self):
        return (self.x,self.y)

    def SetX(self, x):
        self.SetPosition(x, self.y)

    def GetX(self):
        return self.x

    def SetY(self, y):
        self.SetPosition(self.x, y)
    
    def GetY(self):
        return self.y

    def SetRotation(self,angle):
        self.angle = angle

    def GetRotation(self):
        return self.angle

    def SetScale(self,scale):
        self.scale = scale
    
    def GetScale(self):
        return self.scale
    
    def GetName(self):
        return name