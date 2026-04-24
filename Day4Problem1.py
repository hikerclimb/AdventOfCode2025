from copy import copy,deepcopy

def main():
    with open("Day4Problem1Input.txt") as f:
        countRollOfPaper = 0
        rollYesOrNo = []
        for row, line in enumerate(f):
            new = []
            for col, i in enumerate(line):
                if i == '\n':
                    continue
                new.append(i)
            rollYesOrNo.append(new)
        countRollOfPaper += checkRolls(rollYesOrNo, row, col)
    print(countRollOfPaper)

def checkRolls(rollYesOrNo, row, col):
    counter = 0
    rollsOfPaper = 0
    output = deepcopy(rollYesOrNo)
    for row, line1 in enumerate(rollYesOrNo):
        for col, j in enumerate(line1):
            if rollYesOrNo[row][col] == '@' and col != len(line1) - 1 and rollYesOrNo[row][col+1] == '@':
                counter = counter +1
            if rollYesOrNo[row][col] == '@' and row != len(line1) -1 and rollYesOrNo[row+1][col] == '@':
                counter = counter +1
            if rollYesOrNo[row][col] == '@' and col != len(line1) -1  and row != len(line1) -1 and rollYesOrNo[row+1][col+1] == '@':
                counter = counter +1
            if rollYesOrNo[row][col] == '@' and col != len(line1) -1  and row -1 >= 0 and rollYesOrNo[row-1][col+1] == '@':
                counter = counter +1
            if rollYesOrNo[row][col] == '@' and row != len(line1) -1 and col -1 >= 0 and rollYesOrNo[row+1][col-1] == '@':
                counter = counter +1
            if rollYesOrNo[row][col] == '@' and col > 0 and row > 0 and rollYesOrNo[row-1][col-1] == '@':
                counter = counter +1
            if rollYesOrNo[row][col] == '@' and row -1 >= 0 and rollYesOrNo[row-1][col] == '@':
                counter = counter +1
            if rollYesOrNo[row][col] == '@' and col-1 >= 0 and rollYesOrNo[row][col-1] == '@':
                counter = counter +1
            if counter < 4 and rollYesOrNo[row][col] != '.':
                output[row][col] = 'X'
                rollsOfPaper = rollsOfPaper + 1
            counter = 0
        continue
    return rollsOfPaper
main()
