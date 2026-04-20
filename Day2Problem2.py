import re

def main():
    with open("Day2Problem1Input.txt") as f:
        valid = 0
        for line in f:
            split = line.split('-')
            startNum = split[0]
            endNum = split[1].replace(',', ' ')
            for num in range(int(startNum), int(endNum)+ 1):
                #print(num)
                #print(type(checkIfEqual(num)))
                valid += checkIfEqual(num)
        print(valid)
            
def checkIfEqual(num):
    valid = re.search(r'^(\d+)\1+$', str(num))
    if valid:
        return num
    else:
        return 0 
        

main()
