import subprocess

dirStr = '''K1
 K2
  K3
  K4
 K5
K6'''


def createDir(path, name):
    mkdir = subprocess.call([(path + name).strip()], shell=True)


def cdCommand(dir):
    if dir != '':
        return 'cd ' + dir + ';'
    return ''


def mkdirCommand(dir):
    return 'mkdir ' + dir


a = []
for d in dirStr.split('\n'):
    a.append((d.count(' '), d.strip()))
last = -1
lastPath = ''
lastName = ''
for i in a:
    if last < i[0]:
        last = i[0]
        lastPath = lastPath + ' ' + cdCommand(lastName)
    elif last > i[0]:
        balance = last - i[0]
        while balance > -1:
            lastPath = lastPath[:lastPath.rfind(';')]
            balance -= 1
        if lastPath.strip() == 'cd':
            lastPath = ''
        else:
            lastPath += ';'
    lastName = i[1]
    createDir(lastPath, mkdirCommand(lastName))
