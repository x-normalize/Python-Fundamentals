string = input()
a = []
for index in range(0 , len(string)):
    if string[index].isupper():
        a.append(index)
print(a)


