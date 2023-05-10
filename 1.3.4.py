def decode(password):
    """The function returns the decode password
      :param password: password to decode
      :type password: string
      :return: returns the decode password
      :rtype: string
      """
    return ''.join([x if not x.isalpha() else chr(ord(x) + 2) for x in password])

"""
print(decode("sljmai ugrf rfc ambc: lglc dmsp mlc rum"))
"""