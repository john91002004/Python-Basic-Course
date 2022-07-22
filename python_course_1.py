# -*- coding: UTF-8 -*- 
'''
    Create date: 2022-07-19
    Author: John Huang
'''

# ========= 2022-07-19 ===========

# 穩定具體的變數類型
print(f'type of 3: {type(3)}')
print(f'type of 3.14: {type(3.14)}')
print(f'type of 3 + 4j: {type(3+4j)}')
print(f'type of WHAT: {type("WHAT")}')

# 指標變數類型
print(f'type of [3]: {type([3])}')
print(f'type of (3,1,4): {type((3,1,4))}')
print(f"type of 3:0.14: {type({3:0.14})}")

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

def generateZeroToFiveTableDict() -> dict :
    table_dict = {}
    for a in range(6): 
        for b in range(6):
            complexNum = complex(a, b)
            table_dict[complexNum] = convertComplexToDict(complexNum)
    return table_dict

# 出題3: 
# 產生一個檔案，內容如下:
# 0 j 2j ... 5j
# 1 1+j 1+2j ... 1+5j 
#  ....
# 5 5+j ...   5+5j

def outputZeroToFiveTableDictToFile(): 
    table_dict = generateZeroToFiveTableDict()
    count = 0 
    with open(file='ZeroToFiveTableDict.txt', mode='w') as fw: 
        for key in table_dict.keys(): 
            fw.write(f'{key} ')
            # 滿足一行最大數量，換行
            count += 1 
            if count == 6: 
                count = 0 
                fw.write('\n') 
