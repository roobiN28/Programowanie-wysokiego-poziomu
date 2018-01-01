def comparator(x, y):
    if type(x) is type(y):
        if x > y:
            return 1
        elif x == y:
            return 0
        else:
            return -1
    if type(x) > type(y):
        return -1
    elif type(x) == type(y):
        return 0
    else:
        return 1


class List(object):
    def __init__(self):
        self.tab = []

    def add(self, item):
        self.tab.append(item)

    def delete(self, index):
        try:
            item = self.tab[index]
            self.tab.remove(item)
        except IndexError:
            raise IndexError('Usuwanie. Nie istnieje index o takim numerze w liscie')

    def get(self, index):
        try:
            return self.tab[index]
        except IndexError:
            raise IndexError('Pobieranie. Nie istnieje index o takim numerze w liscie')

    def sort(self):
        self.tab = sorted(self.tab, cmp=comparator)

    def __str__(self):
        ret = ''
        for item in self.tab:
            ret += str(item) + ' '
        return ret.strip()

    def __getitem__(self, item):
        return self.get(item)

    def __eq__(self, o):
        if len(self.tab) != len(o.tab):
            print len(self.tab)
            print len(o.tab)
            return False
        i = 0
        print len(self.tab)
        print len(o.tab)
        while i < len(self.tab):
            if comparator(self.tab[i], o[i]) != 0:
                return False
            i += 1
        return True


list = List()
list.add('ala')
list.add(50)
list.add('kot')
list.add(10)
list.add('ala')
list.add('b')
list.sort()
print list
