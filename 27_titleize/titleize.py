def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    final_phrase = []
    lst = ''.join(phrase).split()

    for word in lst:
        cap = word[0:1:1]
        low = word[1:len(word):1]

        cap_letter = [letter.upper() for letter in cap]
        cap_low = [letter.lower() for letter in low]

        new_word = cap_letter + cap_low
        new_str = ''.join(new_word)
        final_phrase.append(new_str)

    return ' '.join(final_phrase)
