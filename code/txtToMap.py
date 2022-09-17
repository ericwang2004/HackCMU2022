# converts .txt output from editor to int array input into Player class

# opens map.txt / lines is an array containing each line as string
with open('map.txt') as f:
    lines = f.readlines()

# reads through each line, updating input array
input_array = []
for row in rows:
    input_array.append([0]*cols)

for line in lines:
    x = 1
    y = 1
    typ = 1
    input_array[x][y] = typ

f.close()
return input_array

