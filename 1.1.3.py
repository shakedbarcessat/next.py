def division_4(x):
    """The function checks if the number divides with 4
      :param x: a number
      :type x: int
      :return: true is divide with 4, otherwise false
      :rtype: boolean
      """
    return x % 4 == 0

def four_dividers(number):
    """The function creates a list of all the numbers between 1 to number that divide with 4
      :param number: a number
      :type number: int
      :return: a list of all the numbers between 1 to number that divide with 4
      :rtype: list
      """
    return list(filter(division_4, range(1, number+1)))

"""
print(four_dividers(9))
print(four_dividers(3))
"""
