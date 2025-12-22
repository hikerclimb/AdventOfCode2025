def main():
    with open("Day1Problem1SampleInput.txt") as f:
        lines = f.readlines()
    counter = 0
    dialPosition = 50
    #maxDialPosition = 100
    numberOfRotations = 0
    for line in lines:
        direction = line[0]
        #print('line:' + line)
        distance = (int)(line[1:])
        #numberOfRotations = ((int)(distance / maxDialPosition)) + numberOfRotations
        #print('dial position:' + str(dialPosition))
        if direction == 'L':
            dialPosition = (dialPosition - distance) % maxDialPosition
        else:
            dialPosition = (dialPosition + distance) % maxDialPosition
        if dialPosition == 0:
            counter = counter +1
    print('counter:' + str(counter))
    #print(counter+numberOfRotations)

main()
