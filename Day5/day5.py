sort_rules = []
page_numbers = []

sorted_pages = []
checked_pages = []

def SortLine(pages, rules):
    RulesMet = False
    while not RulesMet:
        RulesMet = True
        for x in range(len(rules)):
            if pages.index(rules[x][0]) > pages.index(rules[x][1]):
                RulesMet = False
                move_element = pages[pages.index(rules[x][0])]
                pages.remove(move_element)
                pages.insert(pages.index(rules[x][1]), move_element)
    return pages

def CheckLine(pages, rules):
    for x in range(len(rules)):
        if pages.index(rules[x][0]) > pages.index(rules[x][1]):
            return False
    return True

with open('instructions') as f:
    while f:
        data_line = f.readline()
        if data_line != "":
            data_line = data_line.rstrip("\n")
            sort_rules.append(data_line.split('|'))            
        else:
            break

with open('input') as g:
    while g:
        data_line = g.readline()
        if data_line != "":
            data_line = data_line.rstrip("\n")
            page_numbers.append(data_line.split(','))
        else:
            break

for x in range(len(page_numbers)):
    rules_triggered = []
    for y in range(len(sort_rules)):

        if (sort_rules[y][0] in page_numbers[x] and sort_rules[y][1] in page_numbers[x]):
            rules_triggered.append([sort_rules[y][0], sort_rules[y][1]])
   
    if rules_triggered:
        if CheckLine(page_numbers[x], rules_triggered):
            checked_pages.append(page_numbers[x])
        else:
            sorted_pages.append(SortLine(page_numbers[x], rules_triggered))
    else:
        checked_pages.append(page_numbers[x])
    
    rules_triggered.clear()


total_sorted = 0
total_checked = 0

for x in range(len(sorted_pages)):
    total_sorted += int(sorted_pages[x][len(sorted_pages[x])//2])

for x in range(len(checked_pages)):
    total_checked += int(checked_pages[x][len(checked_pages[x])//2])

print("all pages sorted: " + str(total_sorted))
print("only checked pages: " + str(total_checked))
