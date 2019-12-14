'''
    Scene.py

    하나의 Scene을 담당한다.
    Scene이 바뀌면 해당 Scene에 있던 이미지는 사라지고 새로운 Scene의 로직으로 바뀐다
'''

class Scene:
    def __init__(self):
        # 이전 Scene에서 넘긴 User Custom Data
        self.data = None
        # Scene에 있는 Object 객체, 등록 되어 있어야 Scene에서 Update와 Draw가 이뤄진다.
        self.objects = []

    def Init(self):
        pass

    def Close(self):
        pass

    # self.objects에 등록된 객체들의 Update 함수 호출
    def Update(self, deltaTime):
        for obj in self.objects:
            obj.Update(deltaTime)

    '''
        self.objects에 등록된 객체들의 Draw 함수를 호출해 화면에 그린다
        그리는 순서에 따라 object의 layer 값으로 정렬 시켜 그린다 
    '''
    def Draw(self, surface):

        sortedObjects = sorted(self.objects,key=lambda obj: obj.GetLayer())
        surfRects = list(map(lambda obj: obj.Draw(),sortedObjects))

        surface.blits(surfRects)

    # Scene에 오브젝트를 등록한다.
    def AddObject(self, obj):
        if obj not in self.objects:
            self.objects.insert(0, obj)

    # Scene에 오브젝트를 삭제한다, 더 이상 Update되거나 Draw되지 않는다.
    def RemoveObject(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)