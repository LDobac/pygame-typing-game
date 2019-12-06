class Scene:
    def __init__(self):
        self.data = None
        self.objects = []

    def Init(self):
        pass

    def Close(self):
        pass

    def Update(self, deltaTime):
        for obj in self.objects:
            obj.Update(deltaTime)

    def Draw(self, surface):

        sortedObjects = sorted(self.objects,key=lambda obj: obj.GetLayer())
        surfRects = list(map(lambda obj: obj.Draw(),sortedObjects))

        surface.blits(surfRects)

    def AddObject(self, obj):
        if obj not in self.objects:
            self.objects.insert(0, obj)

    def RemoveObject(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)