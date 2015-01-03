def num_consecutive_chars(str):
    """
    Get the number of consecutive characters in str which are the same
    :param str: the string to consider
    :return: the number of consecutive characters in str which are the same
    """

    count = 0

    for idx in range(len(str) - 1):
        if str[idx] == str[idx + 1]:
            count += 1

    return count


def run():
    """
    "Main" method. Use is as follows:
        First enter the number of queries you will perform
        Then input that number of strings
        Afterwards prints the number of deletions required so that the strings do not have consecutive repeated characters
    :return: None, prints results
    """

    # Get number of numbers user will input
    num_iters = int(input())

    # Get that many numbers from the user, and store result in the result array
    result = []
    for dummy in range(num_iters):
        result.append(num_consecutive_chars(input()))

    # Print the results
    for res in result:
        print(res)


run()