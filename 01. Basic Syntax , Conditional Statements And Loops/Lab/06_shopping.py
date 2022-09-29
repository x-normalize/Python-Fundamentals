budget = int(input())
input_linet = input()

while input_linet != 'End':
    money = int(input_linet)
    budget -= money

    if budget < 0:
        print(f'You went in overdraft!')
        break

    input_linet = input()

else:
    print(f'You bought everything needed.')
    