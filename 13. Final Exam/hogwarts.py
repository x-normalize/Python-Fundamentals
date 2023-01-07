magic_spell = input()

command = input()

while command != "Abracadabra":
    the_magic_command_list = command.split()

    if the_magic_command_list[0] == "Abjuration":
        magic_spell = magic_spell.upper()
        print(magic_spell)

    elif the_magic_command_list[0] == "Necromancy":
        magic_spell = magic_spell.lower()
        print(magic_spell)

    elif the_magic_command_list[0] == "Illusion":
        index = int(the_magic_command_list[1])
        letter = the_magic_command_list[2]

        if len(magic_spell) > index >= 0:
            magic_spell = magic_spell[:index] + letter + magic_spell[index + 1:]
            print("Done!")
        else:
            print(f"The spell was too weak.")

    elif the_magic_command_list[0] == "Divination":
        first_sub = the_magic_command_list[1]
        second_sub = the_magic_command_list[2]

        magic_spell = magic_spell.replace(first_sub, second_sub)
        print(magic_spell)

    elif the_magic_command_list[0] == "Alteration":
        substring = the_magic_command_list[1]

        magic_spell = magic_spell.replace(substring, '')
        print(magic_spell)

    else:
        print(f"The spell did not work!")

    command = input()

