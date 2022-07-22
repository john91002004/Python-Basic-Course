# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-19
    Author: John Huang
'''

import json

# ========= 以下函式沿用 python_homework_1 ===========

def convertComplexToDict(complexNum:complex) -> dict:
    real = complexNum.real 
    imag = complexNum.imag 
    absolute = abs(complexNum)
    return {'Real': real, 'Imag': imag, 'Abs': absolute}

# ========= 以上函式沿用 python_homework_1 ===========

# ========= 2022-07-21 ===========

# 延伸4: 
# Input -> 包含很多複數的檔案，如出題3
# Output -> 產生json檔案，內容如下:
#       {... , 3+4j: {'Real': 3, 'Imag': 4, 'Abs': 5},
#        3+5j: {...}, 4+0j:{...}, 4+j: {...} ...}
# 提示: 先將檔案讀入，轉換成list，然後產生雙層字典，再轉換成json字串。
# 
# [JSON_BUG]: json的dumps方法無法接受字典用complex型態的變數當作key。
# 

def FourthFunction(inputFile='NxMComplexDict.txt', outputFile=None): 
    complexTableString = readFile(inputFile)
    complexArray = convertComplexTableStringIntoList(complexTableString)
    complexArrayDict = convertComplexListIntoDict(complexArray) 
    jsonComplexArrayDict = json.dumps(complexArrayDict, indent=4)
    
    if outputFile == None: 
        outputFile = inputFile.split('.')[0] + '.json'
    writeFile(jsonComplexArrayDict, outputFile)

def readFile(file):
    with open(file) as fr:
        s = fr.read() 
    return s

def convertComplexTableStringIntoList(complexTableString:str):
    s = complexTableString.strip()
    s = s.replace('\n', ' ')
    s = s.split(' ')
    return s 

def convertComplexListIntoDict(complexTableList):
    complexDict = {}
    for item in complexTableList:
            complexNum = complex(item)
            complexDict[item] = convertComplexToDict(complexNum)
    return complexDict

def writeFile(txt, file): 
    with open(file, 'w') as fw: 
        fw.write(txt)
