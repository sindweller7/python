class Leap_year:
    def __init__(self, year):
        self.year = int(year)

    def answer(self):
        y = self.year
        if y % 400 ==0:
            if y % 100 == 0:
                return "{0}是闰年".format(y)
            else:
                return "{0}不是闰年".format(y)
        else:
            if y % 4 == 0:
                return "{0}是闰年".format(y)
            else:
                return "{0}不是闰年".format(y)
