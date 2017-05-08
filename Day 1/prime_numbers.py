def prime_numbers_generator(n):
    """ Function to generate prime numbers for 0 to n """
    primes = []  # Initialize the list to contain the prime numbers generated
    if isinstance(n, int):
        for number in range(2, n + 1):
            # Check if number is only divisible by itself and one only
            if all(number % i != 0 for i in range(2, number)):
                primes.append(number)  # Add the number to the list of prime numbers
        return primes
    elif not isinstance(n, int):
        raise ValueError("Please enter an integer to generate a list of primes")

