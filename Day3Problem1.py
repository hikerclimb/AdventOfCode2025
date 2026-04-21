def main():
    with open("Day3Problem1Input.txt") as f:
        summ = 0
        for line in f:
            numbers = []
            startPosition = 0
            numbersShortened = []
            for index in range(0, len(line) -1):
                if index == len(line) - 2:
                   continue
                else:
                    numbers.append(line[index])
            startPosition = numbers.index(str(max(numbers))) + 1
            for index in range(startPosition, len(line)):
                numbersShortened.append(line[index])
            numJoint = int(max(numbers)+ max(numbersShortened))
            summ += numJoint
        print(summ)
            
main()
