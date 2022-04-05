def interleave(*args):
    """
    Functions that get unlimited iterable objects and weaves them.
    :param args: An unlimited iterable objects.
    :return: A list containing the weaving of the iterable objects.
    """
    connected_vessels_list = []

    for iterable_index in range(len(args)):
        curr_index = iterable_index
        for element in args[iterable_index]:
            connected_vessels_list.insert(curr_index, element)
            curr_index += iterable_index + 1

    return connected_vessels_list


def interleave_generator(*args):
    """
    Functions generator that get unlimited iterable objects and weaves them.
    :param args: An unlimited iterable objects.
    :return: A list containing the weaving of the "n" first iterable objects
            (n = The number of calling to this function).
    """
    connected_vessels_list = []

    for iterable_index in range(len(args)):
        curr_index = iterable_index
        for element in args[iterable_index]:
            connected_vessels_list.insert(curr_index, element)
            curr_index += iterable_index + 1
        yield connected_vessels_list


if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print(interleave('abcd', [1, 2, 3, 4], ('!', '@', '#', 't')))
    print(interleave('abc', [1, 2, 3, 4], ('!', '@', '#')))
    for item in interleave_generator('abcd', [1, 2, 3, 4], ('!', '@', '#', 't')):
        print(item)
