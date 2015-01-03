def get_tree_height(num_cycles):
    """
    Get the height of the utopian tree after the given number of "cycles"
    :param num_cycles: the number of cycles of growth to "simulate"
    :return: the height of the tree
    """

    # Base case, at 0 cycles the tree is of height 1
    if num_cycles < 1:
        return 1

    # Recursive case 1, in the spring (odd numbered cycles) the tree's height doubles
    elif num_cycles % 2 == 1:
        return get_tree_height(num_cycles - 1) * 2

    # Recursive case 2, in the summer (even numbered cycles) the tree's height increases by 1
    elif num_cycles % 2 == 0:
        return get_tree_height(num_cycles - 1) + 1


def run():
    """
    "Main" method. Use is as follows:
        First enter the number of queries you will perform
        Then input the number of cycles at which you want to know the tree's height
        Afterwards prints the height at the corresponding number of cycles
    :return: None, prints results
    """

    # Get number of numbers user will input
    num_iters = int(input())

    # Get that many numbers from the user, and store result in the result array
    result = []
    for dummy in range(num_iters):
        result.append(get_tree_height(int(input())))

    # Print the results
    for height in result:
        print(height)


run()