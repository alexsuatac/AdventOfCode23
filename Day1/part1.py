def process(line):
    pair = [None]*2
    # find the first digit iterating from the beginning
    for c in line:
        if c.isdigit():
            pair[0] = c
            break

    # find the last digit by reversing the string and 
    # doing the same thing
    for c in line[::-1]:
        if c.isdigit():
            pair[1] = c
            break

    return int(pair[0]+pair[1])


sum = 0
with open('./input.txt') as file:
    for line in file:
        sum += process(line)

file.close()

print(sum)

