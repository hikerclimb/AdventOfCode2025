import re

def main():
    with open("Day2Problem1Input.txt") as f:
        valid = 0
        for line in f:
            split = line.split('-')
            startNum = split[0]
            endNum = split[1].replace(',', ' ')
            for num in range(int(startNum), int(endNum)+ 1):
                valid += checkIfValid(num)
        print(valid)

def checkIfValid(num):
    valid = re.match(r'^(\d+)\1$', str(num))
    #print(num)
    if valid:
        return num
    else:
        return 0 

main()
