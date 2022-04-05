def perfect_dish_to_share():
    """
    A function that prints all the "Perfect dish to share" numbers.
    :return: none
    """
    for item in search_for_all_perfect_dish():
        print(item)


def search_for_all_perfect_dish():
    """
    A generator function that search for all the "Perfect dish to share" number.
    :return: The next "Perfect dish to share" number.
    """
    num = 1
    while True:
        if is_perfect_dish(num):
            yield num
        num += 1


def is_perfect_dish(dish):
    """
    A functions that get an integer and return if the given number is a "Perfect dish to share"
    :param dish: A int to check if it indicates a "perfect dish to share".
    :return: True if is "Perfect dish to share" and else False.
    """
    dividers_sum = 0
    for divider in range(1, dish // 2 + 1):
        if dish % divider == 0:
            dividers_sum += divider
    if dividers_sum == dish:
        return True
    return False


if __name__ == '__main__':
    perfect_dish_to_share()
