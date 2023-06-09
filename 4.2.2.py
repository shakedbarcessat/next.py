def parse_ranges(ranges_string):
    """The function returns the numbers in the ranges.
      :param ranges_string: ranges of numbers
      :type ranges_string: string
      :return: returns the numbers in the ranges.
      :rtype: list
      """
    lists= (c.split('-') for c in ranges_string.split(','))
    list = []
    for i in lists:
        for n in range(int(i[0]), int(i[1]) + 1):
            list.append(n)
    return list



print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))
