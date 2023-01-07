the_input_info = input()
my_guests_people = {}

angry_dislike_counter = 0
while not the_input_info == "Stop":
    guest_info = the_input_info.split("-")
    command = guest_info[0]
    name = guest_info[1]
    meal = guest_info[2]
    if command == "Like":
        if name not in my_guests_people:
            my_guests_people[name] = {'meal': [meal]}
        elif meal not in my_guests_people[name]['meal']:
            my_guests_people[name]['meal'].append(meal)
    elif command == "Dislike":
        if name not in my_guests_people:
            print(f"{name} is not at the party.")
        elif meal in my_guests_people[name]['meal']:
            angry_dislike_counter += 1
            my_guests_people[name]['meal'].remove(meal)
            print(f"{name} doesn't like the {meal}.")
        else:
            print(f"{name} doesn't have the {meal} in his/her collection.")

    the_input_info = input()

for guest_name, meals in my_guests_people.items():
    print(f"{guest_name}: {', '.join(meals['meal'])}")

print(f"Unliked meals: {angry_dislike_counter}")
