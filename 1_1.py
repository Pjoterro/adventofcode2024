input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""
input_result = 11

table_left = []
table_right = []

def input_to_tables(input):
    for line in input.splitlines():
        if (line == ""):
            continue
        buffor = line.split()
        table_left.append(buffor[0])
        table_right.append(buffor[1])
    table_left.sort()
    table_right.sort()
    
def evaluate_distance(table_left, table_right):
    result = 0
    for i in range(len(table_left)):
        buffor = int(table_left[i]) - int(table_right[i])
        if buffor < 0:
            buffor = -buffor
        result = result + buffor
    return result

input_to_tables(input)
print(table_left)
print(table_right)
result = evaluate_distance(table_left, table_right)
print(result == input_result)
