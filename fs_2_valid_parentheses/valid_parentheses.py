def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    lst = list(parens)
    print(lst)

    n = len(lst)
    if n % 2 != 0:
        return False

    elif lst[0] == ")" or lst[-1] == "(":
        return False

    return True
