letters = input()

digits, letter, others = [], [], []

for digit in letters:
    if digit.isdigit():
        digits.append(digit)
    elif digit.isalpha():
        letter.append(digit)
    else:
        others.append(digit)

print(''.join(digits))
print(''.join(letter))
print(''.join(others))


