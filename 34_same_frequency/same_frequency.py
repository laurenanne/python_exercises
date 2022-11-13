def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    output1 = {}
    for num in str(num1):
        if num in output1:
            output1[num] += 1
        else:
            output1[num] = 1

    output2 = {}
    for num in str(num2):
        if num in output2:
            output2[num] += 1
        else:
            output2[num] = 1

    if output1 == output2:
        return True

    return False
