# Get inputs

input_file = open('input')
input_string = input_file.read()

find_string = 'mul('

start_index = [i for i in range(len(input_string)) if input_string.startswith(find_string, i)]

end_index = []

total = 0

for x in range(len(start_index)):
    try:    
        end_index.append(input_string.find(')', start_index[x]))

        number_string = input_string[start_index[x]+4:end_index[x]]
        number_string = number_string.split(",")
        
        if len(number_string) == 2:
            int_1 = int(number_string[0])
            int_2 = int(number_string[1])

            total += (int_1 * int_2)
    except:
        pass

    
print(total)
