import subprocess

compile = subprocess.call(['gcc', 'program.cpp', '-o program.o'], shell=True)
run = subprocess.call(['./program.o'], shell=True)

if run != 0:
    print 'Dzialanie programu zakonczylo sie bledem'
else:
    print 'Program dziala poprawnie'