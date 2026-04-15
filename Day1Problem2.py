import math

def main():
    with open("Day1Problem2Input.txt") as f:
        lines = f.readlines()
        maxDialPosition = 100
        numOfTimesGoThroughLoop = 0
        click = 0
        currPos = 50
        for line in lines:
            direction = line[0]
            distance = (int)(line[1:])
            clicks = distance
            for _ in range(clicks):
                if direction == 'R':
                    currPos = (currPos + 1) % maxDialPosition
                else:
                    currPos = (currPos - 1) % maxDialPosition
                if currPos == 0:
                    numOfTimesGoThroughLoop += 1
        print(numOfTimesGoThroughLoop)
        '''prevDialPosition = dialPosition
        print('previous dialposition:' + str(prevDialPosition))
        numberOfRotations = countPassZeroNumOfTimes(distance, dialPosition,maxDialPosition, direction) + numberOfRotations
        if direction == 'L':
            dialPosition = (prevDialPosition - distance) % maxDialPosition
        else:
            dialPosition = (prevDialPosition + distance) % maxDialPosition
        print('dialposition:' + str(dialPosition))
        print('direction:' + str(direction))
        print('distance:' + str(distance)+ '\n')
        #numOfTimesGoThroughLoop = numOfTimesGoThroughLoop + 1
    #numberOfRotations = countPassZeroNumOfTimes(distance, dialPosition,maxDialPosition, direction) + numberOfRotations
    #print(numOfTimesGoThroughLoop)
    print(numberOfRotations)

def countPassZeroNumOfTimes(distance, dialPosition, maxDialPosition, direction):
    numOfTimesPassZero = 0
    
    num = (int)(dialPosition - distance)
    if direction == 'L':
        if dialPosition - distance < 0 and dialPosition != 0:
            numOfTimesPassZero = abs(math.floor((dialPosition - distance) // maxDialPosition))
        elif dialPosition == 0:
            numOfTimesPassZero = 1
        elif dialPosition - distance > 0 and dialPosition != 0:
            numOfTimesPassZero = math.ceil((dialPosition - distance) // maxDialPosition)
    else:
        if dialPosition + distance > 0 and dialPosition != 0:
            numOfTimesPassZero = (dialPosition + distance) // maxDialPosition
        elif dialPosition == 0:
            numOfTimesPassZero = 1
        elif dialPosition - distance < 0 and dialPosition != 0:
            numOfTimesPassZero = (dialPosition + distance ) // maxDialPosition
    print('num of iterations:' + str(numOfTimesPassZero))
    return numOfTimesPassZero'''


main()
