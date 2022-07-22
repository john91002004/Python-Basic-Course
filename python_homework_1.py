# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-19
    Author: John Huang
'''

# 出題1: 寫一個函式 
# 參數 3+4j (complex) 
# output -> {'Real': 3, 'Imag': 4, 'Abs': 5} (dict)

def convertComplexToDict(complexNum:complex) -> dict:
    real = complexNum.real 
    imag = complexNum.imag 
    absolute = abs(complexNum)
    return {'Real': real, 'Imag': imag, 'Abs': absolute}

# 延伸2: 
# 參數 N, M
# output -> {..., 3+4j:{'Real': ...}, 3+5j:{'Real':...}, ..., N+Mj:{...}}

def generateNxMComplexDict(N:int, M:int) -> dict :
    table_dict = {}
    complexNumArray = generateNxMComplexArray(N, M)
    complexNumList = expandArrayToList(complexNumArray)
    for complexNum in complexNumList: 
        table_dict[complexNum] = convertComplexToDict(complexNum)
    return table_dict

def expandArrayToList(arr):
    result = []
    for item in arr:
        result.extend(item)
    return result 

# 出題3: 
# 產生一個檔案，內容如下:
# 0 j 2j ... Nj
# 1 1+j 1+2j ... 1+Mj 
#  ....
# N N+j ...   N+Mj

def outputNxMComplexDictToFile(N:int, M:int, file:str = 'NxMComplexDict.txt') : 
    table_txt = generateNxMComplexTableText(N, M)
    with open(file, 'w') as fw: 
        fw.write(table_txt)

def generateNxMComplexTableText(N:int, M:int):
    tmp_list = []
    complex_arr = generateNxMComplexArray(N, M)
    string_arr = convertComplexArrayElementTypeToString(complex_arr)
    for item in string_arr:
        line = ' '.join(item)
        tmp_list.append(line)
    return '\n'.join(tmp_list)    

def convertComplexArrayElementTypeToString(arr):
    for i in range( len(arr) ):
        for j in range( len(arr[i]) ): 
            arr[i][j] = str(arr[i][j])
    return arr

def generateNxMComplexArray(N:int, M:int):
    arr = [] 
    for a in range(N+1): 
        arr.append([])
        for b in range(M+1): 
            complexNum = complex(a, b)
            arr[a].append(complexNum)
    return arr 
