nums = [
    ("zero" , "0"),
    ("one"  , "1"),
    ("two"  , "2"),
    ("three", "3"),
    ("four" , "4"),
    ("five" , "5"),
    ("six"  , "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine" , "9"),
]


def process(line):
    # iterate through list
    # appending an index:digit pair
    # to a new list that keeps track of
    # each digit and its position
    pairs = []
    for i, c in enumerate(line):
        if c.isdigit():
            pairs.append([i, c])
        else:
            for spelled, digit in nums:
                idx = line.find(spelled)
                if idx != -1:
                    pairs.append([idx, digit])


    # find the smallest and largest index
    # and concatenate the two corresponding digits
    # returning their sum
    min_idx = map(lambda *args: min(args), *pairs)
    max_idx = map(lambda *args: max(args), *pairs)
    

    return 0
    # return int(pair[0]+pair[1])


sum = 0
with open('./input2.txt') as file:
    for line in file:
        sum += process(line)

file.close()

print(sum)

