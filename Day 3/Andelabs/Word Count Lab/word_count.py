def words(input_string):
    """
    This function receives a string input
    It returns a dictionary that contains each word in the list
    and the number of times the word appears in the string
    """
    # create a new empty dictionary
    word_count = {}
    # Extract the words from the string ad add them to a list
    words_list = input_string.split()
    for word in words_list:
        try:
            # convert integers in the string to be stored as integers in the final result and not string
            word = int(word)
            try:
                # Check if the word already exists in the dictionary and update the occurrences value by one
                if word_count[word]:
                    word_count[word] += 1
            # If the word does not exist in the dictionary, add it and set its occurrence value to 1
            except KeyError:
                word_count[word] = 1

        # If there are no integers in the string
        except ValueError:
            try:
                # Check if the word already exists in the dictionary and update the occurrences value by one
                if word_count[word]:
                    word_count[word] += 1
            # If the word does not exist in the dictionary, add it and set its occurrence value to 1
            except KeyError:
                word_count[word] = 1

    return word_count

print(words("hello 1 2"))
