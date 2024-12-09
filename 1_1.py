# Test case:
test_input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""
test_result = 11

import requests

mode = "TEST" # either TEST or TASK
table_left = []
table_right = []
distance = 0
url = "https://adventofcode.com/2024/day/1/input"

def input_to_tables(input):
    for line in input.splitlines():
        if (line == ""):
            continue
        buffor = line.split()
        table_left.append(buffor[0])
        table_right.append(buffor[1])
    
def evaluate_distance(table_left, table_right):
    result = 0
    for i in range(len(table_left)):
        buffor = int(table_left[i]) - int(table_right[i])
        if buffor < 0:
            buffor = -buffor
        result = result + buffor
    return result

### main:
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    input = requests.get(url).text
    
input_to_tables(input)
table_left.sort()
table_right.sort()
distance = evaluate_distance(table_left, table_right)

if mode == "TEST":
    print(distance == test_result)
elif mode == "TASK":
    print(distance)
