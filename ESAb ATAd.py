import sys

def complement(array):
    for i in range(len(array)):
        if array[i] == 1:
            array[i] = 0
        elif array[i] == 0:
            array[i] = 1

def findCheckIdx1(array):
    for i in range(int(len(array) / 2)):
        a = array[i]
        b = array[-i -1]
        if a != b and a != -1 and b != -1:
            return i
    
    return -1

def findCheckIdx2(array):
    for i in range(int(len(array) / 2)):
        a = array[i]
        b = array[-i -1]
        if a == b and a != -1 and b != -1:
            return i
    
    return -1

def sendQuery(index):
    print(index)
    sys.stdout.flush()
    res = input()
    if res == 'N':
        return -1
    else:
        return int(res)

def solve(B):
    data = [-1 for x in range(B)]
    checkIdx1 = -1
    checkIdx2 = -1
    queryCnt = 0
    startIdx = 0
    endIdx = B - 1
    sign = True

    while True:
        if queryCnt % 10 == 0:
            if checkIdx1 == -1:
                checkIdx1 = findCheckIdx1(data)
            if checkIdx2 == -1:
                checkIdx2 = findCheckIdx2(data)
            
            if checkIdx1 >= 0 or checkIdx2 >= 0:
                compOrRevs = False
                compOrAll = False
                if checkIdx1 >= 0:
                    bit = sendQuery(checkIdx1 + 1)
                    if bit == -1:
                        return False
                    queryCnt += 1
                    compOrRevs = bit != data[checkIdx1]
                if checkIdx2 >= 0:
                    bit = sendQuery(checkIdx2 + 1)
                    if bit == -1:
                        return False
                    queryCnt += 1
                    compOrAll = bit != data[checkIdx2]
                
                if compOrRevs and compOrAll:
                    complement(data)
                elif compOrRevs and not compOrAll:
                    data.reverse()
                    temp = startIdx
                    startIdx = B - endIdx - 1
                    endIdx = B - temp - 1
                    sign = not sign
                elif not compOrRevs and compOrAll:
                    complement(data)
                    data.reverse()
                    temp = startIdx
                    startIdx = B - endIdx - 1
                    endIdx = B - temp - 1
                    sign = not sign
                
        if sign:
            bit = sendQuery(startIdx + 1)
            if bit == -1:
                return False
            data[startIdx] = bit
            startIdx += 1
            queryCnt += 1
            sign = not sign
        else:
            bit = sendQuery(endIdx + 1)
            if bit == -1:
                return False
            data[endIdx] = bit
            endIdx -= 1
            queryCnt += 1
            sign = not sign

        if startIdx > endIdx:
            break
        
    answer = ""
    for x in data:
        answer += str(x)

    print(answer)
    sys.stdout.flush()
    result = input().strip()
    return result == 'Y'

T, B = [int(x) for x in input().split()]
for t in range(T):
    if solve(B):
        continue
    else:
        break