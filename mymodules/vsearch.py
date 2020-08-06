def search_vowels(word: str) -> set:
    """Return any vowels any vowels found in a supplied word."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return vowels.intersection(set(word))


def search_for_letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

print(search_for_letters('galaxy'))