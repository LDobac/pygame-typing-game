'''
    File.py
    파일 입출력에 관한 클래스들을 명시
'''

import json
import os

from Utils import GetResources

# Json 파일을 불러와 dictionary 형태로 반환하고, 저장하는 클래스
class JsonFile:
    def __init__(self, fileName):

        self.filePath = GetResources(''.join([fileName,".json"]))

        # 해당 파일이 없으면 빈 JSON 파일을 생성한다.
        if not os.path.isfile(self.filePath):
            file = open(self.filePath,"x+", encoding="UTF-8")
            file.write("{ }")
            file.flush()
            file.close()

        self.jsonData = None

    # JSON 파일을 읽어와 python 자료형으로 변경해 반환한다.
    def Load(self):
        file = open(self.filePath, "r", encoding="UTF-8")
        
        strJsonData = file.read()
        self.jsonData = json.loads(strJsonData)

    # python 자료형을 JSON 포맷 자료형으로 변경 후 저장한다.
    def Save(self):
        file = open(self.filePath, "w", encoding="UTF-8")

        file.write(json.dumps(self.jsonData))
        file.flush()