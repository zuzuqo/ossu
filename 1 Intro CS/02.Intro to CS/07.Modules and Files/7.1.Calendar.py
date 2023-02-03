import calendar as cal


def find_thanksgiving(year):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving


def find_canadian_thanksgiving(year):
    if year > 1957:
        month = cal.monthcalendar(year, 10)
        if month[0][cal.MONDAY] != 0:
            thanksgiving = month[1][cal.THURSDAY]
        else:
            thanksgiving = month[2][cal.THURSDAY]
        return thanksgiving
    else:
        return find_thanksgiving(year)


def shopping_days(year, country='USA'):
    october = 31
    november = 30
    christmas = 25
    if country.upper() == 'CANADA':
        thanksgiving = find_canadian_thanksgiving(year)
        return october + november + christmas - thanksgiving
    thanksgiving = find_thanksgiving(year)
    return november + christmas - thanksgiving


print(f'In 2022 Canada Thanksgiving was on October {find_canadian_thanksgiving(2022)}')
print(f'In 2022 U.S. Thanksgiving was on November {find_thanksgiving(2022)}')

print(f'Shopping days in Canada 2022: {shopping_days(2022, "Canada")}')
print(f'Shopping days in USA 2022: {shopping_days(2022)}')
