import math

value = raw_input('Podaj liczbe: ')

try:
    intValue = float(value)

except ValueError:
    print 'Nie podales prawidlowej liczby'

try:
    print math.sqrt(intValue)
except ValueError:
    print 'Podales ujemna liczbe'
