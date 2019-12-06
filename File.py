import json
import os

from Utils import GetResources

class JsonFile:
    def __init__(self, fileName):
        self.filePath = GetResources(''.join([fileName,".json"]))

        if not os.path.isfile(self.filePath):
            file = open(self.filePath,"x+", encoding="UTF-8")
            file.write("{ }")
            file.flush()
            file.close()

        self.jsonData = None

    def Load(self):
        file = open(self.filePath, "r", encoding="UTF-8")
        
        strJsonData = file.read()
        self.jsonData = json.loads(strJsonData)


    def Save(self):
        file = open(self.filePath, "w", encoding="UTF-8")

        file.write(json.dumps(self.jsonData))
        file.flush()