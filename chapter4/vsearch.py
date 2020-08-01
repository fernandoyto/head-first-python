def search_vowels(word):
    """Display any vowels found in a supplied word."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search_vowels('hitch-hiker')
