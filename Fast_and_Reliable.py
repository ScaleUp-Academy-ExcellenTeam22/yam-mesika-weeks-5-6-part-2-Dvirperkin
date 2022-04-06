import time


def file_words_to_list_and_set():
    """
    Function that open a words file and creates two data structure (set and list) containing the words.
    :return: List and Set containing the words from the words file.
    """
    words_list = list()
    words_set = set()
    with open("words.txt", mode='r', encoding="utf-8") as file:
        for line in file.readlines():
            words_list.append(line)
            words_set.add(line)

    return words_list, words_set


def average_runtime(data_structure):
    """
    Function that get a data structure and measures the average time to search in it.
    :param data_structure: A data structure to measure the searching time.
    :return: Average time to search in the given data structure.
    """
    avg = 0
    for i in range(1000):
        start = time.time()
        "zwitterion" in data_structure
        end = time.time()
        avg += end - start
    return avg / 1000


if __name__ == '__main__':
    words_list_and_set = file_words_to_list_and_set()
    print(average_runtime(words_list_and_set[0]))
    print(average_runtime(words_list_and_set[1]))
