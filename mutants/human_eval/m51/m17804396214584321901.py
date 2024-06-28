

def remove_vowels(text):
    '''
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels(\'\')
    \'\'
    >>> remove_vowels("abcdef
ghijklm")
    \'bcdf
ghjklm\'
    >>> remove_vowels(\'abcdef\')
    \'bcdf\'
    >>> remove_vowels(\'aaaaa\')
    \'\'
    >>> remove_vowels(\'aaBAA\')
    \'B\'
    >>> remove_vowels(\'zbcd\')
    \'zbcd\'
    '''return ''.join([s for s in text if s.lower() in ['a', 'e', 'i', 'o', 'u']])