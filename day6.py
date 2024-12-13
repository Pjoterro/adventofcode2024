import sys

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day5_input.txt"

### Start of test case ###
test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

test_1 = 41
#test_2 = 123
### End of test case ###

all_dir = ['^', '>', 'v', '<'] # in that order
current_dir = ''
map_size_x = 0
map_size_y = 0

def get_map_size(input):
    pass

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()



if mode == "TEST":
#    print("test status: " + str(result1 == test_1))
#    print("test status: " + str(result2 == test_2))
