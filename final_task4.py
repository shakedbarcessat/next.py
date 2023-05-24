def gen_secs():
    """The function finds the next second.
      :return: returns the next second.
      :rtype: int
      """
    x = 0
    while x < 60:
        yield x
        x += 1


def gen_minutes():
    """The function finds the next minute.
      :return: returns the next minute.
      :rtype: int
      """
    x = 0
    while x < 60:
        yield x
        x += 1


def gen_hours():
    """The function finds the next hour.
      :return: returns the next hour.
      :rtype: int
      """
    x = 0
    while x < 24:
        yield x
        x += 1


def gen_time():
    """The function finds the next time: including hour, minute and second.
      :return: returns the next time: including hour, minute and second.
      :rtype: string
      """
    h = gen_hours()
    for i in range(24):
        r = next(h)
        m = gen_minutes()
        for x in range(60):
            e = next(m)
            s = gen_secs()
            for z in range(60):
                yield ("%02d:%02d:%02d" % (r, e, next(s)))


def gen_years(start=2023):
    """The function finds the next year, the default is 2023.
      :return: returns the next year.
      :rtype: int
      """
    year = start
    while year < 2024:
        yield year
        year += 1


def gen_months():
    """The function finds the next month.
      :return: returns the next month.
      :rtype: int
      """
    x = 1
    while x < 13:
        yield x
        x += 1


def gen_days(month, leap_year=True):
    """The function finds the next day in the month, with the importance of leap year.
      :return: returns the next day.
      :rtype: int
      """
    days_meuberet = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_not_meuberet = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year == True:
        yield days_meuberet[month - 1]
    else:
        yield days_not_meuberet[month - 1]


def gen_date():
    """The function finds the next date: including year, month, and day, hour, minute and second.
      :return: returns the next date.
      :rtype: string
      """
    for i in gen_years(2019):
        m = gen_months()
        for x in range(12):
            e = next(m)
            if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
                d = gen_days(e, True)
            else:
                d = gen_days(e, False)
            y = next(d)
            for w in range(1, y + 1):
                q = gen_time()
                for t in range(86400):
                    yield ("%02d/%02d/%02d" % (w, e, i) + "   " + str(next(q)))


gt = gen_date()
for i in range(1000000):
    next(gt)
print(next(gt))
for i in range(999999):
    next(gt)
print(next(gt))
for i in range(999999):
    next(gt)
print(next(gt))

