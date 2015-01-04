def operation_to_palindrome(word):
    """
    Determines the number of operations required to change the word into a palindrome where the only operations allowed
    are to change a letter into a "preceding" letter. B -> A is valid but B -> C is not
    :param word: the word to change into a palindrome
    :return: the number of shifts required to change the word into a palindrome
    """

    # Point to the beginning and end of the word
    low = 0
    high = len(word) - 1

    # Move each pointer toward each other, at each place determining the lexicographic distance of the characters
    # and using this to determine the number of shifts at each position
    num_changes = 0
    while low < high:
        num_changes += abs(ord(word[low]) - ord(word[high]))
        low += 1
        high -= 1

    return num_changes


def run():
    """
    "Main" method. Use is as follows:
        First enter the number of queries you will perform
        Then input that number of strings
        Afterwards prints the number of changes required to change each word into a palindrome
    :return: None, prints results
    """

    # Get number of numbers user will input
    num_iters = int(input())

    # Get that many numbers from the user, and store result in the result array
    result = []
    for dummy in range(num_iters):
        result.append(operation_to_palindrome(input()))

    # Print the results
    for res in result:
        print(res)


run()