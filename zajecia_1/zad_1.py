name = raw_input("Podaj imie: ")
surname = raw_input("Podaj nazwisko: ")
age = raw_input("Podaj wiek: ")

if age > 18:
    ageMessage = 'PELNOLETNI'
else:
    ageMessage = 'NIEPELNOLETNI'

print 'Czesc ' + name + ' ' + surname + ', jestes ' + ageMessage