number_of_orders = int(input())
total = 0
for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_needed_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_needed_per_day < 1 or capsule_needed_per_day > 2000:
        continue
    total_price = capsule_needed_per_day * price_per_capsule * days
    total += total_price
    print(f"The price for the coffee is: ${total_price:.2f}")
print(f'Total: ${total:.2f}')


