def find_max_xor(min_num, max_num):
    """
    Find the value of the maximum bitwise xor of any number in the range of min_num and max_num
    :param min_num: the lowest number in the range to consider
    :param max_num: the largest number in the range to consider
    :return: the value of the maximum bitwise xor of any two numbers between min_num and max_num inclusive
    """

    # Initialize best to be the xor of the given minimum and maximum numbers
    best = min_num ^ max_num

    # Go through each unchecked combination brute-force style. I'm not sure there is a better way to do this than
    # simply brute-forcing it
    for num1 in range(min_num, max_num + 1):
        for num2 in range(num1, max_num + 1):
            if num1 ^ num2 > best:
                best = num1 ^ num2

    return best


def run():
    """
    Solves the "Maximizing XOR" Challenge from HackerRank
    Usage:
        Enter the minimum number of the range
        Enter the maximum of the range

        Prints the maximum xor of any two numbers in the range
    :return:
    """
    print(find_max_xor(int(input()), int(input())))


run()