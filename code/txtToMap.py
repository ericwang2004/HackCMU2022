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
    
    adj_list = {}

    endx, endy = -1, -1
    for i in range(1, len(lines)):
        line = lines[i]
        x, y = getTuple(line)
        if 'EMPTY' in line:
            typ = 0
            if 'END' in line:
                endx, endy = x, y
        elif 'WALL' in line:
            typ = 1
        elif 'MAGIC' in line:
            index = line.find('MAGIC')
            line = line[index:] 
            x1, y1 = getTuple(line)
            adj_list[(y, x)] = (y1, x1)
            typ = 2
        input_array[y][x] = typ

    f.close()
    return input_array, adj_list, endx, endy


