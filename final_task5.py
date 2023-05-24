import functools

class IDIterator:
    def __init__(self, id):
        self._id=id
        self._number=id+1

    def __iter__(self):
        return self

    def __next__(self):
        if self._id==999999999:
            raise StopIteration
        while check_id_valid(self._number)==False:
            self._number += 1
        self._number += 1
        return self._number-1

def add(x, y):
    """The function sums up x and y
      :param x: number
      :type x: int
      :param y: number
      :type y: int
      :return: returns the sum of x and y
      :rtype: int
      """
    return x + y

def check_id_valid(id_number):
    """The function checks if id_number is valid or not
      :param id_number: id
      :type id_number: int
      :return: true if the id is valid, else false
      :rtype: boolean
      """
    digits = [int(i) for i in str(id_number)]
    digits=[digits[i] if i%2==0 else digits[i]*2 for i in range(len(digits))]
    digits=[digit%10+int(digit/10)%10 if digit>9 else digit for digit in digits]
    sum= functools.reduce(add, digits)
    if sum % 10==0:
        return True
    return False

def id_generator(id_number):
    """The function returns the next valid id
      :param id_number: id
      :type id_number: int
      :return: the next valid id
      :rtype: int
      """
    num= id_number+1
    while True:
        while check_id_valid(num)==False:
            num+=1
        yield num
        num+=1


id_input= int(input("Enter id: "))
choice= input("Generator or Iterator? (gen/it)? ")
if choice=="it":
    id= IDIterator(id_input)
    for i in range(10):
        print(id.__next__())

elif choice=="gen":
    id=id_generator(id_input)
    for i in range(10):
        print(next(id))
