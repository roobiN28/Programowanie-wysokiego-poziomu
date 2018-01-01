jednostki = ['', 'jeden', 'dwa', 'trzy', 'cztery', 'piec', 'szesc', 'siedem', 'osiem', 'dziewiec']
dziesiec_dziewietnascie = ['dziesiec', 'jedenascie', 'dwanascie', 'trzynascie', 'czternascie', 'pietnascie',
                           'szesnascie', 'siedemnascie', 'osiemnascie', 'dziewietnascie']
dziesiatki = ['', '', 'dwadziescia', 'trzydziesci', 'czterdziesci', 'piecdziesiat', 'szescdziesiat', 'siedemdziesiat',
              'osiemdziesiat', 'dziewiecdziesiat']
setki = ['', 'sto', 'dwiescie', 'trzysta', 'czterysta', 'piecset', 'szescset', 'siedemset', 'osiemset', 'dziewiecset']

n = raw_input('Wpisz liczbe:')
n = int(n)
s = n / 100
if s != 0:
    n = n % 100
d = n / 10
if d != 0:
    n = n % 10
j = n

text = ''
text += setki[s] + ' '
if d == 1:
    text += dziesiec_dziewietnascie[j] + ' '
else:
    if d != 0:
        text += dziesiatki[d] + ' '
    text += jednostki[j] + ' '

print text.strip()