# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-19
    Author: John Huang
'''
import json

# 出題1: 寫一個函式 
# 參數 3+4j (complex) 
# output -> {'Real': 3, 'Imag': 4, 'Abs': 5} (dict)

def convertComplexToDict(complexNum:complex) -> dict:
    real = complexNum.real 
    imag = complexNum.imag 
    absolute = abs(complexNum)
    return {'Real': real, 'Imag': imag, 'Abs': absolute}

# 延伸2: 
# 參數 None
# output -> {..., 3+4j:{'Real': ...}, 3+5j:{'Real':...}, ...}

def generateNxMComplexDict(N:int, M:int) -> dict :
    table_dict = {}
    complexNumberArray = generateNxMComplexArray(N, M)
    for complexNum in complexNumberArray: 
        table_dict[complexNum] = convertComplexToDict(complexNum)
    return table_dict

# 出題3: 
# 產生一個檔案，內容如下:
# 0 j 2j ... Nj
# 1 1+j 1+2j ... 1+Mj 
#  ....
# N N+j ...   N+Mj

def ThirdFunction(N:int, M:int, file:str = 'test.txt'):
    table_txt = generateNxMComplexTableText(N, M)
    outputTextToFile(table_txt, file)

def outputTextToFile(text, file):
    with open(file, 'w') as fw: 
        fw.write(text)

def generateNxMComplexTableText(N:int, M:int):
    tmp_list = []
    complex_arr = generateNxMComplexArray(N, M)
    for item in complex_arr:
        line = ' '.join(item)
        tmp_list.append(line)
    return '\n'.join(tmp_list)    

def generateNxMComplexArray(N:int, M:int):
    arr = [] 
    for a in range(N+1): 
        arr.append([])
        for b in range(M+1): 
            complexNum = complex(a, b)
            arr[a].append(str(complexNum))
    return arr 

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

def FourthFunction(inputFile, outputFile=None): 
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
    s = s.replace('\n', '')
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
