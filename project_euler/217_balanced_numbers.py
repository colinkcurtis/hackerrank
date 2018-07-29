input_line_1 = input()
input_1_values = [int(x) for x in input_line_1.split(' ')]

input_line_2 = input()
input_2_values = [int(x) for x in input_line_2.split(' ')]

base = input_1_values[0]
N = input_1_values[1]

input_digits = input_2_values

powers_list = list(reversed(range(N)))

# print('powers_list', powers_list)

# print('base:', base)

# print('number_of_integers:', N)

# print('input digits:', input_digits)

# print('powers list:', powers_list)

converted_digits = [(base**powers_list[x])*input_digits[x] for x in powers_list if input_digits[x]]
N = sum(converted_digits)
print('N:', N)