class BinarySearch(list):
    """
    This class inherits from the list class.
    The __init__() takes two integers as parameters
    The first is is the length of the list.
    The second is the difference between the consecutive values.
    It initializes an instance variable 'length'
    It has a method called search that takes one argument that is the value to be found
    The search method returns a dictionary object that contains count, index.
    The search method implements the binary search algorithm
    """
    def __init__(self, a, b):
        data = []
        list_len = 1
        while list_len < a:
            data.append(data[list_len - 1] + b)
            list_len += 1
        super(BinarySearch, self).__init__(data)
        self.length = len(data)

    def search(self, number):
        pass

