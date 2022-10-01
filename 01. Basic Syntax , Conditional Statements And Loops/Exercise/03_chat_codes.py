number = int(input())

for messages in range(number):
    type_messages = int(input())
    if type_messages == 88:
        print('Hello')
    elif type_messages == 86:
        print('How are you?')
    elif type_messages <= 88:
        print('GREAT!')
    elif type_messages > 88:
        print('Bye.')


