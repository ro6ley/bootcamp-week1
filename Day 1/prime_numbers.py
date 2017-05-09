def prime_numbers_generator(number):
    """ Function to generate prime numbers from 0 to number """
    primes = []  # Initialize the list to contain the prime numbers generated
    if isinstance(number, int):
        if number <= 1:
            return []
        else:
            for item in range(2, number + 1):
                # Check if number is only divisible by itself and one only
                if all(item % i != 0 for i in range(2, item)):
                    primes.append(item)  # Add the number to the list of prime numbers
            return primes
    elif not isinstance(number, int):
        raise ValueError("Please enter an integer to generate a list of primes")
