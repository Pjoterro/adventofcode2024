import sys
mode = sys.argv[1] # TEST or TASK
input_file_path = "./day2_input.txt"

### Start of test case ###
test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

test_safe = 2
test_safe2 = 4
### End of test case ###

def filter_safe_results(all_results):
    results = []
    for line in all_results.splitlines():
        if is_record_safe(line):
            results.append(line)
    return results

def is_record_safe(input):
    record = input.split()
    ascending_modifier = 1
    if int(record[0]) > int(record[1]):
        ascending_modifier = -1
    for i in range(len(record)-1):
        delta = (int(record[i+1]) - int(record[i])) * ascending_modifier
        if delta < 1 or delta > 3:
            return False
    return True

def is_record_safe2(input):
    record = input.split()
    ascending_modifier = 1
    recheck_flag = False
    recheck_index = 0
    if int(record[0]) > int(record[-1]):
        ascending_modifier = -1
    for i in range(len(record) - 1):
        delta = (int(record[i+1]) - int(record[i])) * ascending_modifier
        if (delta < 1 or delta > 3):
            if recheck_flag:
                return False
            recheck_flag = True
            recheck_index = i
    if not recheck_flag:
        return True
    rerecord_1 = input.split()
    rerecord_1.pop(recheck_index)
    rerecord_2 = input.split()
    rerecord_2.pop(recheck_index + 1)
    flag_1 = 
### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

buffer = filter_safe_results(input)
print("no. of safe reports: " + str(len(buffer)))
if mode == "TEST":
    print("test status: " + str(len(buffer) == test_safe))
