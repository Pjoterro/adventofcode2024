import sys
mode = sys.argv[1] # TEST or TASK
input_file_path = "./day2_input.txt"

### Start of test case ###
test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
48 46 47 49 51 54 56
1 1 2 3 4 5
1 2 3 4 5 5
5 1 2 3 4 5
1 4 3 2 1
1 6 7 8 9
1 2 3 4 3
9 8 7 6 7
7 10 8 10 11
29 28 27 25 26 25 22 20"""

test_safe = 2
test_safe2 = 14
### End of test case ###

def filter_safe_results(all_results):
    results = []
    for line in all_results.splitlines():
        if (line == ""):
            continue
        if is_record_safe(line.split()):
            results.append(line)
    return results

def is_record_safe(array):
    recheck_flag = False
    recheck_index = 0
    ascending_modifier = 1
    if int(array[0]) > int(array[-1]):
        ascending_modifier = -1
    for i in range(len(array) -1):
        delta = (int(array[i+1]) - int(array[i])) * ascending_modifier
        if (delta < 1 or delta > 3):
            if recheck_flag:
                print("----TO IGNORE\nindex: " + str(i) + "\n" + str(array))
                return False
            else:
                recheck_flag = True
                recheck_index = i
    if not recheck_flag:
        return True
    print("----TO RECHECK\n" + str(array))
    sub_array_1 = array.copy()
    sub_array_2 = array.copy()
    sub_array_1.pop(recheck_index)
    flag_1 = True
    sub_array_2 = array
    sub_array_2.pop(recheck_index + 1)
    flag_2 = True
    for i in range(len(sub_array_1) - 1):
        delta = (int(sub_array_1[i+1]) - int(sub_array_1[i])) * ascending_modifier
        if (delta < 1 or delta > 3):
            flag_1 = False
            break
    for i in range(len(sub_array_2) - 1):
        delta = (int(sub_array_2[i+1]) - int(sub_array_2[i])) * ascending_modifier
        if (delta < 1 or delta > 3):
            flag_2 = False
            break
    print("index: " + str(recheck_index) + " | bools: " + str(flag_1 or flag_2))
    return (flag_1 or flag_2)


### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

buffer = filter_safe_results(input)
print("no. of safe reports: " + str(len(buffer)))
if mode == "TEST":
    print("test status: " + str(len(buffer) == test_safe2))
