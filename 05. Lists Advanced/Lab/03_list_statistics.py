number = int(input())
positive = []
negative = []
for i in range(number):
    current_numbers = int(input())

    if current_numbers >= 0:
        positive.append(current_numbers)
    else:
        negative.append(current_numbers)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}\nSum of negatives: {sum(negative)}")
