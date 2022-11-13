def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    lst = list(phrase)

    if to_swap.isupper(): 
        new_lst = [char.lower() if char == to_swap else char.upper() for char in lst]
        return ''.join(new_lst)

    elif to_swap.islower(): 
        new_lst = [char.upper() if char == to_swap else char.lower() for char in lst]
        return ''.join(new_lst)