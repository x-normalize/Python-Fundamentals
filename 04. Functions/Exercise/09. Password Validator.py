def password_is_valid(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10:  # Check digits len!
        print(f'Password must be between 6 and 10 characters')
        is_valid = False
    if not password.isalnum():
        print(f'Password must consist only of letters and digits')
        is_valid = False
    digits_counter = 0
    for character in password:
        if character.isdigit():  # Check if password have digits and letters
            digits_counter += 1
    if digits_counter < 2:  # Count digits number!
        print(f'Password must have at least 2 digits')
        is_valid = False

    return is_valid


some_password = input()
password_is_valid = password_is_valid(some_password)
if password_is_valid:
    print(f'Password is valid')
