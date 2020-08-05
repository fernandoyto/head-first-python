def search_vowels(word:str) -> set:
    """Return any vowels any vowels found in a supplied word."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return vowels.intersection(set(word))

help(search_vowels)
