import sys
import copy

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day9_input.txt"

### Start of test case ###
test_input = """2333133121414131402"""

test_1 = 1928
test_2 = 2858
### End of test case ###

drive = []
drive2 = [] # [[char, count, moved_flag], [char, count, moved_flag]...]

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

def expand_drive2(input):
    global drive2
    id = 0
    for i in range(len(input)):
        if input[i] == "\n":
            print("input len: " + str(len(input)) + " | i index: " + str(i))
            continue
        if i % 2 == 0:
            drive2.append([id, int(input[i]), False])
            id = id + 1
        else:
            drive2.append(['.', int(input[i]), False])

def drive_to_string():
    global drive
    result = ""
    for i in drive:
        result = result + i
    print(result)

def drive2_to_string():
    global drive2
    result = ""
    for record in drive2:
        for count in range(record[1]):
            result = result + str(record[0])
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

def defrag2():
    print("defrag2() start")
    global drive2 # [[char, count, moved_flag], [char, count, moved_flag]...]
    for i_b in range(len(drive2)-1, 0, -1):
        #print("i_b: " + str(i_b) + " = " + str(drive2[i_b]))
        drive2_to_string()
        if drive2[i_b][2]:
            continue
        i_f = 0
        #print("i_f: " + str(drive2[i_f]) + "  |  i_b: " + str(drive2[i_b]))
        while i_f < len(drive2):
            if drive2[i_f][1] > drive2[i_b][1] and drive2[i_f][0] == '.':
                buffor = copy.deepcopy(drive2[i_f][1] - drive2[i_b][1])
                drive2[i_f][0] = copy.deepcopy(drive2[i_b][0])
                drive2[i_f][1] = copy.deepcopy(drive2[i_b][1])
                drive2.insert(i_f + 1, ['.', copy.deepcopy(buffor), True])
                drive2[i_b + 1][0] = '.'
                break
            elif drive2[i_f][1] == drive2[i_b][1] and drive2[i_f][0] == '.':
                drive2[i_f][0] = copy.deepcopy(drive2[i_b][0])
                drive2[i_b][0] = '.'
                break
            else:
                i_f = i_f + 1
            if i_f >= i_b:
                break
    print("defrag2() stop")

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

expand_drive2(input)
print("Before defrag:")
drive2_to_string()
defrag2()
print("After defrag:")
drive2_to_string()

if mode == "TEST":
    pass
    #print("test status: " + str(test_1 == result_1))
    #print("test status: " + str(test_2 == result_2))
