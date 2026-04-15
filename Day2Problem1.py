def main():
    with open("Day2Problem1Input.txt") as f:
        valid = 0
        for line in f:
            split = line.split('-')
            startNum = split[0]
            endNum = split[1].replace(',', ' ')
            for num in range(int(startNum), int(endNum)+ 1):
                valid += checkIfEqual(num)
        print(valid)
            
def checkIfEqual(num):
    numStr = str(num)
    firstHalf, secondHalf = generateHalfNumber(str(num))
    invalid = 0
    if firstHalf == secondHalf:
        invalid += num

    return invalid
        
def generateHalfNumber(num):
    whereToSplit = (int)(len(str(num))/2)
    firstHalf = num[0:whereToSplit]
    secondHalf = num[whereToSplit:len(str(num))]
    return firstHalf,secondHalf

main()
