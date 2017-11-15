width = input('Podaj rozmiar: ')
with open('zadanie_1_file.txt') as file:
    text = ''.join(file.readlines()).replace('\n', '')
    while text:
        print text[:width].center(30)
        text = text[width:]
