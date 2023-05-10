def gen_secs():
    x = 0
    while x < 60:
        yield x
        x += 1


def gen_minutes():
    x = 0
    while x < 60:
        yield x
        x += 1


def gen_hours():
    x = 0
    while x < 24:
        yield x
        x += 1


def gen_time():
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
    year = start
    while year < 2024:
        yield year
        year += 1


def gen_months():
    x = 1
    while x < 13:
        yield x
        x += 1


def gen_days(month, leap_year=True):
    days_meuberet = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_not_meuberet = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year == True:
        yield days_meuberet[month - 1]
    else:
        yield days_not_meuberet[month - 1]


def gen_date():
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

