import sys
import copy

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day10_input.txt"

### Start of test case ###
test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

test_1 = 36
test_2 = 2858
### End of test case ###



### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()



if mode == "TEST":
    pass
#    print("test status: " + str(test_1 == result_1))
#    print("test status: " + str(test_2 == buffor3))
