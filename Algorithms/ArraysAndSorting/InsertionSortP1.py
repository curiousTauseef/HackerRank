def pretty_print(array):
    """
    Prints the given list as merely space-separated values
    :param array: the list to print
    :return: None, prints to std out
    """
    string = ""
    for val in array:
        string += str(val) + " "

    print(string.strip())


def run():
    """
    "Main" method, usage is:
        User inputs size of array, s
        User inputs array of size s with all elements sorted except the rightmost

        Prints the array at every step until array is sorted
    :return:
    """

    # Get parameters from user and throw away
    array_size = int(input())

    # Get array and convert to integers
    array_string = input()
    array = array_string.split()
    array = [int(val) for val in array]

    idx = array_size - 2
    to_move = array[idx + 1]
    while (array[idx] > to_move) and (idx >= 0):
        array[idx + 1] = array[idx]
        idx -= 1
        pretty_print(array)

    array[idx + 1] = to_move
    pretty_print(array)


run()
