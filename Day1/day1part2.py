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

sim_score = 0
for x in range(len(left_list)):
    sim_score += left_list[x] * right_list.count(left_list[x])

print(sim_score)
