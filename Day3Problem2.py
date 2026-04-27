def main():
    with open("Day3Problem1SampleInput.txt") as f:
        output = []
        for line in f:
            output += numberToFind(line)
            print('out: ' +str(output))

def numberToFind(line):
    numbersRight = []
    numToFind = 4
    numbersLeft = []
    output = []
    for i in range(0, numToFind ):
        print('i:' + str(i))
        for index in range(numToFind - i,  len(line)):
            print('index: ' + str(index))
            if line[index] == '\n':
                line.replace('\n', '')
            else:
                numbersRight.append(line[index])
        for index in range(i, numToFind - i):
            if i >0:
                numbersLeft.append(numbersRight[i])
                break
            else:
                numbersLeft.append(line[index])
        print('numberLeft:' + str(numbersLeft))
        numbersLeft = list(map(int, numbersLeft))
        print('after Converting to int:' + str(numbersLeft))
        output.append(max(numbersLeft))
        numbersLeft.pop(numbersLeft.index(int(max(numbersLeft))))
        print('numberLeft after:' + str(numbersLeft))
        print('numberRight:' + str(numbersRight))
        #numbersLeft = []
        numbersRight = []
    return output
main()
