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
#print('N:', N)

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b # //= for python 3
    return digits[::-1]

list_of_values_up_to_N = [x+1 for x in range(N)]

numbers_to_balance = []
for x in list_of_values_up_to_N:
    #print(x)
    x_10 = numberToBase(x, 10)
    print(x_10[-1])
    numbers_to_balance.append(x_10[-1])

print(numbers_to_balance)

#print(list_of_values_up_to_N)