first_position = input()
second_position = input()
last_position = input()

strings = [first_position, second_position, last_position]
strings[0], strings[2] = strings[2], strings[0]

print(strings)


