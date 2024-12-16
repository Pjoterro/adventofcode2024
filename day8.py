import sys
import copy

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day8_input.txt"

### Start of test case ###
test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

test_1 = 14
test_2 = 7
### End of test case ###



### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()



if mode == "TEST":
    pass
#    print("test status: " + str(test_1 == result))
#    print("test status: " + str(test_2 == result))
