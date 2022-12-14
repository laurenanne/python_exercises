def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    output = {}
    vowel = 'aeiou'
    for char in phrase.lower():
        if char in vowel:
            if char in output:
                output[char] += 1
            else:
                output[char] = 1

    return output
