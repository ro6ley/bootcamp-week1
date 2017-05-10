def find_max_min(input_list):
    """
    This function takes a list of integers as input
    It returns a list that contains the largest and smallest integers
    If the maximum and minimum are equal it returns the number of elements in the list
    """
    # Create an empty list to add to and return
    new_list = []
    # Confirm that the largest and smallest integers are not equal
    if min(input_list) != max(input_list):
        new_list.append(min(input_list))
        new_list.append(max(input_list))
        return new_list

    # Check if the largest and smallest integers are equal and return the length of the list
    elif min(input_list) == max(input_list):
        new_list.append(len(input_list))
        return new_list
