
total_calibration_value = 0

with open("input.txt") as input_text:
    for line in input_text.readlines():
        digits_in_line = ""
        for character in line:
            if character.isdigit():
                digits_in_line += character
        if len(digits_in_line) > 0:
            total_calibration_value += int(digits_in_line[0] + digits_in_line[-1])

print(total_calibration_value)
