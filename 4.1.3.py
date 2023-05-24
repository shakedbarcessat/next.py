def is_prime(n):
    """The function checks if the number is prime.
      :param n: a number
      :type n: int
      :return: returns true if the number is prime, else returns false.
      :rtype: boolean
      """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def first_prime_over(n):
    """The function checks the next prime number.
      :param n: number
      :type n: int
      :return: returns the next prime number.
      :rtype: int
      """
    prime_generator = (i for i in range(n+1, 2*n+1) if is_prime(i))
    return next(prime_generator)


print(first_prime_over(1000000))
