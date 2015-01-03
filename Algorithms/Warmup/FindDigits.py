def find_digits(num_string):
    """
    Given the string representation of a number find the number of its digits which evenly divide the number

    :param num_string: the number to perform this calculation on
    :return: the number of digits of num which evenly divide num (repeated digits are counted for each repetition)
    """

    count = 0
    number = int(num_string)

    # For each digit of the string, if whole number mod the digit is 0, increment the count
    for digit in num_string:
        if digit == '0':
            continue
        elif (number % int(digit)) == 0:
            count += 1

    return count


def run():
    """
    Main method. User is to input numbers, the first of which is the number of numbers they wish to perform find_digits
    on. They then input those numbers and the result of each find_digits is printed
    :return:
    """

    # Get the number of numbers the user will input
    num_iters = int(input())

    # Get that many numbers from the user, and store result in the result array
    result = []
    for dummy in range(num_iters):
        result.append(find_digits(input()))

    # Print the result array
    for number in result:
        print(number)
        

run()