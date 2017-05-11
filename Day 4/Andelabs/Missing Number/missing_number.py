def find_missing(first_array, second_array):
    """
    Function that compares two arrays
    It returns the value that is in one and not the other
    """
    # If lists have the same entries
    if first_array == second_array:
        return 0
    # If the lists do not have same entries
    elif first_array != second_array:
        # Get the unique elements in the respective lists
        first = set(first_array)
        second = set(second_array)
        # Get the unique elements
        difference = first ^ second
        return list(difference)[0]
