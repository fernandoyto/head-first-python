word = 'Marvin, the Paranoid Android'

l = list(word)

for char in l[:6]:
    print('\t', char)
print()

for char in l[-7:]:
    print('\t' * 2, char)
print()

for char in l[12:20]:
    print('\t' * 3, char)