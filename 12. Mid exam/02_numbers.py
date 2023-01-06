the_good_numbers = [int(x) for x in input().split()]

the_possible_commands_data = input()

while not the_possible_commands_data == "Finish":

    the_command_list_for_numbers = the_possible_commands_data.split()
    inp_commands_for_num = the_command_list_for_numbers[0]

    if inp_commands_for_num == "Add":
        value = int(the_command_list_for_numbers[1])
        the_good_numbers.append(value)

    elif inp_commands_for_num == "Remove":
        value = int(the_command_list_for_numbers[1])
        if value in the_good_numbers:
            the_good_numbers.remove(value)

    elif inp_commands_for_num == "Replace":
        value = int(the_command_list_for_numbers[1])
        replacement = int(the_command_list_for_numbers[2])
        if value in the_good_numbers:
            index = the_good_numbers.index(value)
            if replacement:
                the_good_numbers.insert(index, replacement)
                the_good_numbers.remove(value)

    elif inp_commands_for_num == "Collapse":
        value = int(the_command_list_for_numbers[1])
        the_good_numbers = [x for x in the_good_numbers if x >= value]

    the_possible_commands_data = input()

print(*the_good_numbers)
