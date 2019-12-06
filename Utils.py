class Color:
    BLACK = (0,0,0)
    WHITE = (255,255,255)

WindowSize = (1280,720)

def GetResources(fileName):
    return ''.join(["Resources/", fileName])