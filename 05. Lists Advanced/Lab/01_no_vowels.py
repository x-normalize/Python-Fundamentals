vowels = input()
lists = ['a', 'o', 'u', 'e', 'i']
no_vowels = [ch for ch in vowels if ch not in lists]
print(''.join(no_vowels))

