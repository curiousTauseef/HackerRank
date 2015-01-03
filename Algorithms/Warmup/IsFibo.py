import math


def is_perfect_square(number):
    """
    Determines if the given number is a perfect square or not
    :param number: the number to determine if it is a perfect square
    :return: true if the number is a perfect square, false otherwise
    """

    root = math.floor(math.sqrt(number))
    return root**2 == number


def is_fibo(number):
    """
    Determines if the given number is a Fibonacci number. Utilizes the property given here:
    http://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers

    :param number: the number whose 'fibonacci-ness' we want to check
    :return: true if the number is a fibonacci number, false otherwise
    """

    # Just check to see if 5x^2 + 4 or 5x^2 - 4 is a perfect square
    return is_perfect_square(5*number**2 + 4) or is_perfect_square(5*number**2 - 4)


def run():
    """
    "Main" method. Use is as follows: First enter the number of numbers whose fibonacci-ness you want to determine.
        Then input the numbers
        Afterwards, the whether each is a fibonacci or not with be output
    :return: None, prints in order IsFibo or IsNotFibo depending of if each number input is a Fibonacci
    """

    # Get number of numbers user will input
    num_iters = int(input())

    # Get that many numbers from the user, and store result in the result array
    result = []
    for dummy in range(num_iters):
        result.append(is_fibo(int(input())))

    # Print the results
    for bool in result:
        if(bool):
            print("IsFibo")
        else:
            print("IsNotFibo")


run()