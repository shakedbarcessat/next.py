def is_funny(string):
    """The function checks if the string contains only the chars h and a.
      :param string: string of letters
      :type string: string
      :return: returns true if the string contains only the chars h and a.
      :rtype: boolean
      """
    return not False in [False if (char != 'h') and (char != 'a') else True for char in string]

"""
print(is_funny("hahahahahaha"))
"""