left_list = []
right_list = []

# Get inputs

with open('input') as f:
    while f:
        input_line = f.readline()
        if input_line != "":
            input_line = input_line.rstrip("\n")
            input_split = input_line.split()
            left_list.append(int(input_split[0]))
            right_list.append(int(input_split[1]))
        else:
            break


# List sorting
left_list.sort()
right_list.sort()

# Calc total

total_dif = 0

for x in range(len(left_list)):
    total_dif += abs(left_list[x] - right_list[x])

print(total_dif)
