import functools
def add(x, y):
    """The function sums x and y
       :param x: a number
       :type x: int
       :param y: a number
       :type y: int
       :return: sum of x and y
       :rtype: int
       """
    return int(x) + int(y)

def sum_of_digits(number):
    """The function sums the number digits
       :param number: a number
       :type number: int
       :return: return the sum the number digits
       :rtype: int
       """
    return functools.reduce(add, (list(str(number))))

"""
print(sum_of_digits(104))
"""