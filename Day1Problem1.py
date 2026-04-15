def main():
    with open("Day1Problem2SampleInput.txt") as f:
        lines = f.readlines()
    counter = 0
    dialPosition = 50
    maxDialPosition = 100
    for line in lines:
        direction = line[0]
        distance = (int)(line[1:])
        if direction == 'L':
            dialPosition = (dialPosition - distance) % maxDialPosition
        else:
            dialPosition = (dialPosition + distance) % maxDialPosition
        if dialPosition == 0:
            counter = counter +1
    print('counter:' + str(counter))

main()
