import json
import random

from Utils import GetResources

class WordGenerator:

    def __init__(self):
        file = open(GetResources("wordDict.json"),"rt")
        self.wordList = json.loads(file.read())

    def GetWord(self, count = 1):
        
        randWords = []
        for i in range(0, count):
            word = self.wordList[random.randint(0, len(self.wordList) - 1)]
            randWords.append(word)

        return randWords