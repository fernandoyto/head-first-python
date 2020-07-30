word = input('Provide a word to search for vowels: ')

vowels = ['a', 'e', 'i', 'o', 'u']

found = {}

for c in word:
    if c in vowels:
        found.setdefault(c, 0)
        found[c] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
    