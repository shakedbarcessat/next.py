def is_prime(number):
    """The function checks if the number is prime.
      :param number: a number
      :type number: int
      :return: returns true if the number is prime, else returns false.
      :rtype: boolean
      """
    return number>2 and [False if (number % i == 0) else True for i in range(2, int(number))][0]


print(is_prime(42))
print(is_prime(43))