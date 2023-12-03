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

# find_all taken from 
# https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
def find_all(str, sub):
    start = 0
    while True:
        start = str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def process(line):
    # iterate through list
    # appending an index:digit pair
    # to a new list that keeps track of
    # each digit and its position
    pairs = []
    for i, c in enumerate(line):
        if c.isdigit():
            pairs.append([i, c])

    for spelled, digit in nums:
        for idx in find_all(line, spelled):
            pairs.append([idx, digit])


    # find the smallest and largest index
    # and concatenate the two corresponding digits
    # returning their sum - unless there is only one
    # digit in which case concatenate it with itself
    if len(pairs) == 0:
        return 0
    elif len(pairs) == 1:
        return int(pairs[0][1] + pairs[0][1])
    else:
        return int(min(pairs)[1] + max(pairs)[1])


sum = 0
with open('./input2.txt') as file:
    for line in file:
        sum += process(line)

file.close()

print(sum)

