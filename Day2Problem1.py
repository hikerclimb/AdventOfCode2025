def main():
    with open("Day2Problem1Input.txt") as f:
        valid = 0
        for line in f:
            split = line.split('-')
            startNum = split[0]
            endNum = split[1].replace(',', ' ')
            #print(startNum)
            #print(endNum)
            for num in range(int(startNum), int(endNum)+ 1):
                valid += checkIfEqual(num)
        print(valid)
            
def checkIfEqual(num):
    checkDigit = []
    numStr = str(num)
    #print('num:' + str(num))
    firstHalf, secondHalf = generateHalfNumber(str(num))
    invalid = 0
    if firstHalf == secondHalf:
        #print('fir:'+firstHalf)
        #print('sec:'+secondHalf)
        invalid += num

    return invalid
    
    '''for i in range(0, len(str(num))-1):
        print('i:' + str(i))
        print('length:' + str(len(str(num)) - 1))
        if numStr[i] == numStr[i+1] and len(str(num))% 2 == 0:
            checkDigit.append(i % 10)
            print(checkDigit)
        else:
            break'''
        
def generateHalfNumber(num):
    whereToSplit = (int)(len(str(num))/2)
    firstHalf = num[0:whereToSplit]
    secondHalf = num[whereToSplit:len(str(num))]
    #print('fir:'+firstHalf)
    #print('sec:'+secondHalf)
    return firstHalf,secondHalf

main()
