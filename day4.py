import sys
import re

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day3_input.txt"

### Start of test case ###
test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

test_XMAS = 18
#test_mul2 = 48
### End of test case ###

def input_to_2d_array(string):
    result = []
    for line in input.splitlines():
        larray = []
        for char in line:
            larray.append(char)
        result.append(larray)
    return result

def find_xmas(array2d):
    result = 0
    width = len(array2d[1])
    height = len(array2d)
    print("Array size: " + str(width) + "x" + str(height))
    x_cord = 0
    y_cord = 0
    for line in array2d:
        x_cord = 0
        for char in line:
            if char == 'X':
            pass

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

buffer = input_to_2d_array(input)
find_xmas(buffer)

#if mode == "TEST":
#    print("test status: " + str(res == test_mul2))
