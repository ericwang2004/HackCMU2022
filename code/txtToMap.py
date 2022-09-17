# converts .txt output from editor to int array input into Player class

def txtToInput():
    # opens map.txt / lines is an array containing each line as string
    with open('map.txt') as f:
        lines = f.readlines()

    def getTuple(s):
        start = s.find('(')
        mid = s.find(',')
        end = s.find(')')

        x = int(s[start + 1: mid])
        y = int(s[mid + 2: end])
        return x, y

    # get dimensions
    rows, cols = getTuple(lines[0])

    # reads through each line, updating input array
    input_array = []
    for row in range(rows):
        input_array.append([0]*cols)

    for i in range(1, len(lines)):
        x, y = getTuple(lines[i])
        if 'EMPTY' in lines[i]:
            typ = 0
        elif 'WALL' in lines[i]:
            typ = 1
        elif 'MAGIC' in lines[i]:
            typ = 2
        input_array[y][x] = typ

    f.close()
    return input_array
