def intersection(list_1, list_2):
    """The function creates a list of numbers that are both in list 1 and list 2
      :param list_1: list of numbers
      :type list_1: list
      :param list_2: list of numbers
      :type list_2: list
      :return: returns a list of numbers that are both in list 1 and list 2
      :rtype: list
      """
    return list(set([i for i in list_1 if i in list_2]))

"""
print(intersection([1, 2, 3, 4], [8, 3, 9]))
print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
"""