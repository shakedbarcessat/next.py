def is_prime(number):
    return number>2 and [False if (number % i == 0) else True for i in range(2, int(number))][0]


print(is_prime(42))
print(is_prime(43))