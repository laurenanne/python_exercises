def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    output = {}
    for num in nums:
        if num in output.keys():
            output[num] +=1
        else: output[num]=1

    final = max(list(output.values()))

    for (k,v) in output.items():
        if v == final:
            return k

