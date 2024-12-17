import sys
import copy

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day9_input.txt"

### Start of test case ###
test_input = """2333133121414131402"""

test_1 = 1928
test_2 = 34
### End of test case ###

drive = []

def expand_drive(input):
    global drive
    id = 0
    for i in range(len(input)):
        if input[i] == "\n":
            print("input len: " + str(len(input)) + " | i index: " + str(i))
            continue
        if i % 2 == 0:
            for j in range(int(input[i])):
                drive.append(str(copy.deepcopy(id)))
            id = id + 1
        else:
            for j in range(int(input[i])):
                drive.append('.')

def drive_to_string():
    global drive
    result = ""
    for i in drive:
        result = result + i
    print(result)

def defrag():
    global drive
    i_f = 0
    i_b = len(drive) - 1
    while True:
        while drive[i_b] == '.': # ustawiamy i_backward na jakas cyfre
            i_b = i_b - 1
        if i_f >= i_b: # trzeba sprawdzic czy i_b sie za bardzo nie zmienilo
            break
        if drive[i_f] == ".": # natrafiamy z przody na .
            drive[i_f] = copy.deepcopy(drive[i_b])
            drive[i_b] = '.'
            i_f = i_f + 1
            i_b = i_b - 1
        else: # natrafiamy na cyfre
            i_f = i_f + 1
        if i_f >= i_b: #znowu po zmianie indeksow sprawdzamy czy warunek jest ok
            break

def calc_checksum():
    global drive
    result = 0
    i = 0
    while True:
        if drive[i] == '.':
            break
        result = result + (int(drive[i]) * i)
        i = i + 1
    return result

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

expand_drive(input)
defrag()
result_1 = calc_checksum()
print(result_1)

if mode == "TEST":
    print("test status: " + str(test_1 == result_1))
    #print("test status: " + str(test_2 == result_2))
