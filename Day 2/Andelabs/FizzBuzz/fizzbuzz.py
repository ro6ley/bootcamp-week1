def fizz_buzz(n):
    """
    This function takes in an argument 'n' which is an integer
    It returns Fizz if n is divisible by 3
    It returns Buzz if n is divisible by 5
    It returns FizzBuzz if n is divisible by both 3 and 5
    It returns the n if it is not divisible by 3 or 5
    """

    # n divisible by bot 3 and 5
    if (n % 3) == 0 and (n % 5) == 0:
        return "FizzBuzz"

    # n divisible by 3
    elif (n % 3) == 0:
        return "Fizz"

    # n divisible by 5
    elif (n % 5) == 0:
        return "Buzz"

    # n not divisible by 3 or 5
    else:
        return n
