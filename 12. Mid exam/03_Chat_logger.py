for_the_list = []
my_list_commands = input()
while my_list_commands != 'end':
	my_list_commands = my_list_commands.split()
	if my_list_commands[0] == 'Chat':
		for_the_list.append(my_list_commands[1])
	elif my_list_commands[0] == 'Delete':
		if my_list_commands[1] in for_the_list:
			pos = for_the_list.index(my_list_commands[1])
			for_the_list.pop(pos)
	elif my_list_commands[0] == 'Edit':
		if my_list_commands[1] in for_the_list:
			pos = for_the_list.index(my_list_commands[1])
			for_the_list[pos] = my_list_commands[2]

	elif my_list_commands[0] == 'Spam':
		for c in my_list_commands[1:]:
			for_the_list.append(c)

	elif my_list_commands[0] == 'Pin':
		if my_list_commands[1] in for_the_list:
			pos = for_the_list.index(my_list_commands[1])
			for_the_list.append(for_the_list.pop(pos))

	my_list_commands = input()

print('\n'.join(for_the_list))