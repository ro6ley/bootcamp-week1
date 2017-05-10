def words(input_string):
    """
    This function receives a string input
    It returns a dictionary that contains each word in the list
    and the number of times the word appears in the string
    """
    word_count = {}
    words_list = input_string.split()
    for word in words_list:
        try:
            if word_count[word]:
                word_count[word] += 1
        except KeyError:
                word_count[word] = 1

    return word_count

print(words("hello friend"))