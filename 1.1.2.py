def double_char(ch):
    """The function doubles the char
      :param ch: char of the string
      :type ch: char
      :return: the char written twice
      :rtype: string
      """
    return ch*2

def double_letter(my_str):
    """The function creates a string when each char is double
      :param my_str: string as an input
      :type my_str: string
      :return: string when each char is double
      :rtype: string
      """
    return ''.join(list(map(double_char, list(my_str))))


"""
print(double_letter("python"))
print(double_letter("we are the champions!"))
"""