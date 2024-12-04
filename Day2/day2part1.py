def CheckAscDec(input_line):
    try:
        if input_line[0] == input_line[1]:
            return False
        elif input_line[0] > input_line[1]:
            for x in range(len(input_line)):
                if x != 0:
                    if input_line[x-1] <=input_line[x]:
                        return False
        elif input_line[0] < input_line[1]:
            for x in range(len(input_line)):
                if x != 0:
                    if input_line[x-1] >= input_line[x]:
                        return False
        return True
    except:
        print("Error")
        return False

def CheckSpread(input_line):
    try:
        for x in range(len(input_line)):
            if x != 0:
                if abs(input_line[x-1] - input_line[x]) > 3:
                    return False
        return True
    except:
        print("Error")
        return False

# Get inputs
safe_states = 0

input_split = []

with open('input') as f:
    while f:
        input_split.clear()
        input_line = f.readline()
        if input_line != "":
            input_line = input_line.rstrip("\n")
            input_split = list(map(int, input_line.split()))
            
            if CheckAscDec(input_split) and CheckSpread(input_split):
                safe_states += 1
        else:
            break

print(safe_states)

