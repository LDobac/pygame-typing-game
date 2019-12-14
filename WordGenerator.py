'''
    WordGenerator.py
'''

import json
import random

from Utils import GetResources

# 무작위 영단어를 생성해 반환하는 클래스
class WordGenerator:

    def __init__(self):
        # Resources 폴더 내의 wordDict.json 파일을 사용한다.
        file = open(GetResources("wordDict.json"),"rt")
        self.wordList = json.loads(file.read())

    def GetWord(self, count = 1):
        
        # 무작위 단어 count개 반환
        randWords = []
        for i in range(0, count):
            word = self.wordList[random.randint(0, len(self.wordList) - 1)]
            randWords.append(word)

        return randWords