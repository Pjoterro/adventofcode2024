import sys
import re

mode = sys.argv[1] # TEST or TASK
input_file_path = "./day3_input.txt"

### Start of test case ###
test_input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

test_mul = 161
test_mul2 = 48
### End of test case ###

mul_reg = r'mul\(\d+,\d+\)'
dont_do_reg = r'don\'t\(\).*do\(\)'
do_reg = r'do\(\)'
dont_reg = r'don\'t\(\)'

def multiply(single_mul): #w formacie string = "mul(int1,int2)"
    mul_red = single_mul.replace('mul(', '').replace(')', '')
    mul_array = mul_red.split(',')
    return int(mul_array[0])*int(mul_array[1])

def get_all_muls(input_text):
    result = re.findall(mul_reg, input_text)
    return result

def get_do_muls(input_text):
    result = []
    for part in re.split(dont_do_reg, input_text):
        result.extend(re.findall(mul_reg, part))
    return result

### main: ###
if mode == "TEST":
    input = test_input
elif mode == "TASK":
    file = open(input_file_path)
    input = file.read()

buffer = get_do_muls(input)
res = 0
for record in buffer:
    res = res + multiply(record)
print("mul result: " + str(res))
if mode == "TEST":
    print("test status: " + str(res == test_mul2))
