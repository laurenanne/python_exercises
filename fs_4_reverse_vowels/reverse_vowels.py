def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = "aeiouAEIOU"

    str_vow = []
    for char in s:
        if char in vowels:
            str_vow.append(char)

    str_vow.reverse()

    lst = list(s)
    n = 0
    for i in range(len(lst)):
        if lst[i] in vowels:
            lst[i] = str_vow[n]
            n += 1

        else:
            lst

    return ''.join(lst)
