column = 0

data_set = []

def HorizontalSearch(data_set):
    count = 0
    for x in range(len(data_set)):
        for y in range(len(data_set[x])):
            try:
                if data_set[x][y] == "X" and data_set[x][y+1] == "M" and data_set[x][y+2] == "A" and data_set[x][y+3] == "S":
                    count += 1
            except:
                pass
        for y in range(len(data_set[x])):
            try:
                if data_set[x][y] == "S" and data_set[x][y+1] == "A" and data_set[x][y+2] == "M" and data_set[x][y+3] == "X":
                    count += 1
            except:
                pass

    return count

def VerticalSearch(data_set):
    count = 0
    data_rotate = [list(tup) for tup in zip(*data_set)]
    
    for x in range(len(data_rotate)):
        for y in range(len(data_rotate[x])):
            try:
                if data_rotate[x][y] == "X" and data_rotate[x][y+1] == "M" and data_rotate[x][y+2] == "A" and data_rotate[x][y+3] == "S":
                    count += 1
            except:
                pass
        for y in range(len(data_set[x])):
            try:
                if data_set[x][y] == "S" and data_set[x][y+1] == "A" and data_set[x][y+2] == "M" and data_set[x][y+3] == "X":
                    count += 1
            except:
                pass
    return count

def DiagonalSearch(data_set):
    count = 0

    for x in range(len(data_set)):
        for y in range(len(data_set[x])):
            try:
                if data_set[x][y] == "X" and data_set[x+1][y+1] == "M" and data_set[x+2][y+2] == "A" and data_set[x+3][y+3] == "S":
                    count += 1
            except:
                pass
        for y in range(len(data_set[x])):
            try:
                if data_set[x][y] == "X" and data_set[x+1][y-1] == "M" and data_set[x+2][y-2] == "A" and data_set[x+3][y-3] == "S":
                    count += 1
            except:
                pass
        for y in range(len(data_set[x])):
            try:
                if data_set[x][y] == "X" and data_set[x-1][y+1] == "M" and data_set[x-2][y+2] == "A" and data_set[x-3][y+3] == "S":
                    count += 1
            except:
                pass
        for y in range(len(data_set[x])):
            try:
                if data_set[x][y] == "X" and data_set[x-1][y-1] == "M" and data_set[x-2][y-2] == "A" and data_set[x-3][y-3] == "S":
                    count += 1
            except:
                pass
    return count





with open('input') as f:
    while f:
        data_line = f.readline()
        if data_line != "":
            data_set.append(list(data_line.rstrip("\n")))
            column += 1            
        else:
            break

answer = HorizontalSearch(data_set) + VerticalSearch(data_set) + DiagonalSearch(data_set)

print(answer)
