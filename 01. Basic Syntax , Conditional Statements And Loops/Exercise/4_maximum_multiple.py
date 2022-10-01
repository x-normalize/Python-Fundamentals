divisor = int(input())
boundary = int(input())
for current_numbers in range(boundary, divisor, -1):
    if current_numbers % divisor == 0:
        print(current_numbers)
        break

