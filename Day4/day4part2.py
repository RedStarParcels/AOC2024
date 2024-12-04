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
            try:
                if data_set[x][y] == "X" and data_set[x+1][y-1] == "M" and data_set[x+2][y-2] == "A" and data_set[x+3][y-3] == "S":
                    count += 1
            except:
                pass
            try:
                if data_set[x][y] == "X" and data_set[x-1][y+1] == "M" and data_set[x-2][y+2] == "A" and data_set[x-3][y+3] == "S":
                    count += 1
            except:
                pass
            try:
                if data_set[x][y] == "X" and data_set[x-1][y-1] == "M" and data_set[x-2][y-2] == "A" and data_set[x-3][y-3] == "S":
                    count += 1
            except:
                pass
    return count

def MasSearch(data_set):
    count = 0
    
    for x in range(1, len(data_set)-1):
        for y in range(1, len(data_set[x])-1):
            # 1. M - S      2. M - M    3. S - M    4. S - S 
            #    - A -         - A -       - A -       - A -
            #    M - S         S - S       S - M       M - M  
            try:
                if data_set[x][y] == "A":
                    if data_set[x-1][y-1] == "M" and data_set[x-1][y+1] == "S" and data_set[x+1][y-1] == "M" and data_set[x+1][y+1] == "S":
                        count += 1
                    elif data_set[x-1][y-1] == "M" and data_set[x-1][y+1] == "M" and data_set[x+1][y-1] == "S" and data_set[x+1][y+1] == "S": 
                        count += 1
                    elif data_set[x-1][y-1] == "S" and data_set[x-1][y+1] == "M" and data_set[x+1][y-1] == "S" and data_set[x+1][y+1] == "M": 
                        count += 1
                    elif data_set[x-1][y-1] == "S" and data_set[x-1][y+1] == "S" and data_set[x+1][y-1] == "M" and data_set[x+1][y+1] == "M": 
                        count += 1
            except:
                pass
    return count

with open('input') as f:
    while f:
        data_line = f.readline()
        if data_line != "":
            data_set.append(list(data_line.rstrip("\n")))
        else:
            break

answer = HorizontalSearch(data_set) + VerticalSearch(data_set) + DiagonalSearch(data_set)
answer2 = MasSearch(data_set)

print('Part 1: ' + str(answer))
print('Part 2: ' + str(answer2))
