'''
Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


def p19():
    leap = {}
    months = {
        "jan": 31,
        "feb": 28,
        "mar": 31,
        "apr": 30,
        "may": 31,
        "jun": 30,
        "jul": 31,
        "aug": 31,
        "sep": 30,
        "oct": 31,
        "nov": 30,
        "dec": 31,
    }

    dd = ["Monday", "Tuesday", "Wednesday",
          "Thursday", "Friday", "Saturday", "Sunday"]
    calendar = dict()

    # 01.01.1900 = Monday -> 07.01.1900 = Sunday
    # day 7, 14, 21 etc.

    for y in range(1901, 2001):
        if y % 4 == 0:
            if y % 100 == 0 and y % 400 != 0:
                leap[y] = False
            else:
                leap[y] = True
        else:
            leap[y] = False

    numDays = 0
    sundays = 0

    for year, leap in leap.items():
        for month, days in months.items():
            if month == 'feb' and leap:
                days += 1
            for d in range(days):
                day = dd[numDays % 7]
                da = {day: d}
                mo = {month: da}
                ye = {year: mo}
                if da.get('Sunday') == 1:
                    sundays += 1
                    print(ye)
                numDays += 1
        # break
    print(sundays)


def main():
    p19()


if __name__ == '__main__':
    main()
