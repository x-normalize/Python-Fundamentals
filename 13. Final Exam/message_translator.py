import re
n = int(input())
for nothing in range(n):
    message = input()
    match = re.findall(r"!([A-Z][a-z]{2,})!:\[([a-zA-Z]{8,})\]", message)
    if len(match) != 1:
        print("The message is invalid")
    else:
        command = match[0][0]
        message = match[0][1]
        the_encrypted_one = ""
        for i in message:
            the_encrypted_one += f"{ord(i)} "
        print(f"{command}: {the_encrypted_one}")

