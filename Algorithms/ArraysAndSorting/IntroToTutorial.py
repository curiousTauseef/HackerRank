def run():
    """
    "Main" method. Usage is:
        User inputs the number to be searched, V
        User inputs the size of the array to be input, N
        User inputs the array of size N

        Program prints the index of V in the given array
    :return: None, prints to stdout
    """

    # Get parameters from user
    to_find = int(input())
    array_size = int(input())

    array_string = input()

    array = array_string.split()
    array = [int(val) for val in array]

    print(array.index(to_find))


run()