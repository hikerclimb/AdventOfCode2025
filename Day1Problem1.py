def main():
    with open("Day1Problem1SampleInput.txt") as f:
        lines = f.readlines()
    counter = 0
    start = 50
    swtichSign = False
    for line in lines:
        direction = line[0]
        print('line:' + line)
        if direction == 'L' and (start - int(line[1:])%99) < 0:
            print('enter left')
            start = ((start - int(line[1:])+1) %99)
        elif direction == 'R' and (start + int(line[1:])%99) > 0:
            print('enter right')
            start = ((start + int(line[1:])) % 100)
        elif direction == 'L' and (start - int(line[1:])%99) > 0:
            print("positiveleft")
            start = ((start - int(line[1:])) % 99)
        elif direction == 'R' and (start - int(line[1:])%99) < 0:
            print("positiveright")
            start = ((start - int(line[1:])) % 99)
        if direction == 'L' and start == 0:
            print('enter left sub 0')
            start = ((start - int(line[1:])) %99)
        elif direction == 'R' and start == 99:
            print('enter right sub 0')
            start = 99
        elif direction == 'L' and (start - int(line[1:])%99) > 0:
            print("positiveleft")
            start = ((start - int(line[1:])) % 99)
        elif direction == 'R' and (start - int(line[1:])%99) < 0:
            print("positiveright")
            start = ((start - int(line[1:])) % 99)
        if start == 0:
            
            counter = counter +1
        print('start:' + str(start))
    print(counter)

main()
