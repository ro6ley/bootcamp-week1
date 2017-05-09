def data_type(item):
    """
    Function that takes input 'item' and returns results based on the input as follows
    - For strings it returns its length
    - For None it returns a string 'no value'
    - For booleans it returns the boolean
    - For integers it returns a string showing how it compares to 100
    - For lists it returns the 3rd item or None if it does not exist
    """
    # For strings
    if type(item) is str:
        return len(item)

    # For None
    elif item is None:
        return "no value"

    # For booleans
    elif type(item) is bool:
        return item

    # For integers
    elif type(item) is int:
        if item < 100:
            return "less than 100"
        elif item == 100:
            return "equal to 100"
        return "more than 100"

    # For lists
    elif type(item) is list:
        if len(item) < 3:
            return None
        else:
            return item[2]
