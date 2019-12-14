'''
    Utils.py
    유틸리티 클래스, 함수, 값이 들어있다
'''

# 색상 RGB 값을 정의하는 클래스
class Color:
    BLACK = (0,0,0)
    WHITE = (255,255,255)

# 화면 사이즈 정의
WindowSize = (320,720)

# Resources 폴더 상대 경로 반환 함수
def GetResources(fileName):
    return ''.join(["Resources/", fileName])