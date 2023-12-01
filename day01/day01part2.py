
SPELT_NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def check_for_spelt_numbers(input_string):
    num_string = ""
    for i in range(len(input_string)):
        if input_string[i].isdigit():
            num_string += input_string[i]
        else:
            for j in range(len(SPELT_NUMBERS)):
                if input_string[i-1:].startswith(SPELT_NUMBERS[j]):
                    num_string += str(j+1)
                    break
    return num_string


total_calibration_value = 0

with open("input.txt") as input_text:
    for line in input_text.readlines():
        digits_in_line = check_for_spelt_numbers(line)
        if len(digits_in_line) > 0:
            total_calibration_value += int(digits_in_line[0] + digits_in_line[-1])

print(total_calibration_value)
