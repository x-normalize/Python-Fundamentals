happiness_list = list(map(int, input().split(' ')))
factor = int(input())
happiness_list = [x * factor for x in happiness_list]

total_employees = len(happiness_list)
average_happyness = sum(happiness_list) / total_employees
happy_employees = len(list(filter(lambda x: x >= average_happyness, happiness_list)))

if happy_employees * 2 > total_employees:
    print(f'Score: {happy_employees}/{total_employees}. Employees are happy!')
else:
    print(f'Score: {happy_employees}/{total_employees}. Employees are not happy!')
